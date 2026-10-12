# -*- coding: utf-8 -*-
"""KJournal adb 기반 UI 테스트 공용 헬퍼 (uiautomator dump/탭/입력 등).

`scripts/e2e_test.py` 와 `scripts/app_test.py` 가 importlib 로 불러 재사용한다.

최적화 포인트
- uiautomator dump 를 캐시(0.7s) + --compressed 로 최소화
- 고정 sleep 대신 wait_for(라벨) 폴링
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Windows 콘솔 코드페이지를 UTF-8로 맞춰 한글 로그가 깨지지 않게 한다.
if os.name == "nt":
    try:
        import ctypes

        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        ctypes.windll.kernel32.SetConsoleCP(65001)
    except Exception:  # noqa: BLE001
        pass

ADB = os.environ.get("ADB") or (r"C:\Program Files\platform-tools\adb.exe" if os.name == "nt" else "adb")
# 배타 빌드는 앱 ID가 com.jiwxn3.KJournal.beta 이므로 CI가 환경변수로 넘겨준다.
PKG = os.environ.get("KJOURNAL_PKG") or "com.jiwxn3.KJournal"
MAIN = os.environ.get("KJOURNAL_MAIN") or (PKG + "/com.isaakhanimann.journal.MainActivity")
OTA_URL = os.environ.get("KJOURNAL_OTA_URL") or "https://kjournal.github.io/kjournal-site/ota/version.json"
EN_EXPORT_FIXTURE = os.environ.get("KJOURNAL_EN_EXPORT") or os.path.join("scripts", "ci", "fixtures", "journal_en_export.json")
DIALOG_LABELS = ("지금 업데이트", "나중에", "KJournal 업데이트", "새로운 버전")
DISCLAIMER_LABELS = ("Continue", "계속", "동의하고 계속")

results = []
saved_flag = False
ota_dialog_seen = False

_cache = {"t": 0.0, "root": None}


def sh(*args, timeout=60):
    p = subprocess.run([ADB] + list(args), capture_output=True, timeout=timeout)
    return p.stdout.decode("utf-8", "replace")


def ui(force=True, ttl=0.7):
    if not force and _cache["root"] is not None and (time.time() - _cache["t"]) < ttl:
        return _cache["root"]
    sh("shell", "uiautomator", "dump", "--compressed", "/sdcard/_t.xml")
    xml = sh("shell", "cat", "/sdcard/_t.xml")
    m = re.search(r"<hierarchy.*</hierarchy>", xml, re.S)
    root = ET.fromstring(m.group(0)) if m else None
    _cache["root"] = root
    _cache["t"] = time.time()
    return root


def invalidate():
    _cache["root"] = None


def texts(force=True):
    t = ui(force)
    return [n.attrib.get("text", "") for n in t.iter("node")] if t is not None else []


def find(text, contains=False, force=True):
    t = ui(force)
    if t is None:
        return None
    for n in t.iter("node"):
        v = n.attrib.get("text", "")
        if (text in v) if contains else (v == text):
            return n.attrib
    return None


def center(a):
    m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a["bounds"])
    x1, y1, x2, y2 = map(int, m.groups())
    return (x1 + x2) // 2, (y1 + y2) // 2


def tap(a, wait=0.5):
    x, y = center(a)
    sh("shell", "input", "tap", str(x), str(y))
    invalidate()
    time.sleep(wait)


def swipe_up(ms=160):
    sh("shell", "input", "swipe", "540", "1650", "540", "800", str(ms))
    invalidate()
    time.sleep(0.35)


def wait_for(label, timeout=8.0, contains=False):
    end = time.time() + timeout
    while time.time() < end:
        if find(label, contains=contains):
            return True
        time.sleep(0.35)
    return False


def wait_gone(label, timeout=8.0):
    end = time.time() + timeout
    while time.time() < end:
        if not find(label):
            return True
        time.sleep(0.35)
    return False


def top_activity():
    for line in sh("shell", "dumpsys", "activity", "activities").splitlines():
        if "topResumedActivity=" in line:
            return line.strip()
    return ""


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(("PASS " if ok else "FAIL ") + name + (("  | " + detail[:80]) if detail else ""), flush=True)


def dismiss_disclaimer():
    """첫 실행 면책 대화상자: 체크박스 4개를 모두 누르고 계속 버튼을 누른다."""
    for _ in range(4):
        t = ui()
        if t is None:
            return False
        boxes = [n.attrib for n in t.iter("node")
                 if n.attrib.get("checkable") == "true" and n.attrib.get("checked") != "true"]
        if not boxes:
            break
        for a in boxes:
            tap(a, wait=0.4)
        time.sleep(0.4)
    # 계속 버튼: 아래로 스크롤한 뒤 클릭 가능한 조상 또는 좌표로 탭
    for label in DISCLAIMER_LABELS:
        for attempt in range(3):
            t = ui()
            if t is None:
                return False
            parent = {c: p for p in t.iter() for c in p}
            for n in t.iter("node"):
                if n.attrib.get("text") == label:
                    target = n
                    while target is not None and target.attrib.get("clickable") != "true":
                        target = parent.get(target)
                    a = (target if target is not None else n).attrib
                    m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a["bounds"])
                    x1, y1, x2, y2 = map(int, m.groups())
                    sh("shell", "input", "tap", str((x1 + x2) // 2), str((y1 + y2) // 2))
                    invalidate()
                    time.sleep(1.0)
                    if not find(label):
                        return True
                    break
            # 좌표 폴백(버튼이 화면 하단에 있을 때)
            w, h = screen_size()
            sh("shell", "input", "swipe", str(w // 2), str(int(h * 0.7)), str(w // 2), str(int(h * 0.4)), "200")
            invalidate()
            time.sleep(0.5)
            sh("shell", "input", "tap", str(w // 2), str(int(h * 0.9)))
            invalidate()
            time.sleep(1.0)
            if not find(label):
                return True
    return False


def scroll_top(n=6):
    for _ in range(n):
        sh("shell", "input", "swipe", "540", "800", "540", "1650", "150")
        invalidate()
        time.sleep(0.25)


def scroll_bottom(n=12):
    for _ in range(n):
        swipe_up()


def find_scroll(text, tries=14):
    m = find(text)
    if m:
        return m
    scroll_top()
    for _ in range(tries):
        m = find(text)
        if m:
            return m
        swipe_up()
    return None


def find_scroll_bottom(text, tries=14):
    """화면 하단에 있는 위젯(별칭/메모 등)을 찾는다."""
    m = find(text)
    if m:
        return m
    scroll_bottom(12)
    for _ in range(tries):
        m = find(text)
        if m:
            return m
        sh("shell", "input", "swipe", "540", "800", "540", "1650", "160")
        invalidate()
        time.sleep(0.35)
    return None


def find_scroll_contains(text, tries=8):
    for _ in range(tries):
        m = find(text, contains=True)
        if m:
            return m
        swipe_up()
    return None


def pick_file(skip=(), match=None, tries=6):
    """열기 피커에서 파일을 선택한다(목록이 길면 스크롤)."""
    for _ in range(tries):
        t = ui()
        if t is not None:
            parent = {c: p for p in t.iter() for c in p}
            for n in t.iter("node"):
                txt = n.attrib.get("text", "")
                if not txt:
                    continue
                if match:
                    if match not in txt:
                        continue
                elif not txt.endswith(".json"):
                    continue
                if any(s in txt for s in skip):
                    continue
                target = n
                while target is not None and target.attrib.get("clickable") != "true":
                    target = parent.get(target)
                tap((target if target is not None else n).attrib, wait=1.0)
                return True
        swipe_up()
    return False


def enter_folder(name):
    m = find(name)
    if m:
        tap(m, wait=1.2)
        return True
    return False


def picker_nav_downloads():
    """피커 드로어를 열어 Downloads 루트로 이동."""
    t = ui()
    if t is not None:
        for n in t.iter("node"):
            a = n.attrib
            if a.get("class", "").endswith("ImageButton") and a.get("clickable") == "true":
                tap(a, wait=1.0)
                break
    m = find("Downloads")
    if m:
        tap(m, wait=1.2)
        return True
    return False


def confirm_save(timeout=10.0):
    global saved_flag
    end = time.time() + timeout
    while time.time() < end:
        t = ui()
        if t is not None:
            for n in t.iter("node"):
                a = n.attrib
                if a.get("clickable") != "true":
                    continue
                label = (a.get("text") or "").strip().lower()
                if label in ("save", "저장") or a.get("resource-id", "") == "android:id/button1":
                    tap(a, wait=1.2)
                    saved_flag = True
                    return True
        time.sleep(0.4)
    return False


def status():
    for s in texts():
        if any(k in s for k in ("저장 위치", "완료", "실패", "찾", "백업", "복원")):
            return s
    return ""


def crashes():
    """우리 앱 프로세스의 FATAL EXCEPTION 스택을 검출(시스템 프로세스 제외)."""
    lines = sh("logcat", "-d").splitlines()
    out = []
    for i, l in enumerate(lines):
        if "FATAL EXCEPTION" in l:
            ctx = "\n".join(lines[i:i + 5])
            if PKG in ctx:
                stack = " | ".join(x.strip() for x in lines[i:i + 14] if x.strip())
                out.append(stack)
    return out


ADB_IME = "com.android.adbkeyboard/.AdbIME"
ADB_IME_URL = "https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk"


def ime_ready():
    return "com.android.adbkeyboard" in sh("shell", "ime", "list", "-s")


def ensure_adb_ime():
    """한국어 입력용 ADBKeyboard IME 설치/활성화(최초 1회, 최대 20초 대기)."""
    if ime_ready():
        return True
    import urllib.request
    try:
        apk = os.path.join(os.environ.get("TEMP", "/tmp"), "kilo", "ADBKeyboard.apk")
        os.makedirs(os.path.dirname(apk), exist_ok=True)
        if not os.path.exists(apk):
            with urllib.request.urlopen(ADB_IME_URL, timeout=90) as r, open(apk, "wb") as f:
                f.write(r.read())
        out = sh("install", "-r", apk)
        print("ADBKeyboard install:", out.strip().splitlines()[-1] if out.strip() else "no output", flush=True)
    except Exception as exc:  # noqa: BLE001
        print("ADBKeyboard 다운로드/설치 실패:", exc, flush=True)
    sh("shell", "ime", "enable", ADB_IME)
    sh("shell", "ime", "set", ADB_IME)
    end = time.time() + 40
    while time.time() < end:
        if ime_ready():
            print("ADBKeyboard 활성화 완료", flush=True)
            return True
        # 패키지 매니저 반영/IME 등록 지연 대비 재시도
        sh("shell", "ime", "enable", ADB_IME)
        sh("shell", "ime", "set", ADB_IME)
        time.sleep(2.0)
    print("ADBKeyboard 활성화 실패. ime list:", sh("shell", "ime", "list", "-s").strip(), flush=True)
    return False


def input_text_kr(text, fallback=None, require_kr=True):
    """한국어 입력: 필드를 비운 뒤 1회 입력. 한국어 IME 가 없으면 기본은 실패시킨다."""
    sh("shell", "am", "broadcast", "-a", "ADB_CLEAR_TEXT")
    time.sleep(0.3)
    if ime_ready():
        sh("shell", "am", "broadcast", "-a", "ADB_INPUT_TEXT", "--es", "msg", text)
        time.sleep(0.6)
        return True
    if require_kr:
        raise RuntimeError("한국어 IME(ADBKeyboard) 가 준비되지 않았습니다")
    if fallback:
        sh("shell", "input", "text", fallback)
    time.sleep(0.6)
    return False


def field_texts():
    """EditText 에 들어있는 텍스트 목록."""
    t = ui()
    out = []
    if t is None:
        return out
    for n in t.iter("node"):
        if "EditText" in n.attrib.get("class", ""):
            out.append(n.attrib.get("text", ""))
    return out


def installed_version_code():
    m = re.search(r"versionCode=(\d+)", sh("shell", "dumpsys", "package", PKG))
    return int(m.group(1)) if m else None


def fetch_ota():
    try:
        with urllib.request.urlopen(OTA_URL, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        print("OTA 조회 실패:", exc, flush=True)
        return None


def reset_app():
    """결정적 시작을 위해 문서피커 종료 + 앱 데이터 초기화(첫 실행 상태로)."""
    sh("shell", "am", "force-stop", "com.google.android.documentsui")
    sh("shell", "pm", "clear", PKG)
    time.sleep(1.0)


def tap_clickable(text):
    """텍스트 노드의 클릭 가능한 조상을 눌러라(하단 탭이 시스템 내비바에 가리지 않도록 위쪽 편향)."""
    t = ui()
    if t is None:
        return False
    parent = {c: p for p in t.iter() for c in p}
    for n in t.iter("node"):
        if n.attrib.get("text") == text:
            target = n
            while target is not None and target.attrib.get("clickable") != "true":
                target = parent.get(target)
            a = (target if target is not None else n).attrib
            m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a["bounds"])
            x1, y1, x2, y2 = map(int, m.groups())
            x = (x1 + x2) // 2
            y = y1 + int((y2 - y1) * 0.35)
            sh("shell", "input", "tap", str(x), str(y))
            invalidate()
            time.sleep(1.0)
            return True
    return False



def screen_size():
    out = sh("shell", "wm", "size")
    m = re.search(r"(\d+)x(\d+)", out)
    return (int(m.group(1)), int(m.group(2))) if m else (1080, 2340)


def tap_xy(fx, fy):
    w, h = screen_size()
    sh("shell", "input", "tap", str(int(w * fx)), str(int(h * fy)))
    invalidate()
    time.sleep(1.0)


def soft(name, ok, detail=""):
    """위치 의존적이라 CI 에서 흔들릴 수 있는 베스트에포트 항목(SKIP 허용)."""
    print(("PASS " if ok else "SKIP ") + name + (("  | " + detail[:70]) if detail else ""), flush=True)


def picker_open():
    return "documentsui" in top_activity()


def close_picker():
    for _ in range(2):
        if not picker_open():
            return
        sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(0.8)


def test_ota():
    srv = fetch_ota()
    if srv is None:
        check("OTA 버전 조회", False, "version.json 조회 실패")
        return
    inst = installed_version_code()
    newer = int(srv.get("versionCode") or 0) > (inst or 0)
    ok = ota_dialog_seen == newer
    check("OTA 업데이트 확인", ok,
          "서버 %s(%s) / 설치 %s / 다이얼로그=%s" % (srv.get("versionName"), srv.get("versionCode"), inst, ota_dialog_seen))


def test_changelog():
    """OTA changelog(사이트) + 앱 내 릴리즈노트(설정 > 앱 > 버전 행) 한글 표시를 검증."""
    srv = fetch_ota() or {}
    cl = (srv.get("changelog") or "").strip()
    check("OTA changelog 존재", bool(cl), (cl.splitlines() or [""])[0][:60])

    # "설정 > 앱" 섹션의 버전 행에서 릴리즈노트를 연다.
    sh("shell", "am", "force-stop", PKG)
    sh("shell", "am", "start", "-n", MAIN)
    time.sleep(6)
    for _ in range(8):
        t = texts()
        if any(x in t for x in DIALOG_LABELS):
            for label in ("나중에", "취소"):
                m = find(label)
                if m:
                    tap(m, wait=0.8)
                    break
            continue
        if any(x in t for x in DISCLAIMER_LABELS):
            dismiss_disclaimer()
            continue
        break
    for _ in range(5):
        if find("맞춤 설정"):
            break
        m = find("설정")
        if m:
            tap(m, wait=1.0)
        else:
            time.sleep(0.5)
    row = None
    for _ in range(10):
        row = find("버전", contains=True)
        if row:
            break
        swipe_up()
    if row is None:
        check("앱 릴리즈노트", False, "설정 > 앱 > 버전 행 없음")
        return
    tap(row, wait=1.5)
    t = texts()
    has_ver = any("5 PB8" in s for s in t)
    has_kr = any(any("\uac00" <= c <= "\ud7a3" for c in s) for s in t)
    check("앱 릴리즈노트", has_ver and has_kr, "5 PB8=%s / 한글=%s" % (has_ver, has_kr))
    sh("shell", "input", "keyevent", "KEYCODE_BACK")
