# 저장소 보존·브랜치 감사 기록

감사 기준일: 2026-09-22 (KST)

## 원격 저장소

- 저장소: `exaqueGithb/kjournal-android`
- 원격 URL: `https://github.com/exaqueGithb/kjournal-android`
- 기본 브랜치: `main`
- 클론 직후 상태: `main...origin/main`, 작업 트리 clean

## 브랜치 현황

클론된 refs에서 로컬 `main`과 원격 `origin/main`만 확인되었다. 별도 feature 브랜치, 미병합 브랜치 또는 충돌 상태는 확인되지 않았다. 기존 이력은 커밋으로 보존되어 있으며, 이번 변경도 새 커밋으로 `main`에 추가한다.

## 기존 보존 자료

저장소에는 다음 자료가 이미 포함되어 있다.

- 원본 및 단계별 APK
- 전체 apktool 역공학 결과
- OTA 구현 소스와 Android 16 알림 안정화 패치
- 단계별 빌드·패치 스크립트
- APK 카탈로그와 SHA-256
- 문제별 문서 001~005
- 비밀정보를 제거한 전체 대화 기록

## 이번 추가 자료

- `release/apk/PsyLog_Korean_Patched_v1.apk`
- `release/apk/PsyLog_Korean_Patched_v2.apk`
- `docs/SESSION_2026-09-22_KOREAN_PATCH.md`
- 이 감사 문서
- `release/APK_CATALOG.md`의 두 APK 항목

모든 추가는 additive 방식으로 수행한다. 기존 파일을 삭제하거나 덮어쓰지 않는다.

## 민감정보 처리

GitHub 토큰, NAS 비밀번호, 서명키, 환경변수 값은 문서와 커밋에 포함하지 않는다. 기존 대화 기록의 비밀정보 제거 원칙도 그대로 유지한다.

## 커밋 전 확인 명령

```bash
git status --short --branch
git branch -a
git log --oneline --decorate --all -20
sha256sum release/apk/PsyLog_Korean_Patched_v*.apk
```
