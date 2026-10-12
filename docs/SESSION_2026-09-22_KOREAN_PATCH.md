# 2026-09-22 한국어 패치 세션 기록

## 목적

PsyLog/KJournal Android APK의 사용자에게 표시되는 UI를 한국어로 현지화하고, `assets/Substances.json`은 변경하지 않는 범위에서 설치 가능한 APK를 보존하는 작업이다. 앱 표시 이름은 **KJournal V1.2**, 개발자 표기는 **지원(정병이) 개발**로 정리했으며 Discord와 X 핸들은 유지했다.

## 작업 범위

- 홈 화면, 하단 탭, 설정, 통계, 저널/약물 기록 화면
- 약물 추가·조회 화면과 섭취 경로 선택 화면
- 검색, 저장, 취소, 확인, 편집 등 사용자 조작 문구
- 시작 시 경고·면책 문구
- 내보내기·가져오기, FAQ, 후원 등 설정 부속 화면
- Compose 화면에 남은 하드코딩 사용자 문구

`assets/Substances.json`의 약물 데이터와 개발자용 문자열·로그·예외 메시지·코드 내부 상수는 번역 대상에서 제외했다.

## 주요 수정 위치

- `res/values-ko/strings.xml`: 기본 한국어 리소스
- `smali/j4/a.smali`: 저널·경험 기록 화면
- `smali/K4/a.smali`: 설정, 데이터 관리, 내보내기·가져오기
- `smali/T3/h.smali`: 하단 탭 이름
- `smali/B4/p.smali`: 버전 정보와 개발자 표시
- `smali/O4/g.smali`: 단위와 메모 관련 화면

## 빌드 및 보존

이전 작업에서 apktool로 디코드한 뒤 재빌드하고 `uber-apk-signer`로 서명하는 흐름을 확인했다. 현재 저장소에는 전체 디코드 결과와 재현용 빌드 도구가 `reverse-engineering/`, `build/`, `scripts/` 아래 보존되어 있다. 이번 세션에서 복원된 최종 후보 APK도 `release/apk/`에 원본 파일명 그대로 추가했다.

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| `release/apk/PsyLog_Korean_Patched_v1.apk` | 4,377,646 bytes | `ec913542f801a0fbbd10780681e82630b8663fff77cbc929a8d60fb6cddf75e1` |
| `release/apk/PsyLog_Korean_Patched_v2.apk` | 4,501,274 bytes | `ce557981299261f2075144019e4ce26d04c6a1dcfad3ecace8729ef1c7a90dce` |

## 기존 작업 이력과 이슈

기존 커밋과 문서에는 원본 APK 보존, 단계별 OTA 빌드, Android 16 알림 크래시 수정, 재현 가능한 빌드, 전체 역공학 소스, 한국어 잔여 문구 이슈가 시간순으로 기록되어 있다.

- `docs/issues/001-android16-notification-crash.md`
- `docs/issues/002-ota-install-flow.md`
- `docs/issues/003-korean-localization.md`
- `docs/issues/004-reproducible-build.md`
- `docs/issues/005-release-history.md`
- `docs/CHAT_HISTORY_REDACTED.md`
- `docs/RELEASE_HISTORY.md`

인증 토큰, 비밀번호, 서명 개인키와 같은 비밀정보는 저장하지 않았다. 대화 기록은 이미 비밀정보 제거본으로 보존되어 있다.

## 현재 상태

- 기본 브랜치: `main`
- 원격: `https://github.com/exaqueGithb/kjournal-android`
- 클론 시점 기준 원격 브랜치: `origin/main`만 확인됨
- 별도 미병합 브랜치나 삭제 대상 파일은 확인되지 않음
- 기존 자료는 삭제하지 않고 이번 산출물과 문서만 추가함

## 남은 검증 한계

이 세션의 복원 환경에는 이전 디컴파일 작업 디렉터리의 별도 임시 로그가 모두 남아 있지는 않았다. 대신 저장소에 이미 보존된 전체 역공학 결과, 빌드 스크립트, 이슈 문서, 비밀정보 제거 대화 기록과 이번 APK의 SHA-256을 함께 커밋한다. 실제 기기에서의 모든 화면·입력 경로 검증은 설치 후 별도 수행해야 한다.
