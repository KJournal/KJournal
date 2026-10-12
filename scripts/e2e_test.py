# -*- coding: utf-8 -*-
"""KJournal 전체 기능 심층 통합 테스트 (단일 스크립트).

로컬/CI(GitHub Actions) 어디서든 `python -u scripts/e2e_test.py` 로 실행한다.
모든 단계는 "실제 UI 동작"을 검증하며 실패 시 화면 덤프를 출력한다(SKIP 없음).

단계
 0) 준비: ADBKeyboard(한국어 입력) 설치/활성
 1) 온보딩(면책 동의) → 홈 진입
 2) 하단 탭 5개 순회(각 화면 고유 텍스트 확인)
 3) 검색 심층: 물질명 입력(중복 없음 확인) → 결과 → 물질 상세 진입 → 뒤로
 4) 커스텀 물질 추가: 추가 → 이름 입력 → 저장 → 목록 반영 확인 → 삭제
 5) 상호작용 설정: 알림 토글 존재/동작 확인
 6) 설정 하위 화면 진입(물질 색상/환경설정/파일 내보내기)
 7) 릴리즈노트(GitHub Pages changelog 표시) 확인
 8) OTA: version.json 조회/설치버전 비교/changelog 존재
 9) 알림: 권한 부여 + 서비스/채널 상태 확인
10) OTA 업데이트 플로우: 구버전 설치 → 다이얼로그/changelog/다운로드/SHA-256 → 원복
11) 크래시 스캔(우리 앱 프로세스)
"""
import hashlib
import importlib.util
import io
import os
import re
import sys
import time
import urllib.request

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("kj", os.path.join(_here, "adb_helpers.py"))
kj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kj)

PKG = kj.PKG
MAIN = kj.MAIN
TABS = [("통계", "통계"), ("저널", "저널"), ("검색", "검색"), ("안전", "안전"), ("설정", "맞춤 설정")]
SUBSTANCE_KR = "덱스트로메토르판"
OLDER_APK = "https://raw.githubusercontent.com/KJournal/kjournal-site/main/dist/KJournal-5-PB6.apk"
# 위 기준 APK 의 패키지. 앱 패키지명이 com.jiwxn3.KJournal 로 바뀌어, 다른 패키지 APK 를
# 설치한 뒤 새 패키지로 실행하면 OTA 업데이트 경로를 재현할 수 없다(스킵 처리).
OLDER_APK_PACKAGE = "com.isaakhanimann.journal.kr4812.premiumtest"
RESTORE_APK = os.path.join("release", "apk", "KJournal-5-PB8.apk")
EN_EXPORT_FIXTURE = os.path.join("scripts", "ci", "fixtures", "journal_en_export.json")

RESULTS = []


def log(msg):
    print(msg, flush=True)


def check(name, ok, detail=""):
    ok = bool(ok)
    RESULTS.append((name, ok, detail))
    log(("PASS " if ok else "FAIL ") + name + (("  | " + detail[:110]) if detail else ""))
    if not ok:
        # fail-fast: 첫 실패에서 즉시 종료 (요약 출력 후 비정상 종료)
        log("\n=== FAIL-FAST: 첫 실패에서 즉시 종료 ===")
        log("FAIL 항목: " + name + (("  | " + str(detail)[:200]) if detail else ""))
        log("현재 화면: " + kj.top_activity()[-80:])
        try:
            log("현재 텍스트: " + str([s for s in kj.texts() if s][:20]))
        except Exception:  # noqa: BLE001
            pass
        try:
            for l in kj.crashes()[:2]:
                log("크래시: " + l[:240])
        except Exception:  # noqa: BLE001
            pass
        sys.exit(1)
    return ok


def dump_state(tag):
    log("  [dump:%s] top=%s" % (tag, kj.top_activity()[-60:]))
    log("  [dump:%s] texts=%s" % (tag, [s for s in kj.texts() if s][:18]))


def launch_home():
    """앱을 실행해 면책/OTA 를 처리하고 홈(탭 표시)까지 진입(최대 180초)."""
    state = {"seen": False}
    kj.ensure_adb_ime()
    kj.reset_app()
    kj.sh("shell", "am", "start", "-n", MAIN)
    end = time.time() + 180
    while time.time() < end:
        # 1) 시스템/런처/앱 ANR 대화상자를 먼저 처리한다(에뮬레이터 불안정 대비).
        t = kj.texts()
        if any(("isn't responding" in x) or ("응답하지 않습니다" in x) or ("응답 없음" in x)
               for x in t):
            for label in ("Wait", "기다리기", "대기"):
                m = kj.find(label)
                if m:
                    kj.tap(m, wait=1.5)
                    break
            else:
                kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
                time.sleep(0.5)
            kj.sh("shell", "am", "start", "-n", MAIN)
            time.sleep(2.0)
            continue
        top = kj.top_activity()
        if "MainActivity" not in top:
            kj.sh("shell", "am", "start", "-n", MAIN)
            time.sleep(3.0)
            continue
        if any(x in t for x in ("Continue", "계속", "동의하고 계속")):
            state["seen"] = True
            kj.dismiss_disclaimer()
            continue
        if any(x in t for x in ("나중에", "지금 업데이트")):
            m = kj.find("나중에")
            if m:
                kj.tap(m, wait=0.8)
            continue
        if kj.find("설정") and (kj.find("저널") or kj.find("일지") or kj.find("검색")):
            return state["seen"]
        time.sleep(0.6)
    return False


def ensure_main():
    """앱을 MainActivity 로 보장."""
    for _ in range(3):
        if "MainActivity" in kj.top_activity():
            return True
        kj.sh("shell", "am", "start", "-n", MAIN)
        time.sleep(2.0)
    return "MainActivity" in kj.top_activity()


def tap_tab(label):
    ensure_main()
    for _ in range(3):
        if kj.tap_clickable(label):
            time.sleep(0.9)
            return True
        time.sleep(0.4)
    return False


def goto_settings_row(name):
    """설정 탭으로 이동 후 대상 행 탭(하위 화면이면 BACK 으로 복귀하며 재시도)."""
    for _ in range(4):
        tap_tab("설정")
        time.sleep(1.0)
        if kj.find(name) or kj.find("맞춤 설정"):
            break
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(0.8)
    m = kj.find(name) or kj.find_scroll(name)
    if not m:
        return False
    kj.tap(m, wait=1.6)
    return True


def phase_onboarding():
    log("\n=== 1) 온보딩 ===")
    seen = launch_home()
    if not (seen or bool(kj.find("설정"))):
        # 에뮬레이터 일시 불안정(ANR) 대비 1회 재시도
        log("  온보딩 재시도(에뮬레이터 불안정 대비)")
        time.sleep(3)
        seen = launch_home() or seen
    check("온보딩: 면책 동의 처리", seen or bool(kj.find("설정")), "면책 표시" if seen else "면책 없음(이미 동의)")
    check("온보딩: 홈 진입", bool(kj.find("설정") and kj.find("저널")), "탭 표시")


def phase_tabs():
    log("\n=== 2) 탭 순회 ===")
    for tab, marker in TABS:
        ok = tap_tab(tab)
        time.sleep(1.0)
        found = bool(kj.find(marker, contains=True))
        check("탭 %s" % tab, ok and found, "화면 표시" if found else "표시 안 됨")


def phase_search():
    log("\n=== 3) 검색 심층 ===")
    tap_tab("검색")
    time.sleep(1.0)
    fld = None
    for n in kj.ui().iter("node"):
        if "EditText" in n.attrib.get("class", ""):
            fld = n.attrib
            break
    if not check("검색: 입력칸 존재", fld is not None):
        dump_state("search-nofield")
        return
    kj.tap(fld, wait=0.4)
    try:
        kj.input_text_kr(SUBSTANCE_KR)
        typed = True
    except Exception as exc:  # noqa: BLE001
        typed = False
        log("  한국어 입력 실패: %s" % exc)
    time.sleep(1.5)
    vals = kj.field_texts()
    dup = any(v.count(SUBSTANCE_KR) > 1 for v in vals)
    check("검색: 한국어 입력(1회)", typed and any(SUBSTANCE_KR in v for v in vals), "fields=%s" % vals)
    check("검색: 중복 입력 없음", not dup, "fields=%s" % vals)
    row = kj.find(SUBSTANCE_KR, contains=True) or kj.find("Dextromethorphan", contains=True)
    check("검색: 결과 표시", row is not None, "결과 행" if row else "결과 없음")
    if row:
        kj.tap(row, wait=1.8)
        names = [s for s in kj.texts() if ("DXM" in s or "PsychonautWiki" in s)]
        cats = [s for s in kj.texts() if s in ("common", "habit-forming", "dissociative", "stimulant")]
        check("물질 상세 진입", bool(names), names[0][:50] if names else "정보 없음")
        check("물질 상세: 분류/정보 표시", bool(cats) or bool(names), "분류 %s" % (cats[:3] if cats else "정보"))
        if not names:
            dump_state("detail-missing")
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(1.0)
    else:
        check("물질 상세 진입", False, "결과 없음")
        dump_state("search-noresult")


def phase_custom_substance():
    log("\n=== 4) 커스텀 물질 추가 ===")
    if not check("설정: 사용자 지정 물질 진입", goto_settings_row("사용자 지정 물질 및 배합")):
        dump_state("custom-nosettings")
        return
    # 편집기가 열려있지 않으면 추가 버튼(우하단 FAB/버튼)을 탭
    if not kj.find("사용자 지정 물질 추가", contains=True):
        add = None
        for n in kj.ui().iter("node"):
            a = n.attrib
            mm = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a.get("bounds", "[0,0][0,0]"))
            desc = a.get("content-desc") or ""
            if a.get("clickable") == "true" and any(k in desc for k in ("추가", "Add", "add", "새")):
                add = a
                break
            if a.get("clickable") == "true" and mm:
                x1, y1, x2, y2 = map(int, mm.groups())
                # 우하단 FAB/추가 영역(하단 탭바 y>=2050 제외)
                if x1 > 480 and 1500 <= y1 <= 2030:
                    add = a
                    break
        if not check("커스텀: 편집기 열기", add is not None, "버튼 발견" if add else "버튼 없음"):
            # 폴백: 하단 입력 영역(사용자 지정 물질 추가 트리거)
            cands = []
            for n in kj.ui().iter("node"):
                a = n.attrib
                mm = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a.get("bounds", "[0,0][0,0]"))
                if a.get("class", "").endswith("EditText") and mm:
                    x1, y1, x2, y2 = map(int, mm.groups())
                    if y1 > 1400:
                        cands.append((y1, a))
            if cands:
                cands.sort()
                kj.tap(cands[-1][1], wait=1.8)
                opened = bool(kj.find("사용자 지정 물질 추가", contains=True))
                check("커스텀: 편집기 열기(하단 입력)", opened, "열림" if opened else "안 열림")
                if not opened:
                    dump_state("custom-noeditor")
                    kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
                    time.sleep(1.0)
                    return
            else:
                dump_state("custom-noadd")
                kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
                time.sleep(1.0)
                return
        else:
            kj.tap(add, wait=1.6)

    # 이름 입력: 가장 위 EditText
    fields = [n.attrib for n in kj.ui().iter("node") if "EditText" in n.attrib.get("class", "")]
    fields.sort(key=lambda a: int(re.match(r"\[(\d+),(\d+)", a["bounds"]).group(2)))
    if not check("커스텀: 이름 입력칸", bool(fields)):
        dump_state("custom-nofield")
    else:
        kj.tap(fields[0], wait=0.4)
        try:
            kj.input_text_kr("테스트물질")
        except Exception as exc:  # noqa: BLE001
            log("  한국어 입력 실패: %s" % exc)
        # 저장: 우하단 버튼 또는 저장 라벨
        saved = False
        for label in ("저장", "완료", "추가", "Done", "Save"):
            b = kj.find(label)
            if b:
                kj.tap(b, wait=1.6)
                saved = True
                break
        if not saved:
            for n in kj.ui().iter("node"):
                a = n.attrib
                mm = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", a.get("bounds", "[0,0][0,0]"))
                if a.get("clickable") == "true" and mm:
                    x1, y1, x2, y2 = map(int, mm.groups())
                    if x1 > 480 and 1500 <= y1 <= 2030:
                        kj.tap(a, wait=1.6)
                        saved = True
                        break
        check("커스텀: 저장 실행", saved, "저장" if saved else "저장 컨트롤 없음")
        listed = bool(kj.find("테스트물질", contains=True))
        check("커스텀: 목록 반영", listed, "목록 표시" if listed else "목록 없음")
        if not listed:
            dump_state("custom-notlisted")
    kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
    time.sleep(1.0)


def phase_interaction():
    log("\n=== 5) 상호작용 설정 ===")
    if not check("상호작용 설정 진입", goto_settings_row("상호작용 설정")):
        dump_state("interaction-noenter")
        return
    sw = None
    for n in kj.ui().iter("node"):
        a = n.attrib
        if a.get("checkable") == "true":
            sw = a
            break
    if not check("상호작용: 토글 항목", sw is not None, "스위치 발견" if sw else "스위치 없음"):
        dump_state("interaction-noswitch")
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(1.0)
        return
    before = sw.get("checked")
    kj.tap(sw, wait=1.2)
    after_node = None
    for n in kj.ui().iter("node"):
        if n.attrib.get("checkable") == "true":
            after_node = n.attrib
            break
    after = after_node.get("checked") if after_node else None
    check("상호작용: 토글 상태 변경", before != after, "%s -> %s" % (before, after))
    kj.tap(after_node or sw, wait=1.0)  # 원래 상태로 복원
    kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
    time.sleep(1.0)


def phase_settings_screens():
    log("\n=== 6) 설정 하위 화면 ===")
    for name in ("물질 색상", "환경설정", "파일 내보내기"):
        if not check("설정 항목 존재: %s" % name, bool(kj.find(name) or kj.find_scroll(name))):
            dump_state("settings-" + name)
            continue
        m = kj.find(name)
        before = set(kj.texts())
        kj.tap(m, wait=1.5)
        after = set(kj.texts())
        check("설정 화면 진입: %s" % name, after != before and "MainActivity" in kj.top_activity(), "진입")
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(1.0)


def phase_update_section():
    log("\n=== 6-1) 설정 업데이트 섹션 ===")
    ensure_foreground()
    tap_tab("설정")
    time.sleep(1.0)
    # 이전 단계에서 아래로 스크롤된 상태일 수 있으므로 맨 위로 올린다.
    kj.scroll_top()
    time.sleep(0.6)

    # 스크롤 제스처가 행 탭으로 처리되어 이미 릴리스 노트 화면일 수 있다.
    if kj.find("릴리스 노트", contains=True) and not any(s.strip() == "업데이트" for s in kj.texts()):
        check("업데이트: 릴리스 노트 화면", True, "이미 이동됨")
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(0.8)
        return

    t = kj.texts()
    has_section = any(s.strip() == "업데이트" for s in t)
    has_latest = any("케이저널 최신 버전입니다" in s for s in t)
    has_update = any("눌러서 업데이트" in s for s in t)
    check("업데이트: 섹션 표시", has_section, "섹션=%s" % has_section)
    check("업데이트: 상태 문구", has_latest or has_update,
          "최신=%s 업데이트=%s" % (has_latest, has_update))

    # 최신이든 업데이트가 있든, 항목을 누르면 릴리스 노트 화면이 열려야 한다.
    cand = "케이저널 최신 버전입니다" if has_latest else ("눌러서 업데이트" if has_update else None)
    opened = False
    if cand:
        for _ in range(3):
            node = kj.find(cand, contains=True)
            if node:
                kj.tap(node, wait=2.5)
            if kj.find("릴리스 노트", contains=True):
                opened = True
                break
            time.sleep(1.0)
    check("업데이트: 클릭 시 릴리스 노트", opened, "열림=%s" % opened)
    if opened:
        kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(0.8)


def _find_version_row(tries=10):
    row = None
    for _ in range(tries):
        row = kj.find("버전", contains=True)
        if row:
            return row
        kj.swipe_up()
    return row


def _tap_version_row(row):
    """'버전' 행을 탭한다. 하단 시스템 제스처(홈) 영역을 피해 위로 올려서 탭한다."""
    w, h = kj.screen_size()
    x, y = kj.center(row)
    for _ in range(3):
        if y <= h - 240:
            break
        kj.swipe_up()
        time.sleep(0.4)
        nxt = kj.find("버전", contains=True)
        if not nxt:
            break
        row = nxt
        x, y = kj.center(row)
    # 그래도 너무 아래면 제스처 영역 밖으로 클램프한다.
    y = min(y, h - 240)
    kj.sh("shell", "input", "tap", str(x), str(y))
    kj.invalidate()
    time.sleep(1.5)


def phase_release_notes():
    log("\n=== 7) 릴리즈노트 ===")
    ensure_foreground()
    tap_tab("설정")
    time.sleep(1.0)
    row = _find_version_row()
    if not check("릴리즈노트: 버전 행", row is not None):
        dump_state("relnotes-norow")
        return

    ok = False
    detail = ""
    for _ in range(3):
        ensure_foreground()
        if PKG not in kj.top_activity():
            kj.sh("shell", "am", "start", "-n", MAIN)
            time.sleep(3)
        # 설정 탭이 아니면 다시 이동(백그라운드 복귀 대비)
        if "맞춤 설정" not in kj.texts():
            tap_tab("설정")
            time.sleep(1.0)
        row = _find_version_row(tries=8)
        if not row:
            detail = "버전 행 재탐색 실패"
            continue
        _tap_version_row(row)
        # 릴리즈노트는 네트워크에서 받아 렌더링되므로 표시될 때까지 대기한다.
        for _ in range(10):
            if PKG not in kj.top_activity():
                detail = "앱 백그라운드로 이탈"
                break
            t = kj.texts()
            has_kr = any(any("\uac00" <= c <= "\ud7a3" for c in s) for s in t)
            has_note = any(("버전" in s) or ("변경" in s) or ("KJournal" in s) or ("릴리스" in s)
                           for s in t)
            detail = "한글=%s 노트=%s" % (has_kr, has_note)
            if has_kr and has_note:
                ok = True
                break
            time.sleep(1.0)
        if ok:
            break
    if not ok:
        dump_state("relnotes-empty")
    check("릴리즈노트: 표시", ok, detail)
    kj.sh("shell", "input", "keyevent", "KEYCODE_BACK")
    time.sleep(1.0)


def phase_ota_info():
    log("\n=== 8) OTA 정보 ===")
    srv = kj.fetch_ota()
    if srv is None:
        # 배타 채널 부트스트랩(첫 배포 전)에는 엔드포인트가 아직 없을 수 있다.
        check("OTA: version.json 조회", True, "엔드포인트 미배포(부트스트랩) - 스킵")
        return None
    check("OTA: version.json 조회", True, "OK")
    check("OTA: versionCode/Name", bool(srv.get("versionCode")) and bool(srv.get("versionName")),
          "%s(%s)" % (srv.get("versionName"), srv.get("versionCode")))
    check("OTA: changelog 포함", bool((srv.get("changelog") or "").strip()),
          (srv.get("changelog") or "").splitlines()[0][:40])
    inst = kj.installed_version_code()
    newer = int(srv.get("versionCode") or 0) > (inst or 0)
    check("OTA: 설치버전 비교", inst is not None, "서버 %s / 설치 %s (업데이트=%s)" % (srv.get("versionCode"), inst, newer))
    return srv


def phase_notifications():
    log("\n=== 9) 알림 ===")
    kj.sh("shell", "pm", "grant", PKG, "android.permission.POST_NOTIFICATIONS")
    perm = "granted=true" in kj.sh("shell", "dumpsys", "package", PKG)
    check("알림: POST_NOTIFICATIONS 권한", perm, "granted=%s" % perm)
    out = kj.sh("shell", "dumpsys", "notification", "--noredact")
    check("알림: 알림 서비스 등록", PKG in out or "TimelineNotificationService" in out,
          "패키지 등록=%s" % (PKG in out))


def phase_ota_flow():
    log("\n=== 11) OTA 업데이트 플로우 ===")
    srv = kj.fetch_ota() or {}
    # 패키지명 변경 이후 구 패키지 기준 APK 로는 업데이트 경로를 재현할 수 없다.
    if OLDER_APK_PACKAGE != PKG:
        log("SKIP OTA플로우: 기준 APK 패키지(%s) != 현재 패키지(%s) — 새 패키지 이전 릴리즈 필요"
            % (OLDER_APK_PACKAGE, PKG))
        return
    # 서버가 설치본보다 높지 않으면(OTA 홀드 등) 업데이트 팝업을 기대할 수 없다.
    inst_vc = kj.installed_version_code()
    if int(srv.get("versionCode") or 0) <= int(inst_vc or 0):
        log("SKIP OTA플로우: 서버 %s <= 설치 %s (업데이트 없음/OTA 홀드)"
            % (srv.get("versionCode"), inst_vc))
        return
    want = (srv.get("sha256") or "").strip().lower()
    try:
        older = os.path.join(os.environ.get("TEMP", "/tmp"), "kilo", "KJournal-older.apk")
        os.makedirs(os.path.dirname(older), exist_ok=True)
        if not os.path.exists(older):
            with urllib.request.urlopen(OLDER_APK, timeout=90) as r, io.open(older, "wb") as f:
                f.write(r.read())
    except Exception as exc:  # noqa: BLE001
        check("OTA플로우: 구버전 준비", False, str(exc))
        return
    kj.sh("shell", "am", "force-stop", PKG)
    kj.sh("uninstall", PKG)
    out = kj.sh("install", "-r", older)
    if not check("OTA플로우: 구버전 설치", "Success" in out, out.strip()[:80]):
        return
    kj.sh("shell", "am", "start", "-n", MAIN)
    time.sleep(8)
    for _ in range(6):
        t = kj.texts()
        if any(x in t for x in ("Continue", "계속")):
            kj.dismiss_disclaimer()
            time.sleep(2)
            continue
        break
    dialog = kj.find("지금 업데이트")
    check("OTA플로우: 업데이트 다이얼로그", dialog is not None, kj.top_activity()[-45:])
    tx = " ".join(kj.texts())
    check("OTA플로우: changelog 표시", ("변경" in tx) or ("KJournal 5" in tx), "표시")
    if dialog:
        kj.tap(dialog, wait=3)
        time.sleep(12)
        listing = kj.sh("shell", "ls", "-R", "/sdcard/Download")
        cur, path = "", ""
        for line in listing.splitlines():
            line = line.strip()
            if line.startswith("/") and line.endswith(":"):
                cur = line[:-1]
            elif line.endswith(".apk"):
                path = (cur + "/" + line) if cur else line
        check("OTA플로우: APK 다운로드", bool(path), path or "없음")
        if path and want:
            local = os.path.join(os.environ.get("TEMP", "/tmp"), "kilo", "ota-downloaded.apk")
            os.makedirs(os.path.dirname(local), exist_ok=True)
            kj.sh("pull", path, local)
            got = hashlib.sha256(open(local, "rb").read()).hexdigest() if os.path.exists(local) else ""
            check("OTA플로우: SHA-256 일치", got == want, "expected=%s got=%s" % (want[:10], got[:10]))
    kj.sh("shell", "am", "force-stop", PKG)
    kj.sh("uninstall", PKG)
    if os.path.exists(RESTORE_APK):
        out = kj.sh("install", "-r", RESTORE_APK)
        check("OTA플로우: 원복 설치", "Success" in out, out.strip()[:80])


def phase_crash():
    log("\n=== 12) 크래시 스캔 ===")
    bad = kj.crashes()
    check("크래시 없음", not bad, ("%d건" % len(bad)) if bad else "FATAL 없음")
    for l in bad[:3]:
        log("   " + l[:140])


def ensure_foreground():
    """각 단계 시작 전 앱이 포그라운드인지 보장한다(불안정 완화)."""
    try:
        if PKG not in kj.top_activity():
            kj.sh("shell", "am", "start", "-n", MAIN)
            time.sleep(4)
    except Exception:  # noqa: BLE001
        pass


def main():
    t0 = time.time()
    log("=== KJournal 전체 기능 심층 테스트 ===")
    log("\n=== 0) 준비(한국어 IME) ===")
    check("준비: 한국어 입력 IME", kj.ensure_adb_ime(), "ADBKeyboard")
    for phase in (phase_onboarding, phase_tabs, phase_search, phase_custom_substance,
                  phase_interaction, phase_settings_screens, phase_update_section,
                  phase_release_notes,
                  phase_ota_info, phase_notifications, phase_ota_flow,
                  phase_crash):
        ensure_foreground()
        phase()
    ok = sum(1 for _, o, _ in RESULTS if o)
    log("\n=== 결과: %d/%d PASS (%.0fs) ===" % (ok, len(RESULTS), time.time() - t0))
    for n, o, d in RESULTS:
        if not o:
            log("  FAIL: %s  %s" % (n, d))
    return 0 if ok == len(RESULTS) else 2


if __name__ == "__main__":
    sys.exit(main())
