#!/usr/bin/env python3
"""APK 정적 검증 (에뮬레이터 불필요, CI 필수 게이트).

빌드된 APK 안에 이번 릴리즈의 핵심 요소가 실제로 들어있는지 확인한다.
- OTA(OtaUpdater) 클래스
- 저장 대화상자 문구("파일을 저장했습니다.")
- 한국어 Substances.json
- 프리미엄 해제 패치(문자열 "premium" 존재)

사용: python3 scripts/ci/verify_apk.py build/out/KJournal-5-PB8.apk
"""
import io
import sys
import zipfile

REQUIRED_CLASSES = [
    b"Lcom/isaakhanimann/journal/ota/OtaUpdater;",
    b"Lcom/isaakhanimann/journal/ota/PublicFileStore;",
]
REQUIRED_STRINGS = [
    "파일을 저장했습니다.".encode("utf-8"),
    "premium".encode("utf-8"),
]
KOREAN_ASSET_MARKERS = ["실로시빈", "사이키델릭"]


def main():
    if len(sys.argv) < 2:
        print("usage: verify_apk.py <apk>", file=sys.stderr)
        return 2
    apk = sys.argv[1]
    with zipfile.ZipFile(apk) as z:
        names = z.namelist()
        dex = b"".join(z.read(n) for n in names if n.endswith(".dex"))
        manifest = z.read("AndroidManifest.xml") if "AndroidManifest.xml" in names else b""
        asset_names = [n for n in names if n.endswith("Substances.json")]
        asset = z.read(asset_names[0]).decode("utf-8", "ignore") if asset_names else ""

    def in_manifest(token):
        return token.encode("utf-8") in manifest or token.encode("utf-16-le") in manifest

    failures = []
    for cls in REQUIRED_CLASSES:
        if cls not in dex:
            failures.append("missing class: %s" % cls.decode())
    for s in REQUIRED_STRINGS:
        if s not in dex:
            failures.append("missing string: %s" % s.decode("utf-8", "replace"))
    # 알림 안정성(이슈 #9): 권한 선언 확인(값은 이진 매니페스트에 UTF-16LE 로 저장됨)
    for token in ("POST_NOTIFICATIONS", "FOREGROUND_SERVICE_DATA_SYNC"):
        if not in_manifest(token):
            failures.append("manifest missing: %s" % token)
    if not asset:
        failures.append("assets/Substances.json not found")
    else:
        for m in KOREAN_ASSET_MARKERS:
            if m not in asset:
                failures.append("Substances.json missing Korean marker: %s" % m)

    if failures:
        print("APK 정적 검증 실패:", file=sys.stderr)
        for f in failures:
            print(" -", f, file=sys.stderr)
        return 1

    print("APK 정적 검증 통과: %s" % apk)
    print("  dex 크기: %d bytes / assets/Substances.json: %d bytes" % (len(dex), len(asset)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
