# -*- coding: utf-8 -*-
"""버전 표기 일관성 검증(이슈 #9): apktool.yml ↔ 앱 타이틀 ↔ release 메타데이터.

사용: python scripts/ci/verify_version.py
"""
import io
import json
import os
import re
import sys

SRC = r"reverse-engineering/kjournal-157-decoded"
APKTOOL = os.path.join(SRC, "apktool.yml")
IW0 = os.path.join(SRC, "smali", "iw0.smali")
TITLE_SMALI = os.path.join(SRC, "smali", "iw0.smali")


def esc(s):
    return ''.join(ch if ord(ch) < 128 else '\\u%04x' % ord(ch) for ch in s)


def main():
    t = io.open(APKTOOL, encoding='utf-8').read()
    vc = re.search(r"^  versionCode: *(\d+)", t, re.M).group(1)
    vn = re.search(r"^  versionName: *(.+)$", t, re.M).group(1).strip()
    label = vn.replace(' ', '-')
    problems = []
    print("apktool.yml: versionCode=%s versionName=%s label=%s" % (vc, vn, label))

    # 1) 앱 타이틀 문자열 일치 (정식 `KJournal <versionName>` 또는 메이저 표기 `KJournal <major>` 허용)
    smali = io.open(TITLE_SMALI, encoding='utf-8', errors='ignore').read()
    want = "KJournal " + vn
    major = "KJournal " + vn.split('.')[0].strip()
    if ('"%s"' % esc(want)) in smali:
        print("앱 타이틀 일치: %s" % want)
    elif major != want and ('"%s"' % esc(major)) in smali:
        print("앱 타이틀 일치: %s (메이저 표기)" % major)
    else:
        problems.append("앱 타이틀 문자열 없음: %s (또는 %s)" % (want, major))

    # 2) release 메타데이터 일치
    vjson = os.path.join("release", "KJournal-%s-version.json" % label)
    if os.path.exists(vjson):
        meta = json.load(io.open(vjson, encoding='utf-8'))
        if str(meta.get("versionCode")) != vc:
            problems.append("release versionCode 불일치: %s != %s" % (meta.get("versionCode"), vc))
        if meta.get("versionName") != vn:
            problems.append("release versionName 불일치: %s != %s" % (meta.get("versionName"), vn))
        print("release 메타데이터 확인: %s" % vjson)
    else:
        problems.append("release 메타데이터 없음: %s" % vjson)

    # 3) 알림(FGS) 선언 확인 — 이슈 #9: 포크와 동일한 dataSync 타입
    man = io.open(os.path.join(SRC, "AndroidManifest.xml"), encoding="utf-8", errors="ignore").read()
    if 'android:name="com.isaakhanimann.journal.ui.tabs.journal.experience.timeline.notification.TimelineNotificationService"' not in man:
        problems.append("TimelineNotificationService 선언 없음")
    elif 'android:foregroundServiceType="dataSync"' not in man:
        problems.append("TimelineNotificationService foregroundServiceType != dataSync")
    if "android.permission.FOREGROUND_SERVICE_DATA_SYNC" not in man:
        problems.append("FOREGROUND_SERVICE_DATA_SYNC 권한 없음")
    if "android.permission.POST_NOTIFICATIONS" not in man:
        problems.append("POST_NOTIFICATIONS 권한 없음")
    if not problems:
        print("알림(FGS dataSync/POST_NOTIFICATIONS) 선언 확인")

    # 4) APK 산출물 확인.
    #    CI는 워크플로 안에서 APK를 직접 빌드하므로 build/out 을 먼저 본다.
    #    release/apk 는 기록용이므로 로컬에서 미리 빌드해 커밋할 필요가 없다.
    #    (APK 자체의 필수 검증은 verify_apk.py 가 담당한다.)
    apk_candidates = [
        os.path.join("build", "out", "KJournal-%s.apk" % label),
        os.path.join("build", "out", "KJournal-%s-beta.apk" % label),
        os.path.join("release", "apk", "KJournal-%s.apk" % label),
    ]
    apk = next((p for p in apk_candidates if os.path.exists(p)), None)
    if apk:
        print("APK: %s" % apk)
    else:
        print("APK 산출물 미확인(빌드 전 단계), 검증 대상 아님: %s" % apk_candidates[0])

    if problems:
        print("버전 표기 검증 실패:", file=sys.stderr)
        for p in problems:
            print(" -", p, file=sys.stderr)
        return 1
    print("버전 표기 검증 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
