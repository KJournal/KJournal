# -*- coding: utf-8 -*-
"""OTA 업데이트 플로우 테스트.

서버(GitHub Pages) 최신 버전 > 설치 버전 상황을 만들어 업데이트 다이얼로그와
'지금 업데이트' 다운로드(OtaUpdater) 동작을 실제로 검증한다.

순서
1) GH Pages version.json 조회
2) 현재 설치본 제거 후, 서버보다 낮은 버전의 APK(기본: PB6 5016) 설치
3) 앱 실행 → 업데이트 다이얼로그('지금 업데이트') + changelog 노출 확인
4) '지금 업데이트' 탭 → 다운로드 진행(Download/KJournalUpdates 또는 알림) 확인
5) 원래 빌드(release/apk/KJournal-5-PB8.apk) 로 원복 설치

사용: python scripts/ota_test.py [--older <apk path or url>]
"""
import importlib.util
import io
import os
import sys
import time
import urllib.request

_spec = importlib.util.spec_from_file_location(
    "tt", os.path.join(os.path.dirname(os.path.abspath(__file__)), "adb_helpers.py"))
tt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tt)

DEFAULT_OLDER = "https://raw.githubusercontent.com/KJournal/kjournal-site/main/dist/KJournal-5-PB6.apk"
RESTORE = os.path.join("release", "apk", "KJournal-5-PB8.apk")


def fetch_url(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with urllib.request.urlopen(url, timeout=60) as r, io.open(dest, "wb") as f:
        f.write(r.read())
    return dest


def main():
    t0 = time.time()
    older = DEFAULT_OLDER
    if "--older" in sys.argv:
        older = sys.argv[sys.argv.index("--older") + 1]
    local_older = os.path.join(os.environ.get("TEMP", "/tmp"), "kilo", "KJournal-older.apk")
    os.makedirs(os.path.dirname(local_older), exist_ok=True)

    print("=== OTA 업데이트 플로우 테스트 ===", flush=True)
    srv = tt.fetch_ota()
    if not srv:
        print("FAIL OTA version.json 조회", flush=True)
        return 1
    print("서버: %s(%s)" % (srv.get("versionName"), srv.get("versionCode")), flush=True)
    print("changelog 길이: %d" % len((srv.get("changelog") or "")), flush=True)

    try:
        if older.startswith("http"):
            fetch_url(older, local_older)
        else:
            local_older = older
        print("구버전 APK 준비: %s (%d bytes)" % (local_older, os.path.getsize(local_older)), flush=True)
    except Exception as exc:  # noqa: BLE001
        print("SKIP 구버전 APK 준비 실패:", exc, flush=True)
        return 0

    tt.sh("shell", "am", "force-stop", tt.PKG)
    tt.sh("uninstall", tt.PKG)
    out = tt.sh("install", "-r", local_older)
    if "Success" not in out:
        print("SKIP 구버전 설치 실패:", out.strip()[:120], flush=True)
        return 0
    print("구버전 설치 완료", flush=True)

    tt.sh("shell", "am", "start", "-n", tt.MAIN)
    time.sleep(8)
    for _ in range(6):
        t = tt.texts()
        if any(x in t for x in ("Continue", "계속")):
            tt.dismiss_disclaimer()
            time.sleep(2)
            continue
        break
    dialog = tt.find("지금 업데이트") or tt.find("나중에")
    tx = [s for s in tt.texts() if s]
    has_cl = any(("변경" in s) or ("캘린더" in s) or ("KJournal 5" in s) for s in tx)
    print(("PASS" if dialog else "FAIL") + " 업데이트 다이얼로그 노출", flush=True)
    print(("PASS" if has_cl else "FAIL") + " 다이얼로그 changelog 표시", flush=True)

    if dialog:
        upd = tt.find("지금 업데이트")
        if upd:
            tt.tap(upd, wait=3)
            time.sleep(12)
            out = tt.sh("shell", "ls", "-R", "/sdcard/Download")
            got = "KJournal" in out and ".apk" in out
            print(("PASS" if got else "FAIL") + " 업데이트 다운로드", flush=True)
            print("   Download:", " ".join(out.split())[:160], flush=True)
            # SHA-256 검증: version.json 의 sha256 과 다운로드 APK 해시 비교
            want = (srv.get("sha256") or "").strip().lower()
            if want:
                cur = ""
                path = ""
                for line in out.splitlines():
                    line = line.strip()
                    if line.startswith("/") and line.endswith(":"):
                        cur = line[:-1]
                    elif line.endswith(".apk"):
                        path = (cur + "/" + line) if cur else line
                if path:
                    try:
                        import hashlib
                        local = os.path.join(os.environ.get("TEMP", "/tmp"), "kilo", "ota-downloaded.apk")
                        os.makedirs(os.path.dirname(local), exist_ok=True)
                        tt.sh("pull", path, local)
                        got_hash = hashlib.sha256(open(local, "rb").read()).hexdigest()
                    except Exception as exc:  # noqa: BLE001
                        got_hash = ""
                        print("SHA-256 계산 실패:", exc, flush=True)
                    if got_hash:
                        print(("PASS" if got_hash == want else "FAIL") + " SHA-256 일치",
                              "expected=%s got=%s" % (want[:12], got_hash[:12]), flush=True)
                    else:
                        print("SKIP SHA-256 검증(계산 불가)", flush=True)
                else:
                    print("SKIP SHA-256 검증(APK 경로 미확인)", flush=True)

    # 원복
    tt.sh("shell", "am", "force-stop", tt.PKG)
    tt.sh("uninstall", tt.PKG)
    if os.path.exists(RESTORE):
        out = tt.sh("install", "-r", RESTORE)
        print(("PASS" if "Success" in out else "FAIL") + " 원래 빌드 원복", flush=True)
    print("\n=== OTA 테스트 종료 (%.0fs) ===" % (time.time() - t0), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
