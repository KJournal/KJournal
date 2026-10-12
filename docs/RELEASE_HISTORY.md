# KJournal 4.8 이후 전체 변경 로그

## 4.8~4.9: 원본 분석과 OTA 기반 마련

KJournal 4.8 계열에서 프리미엄 entitlement 확인 위치를 조사하고, 기존 APK의 패키지·서명·기능을 보존하는 것을 기준으로 작업을 시작했다. 이후 KJournal 4.9 계열에 NAS `version.json` 조회, 비동기 APK 다운로드, SHA-256 검증, Android 설치 인텐트, 커스텀 `OtaFileProvider`를 추가했다. AndroidX FileProvider 누락으로 실행 직후 발생하던 크래시도 자체 Provider로 대체했다.

## 5 DP1~DP4: 브랜딩·번역·설치 흐름

앱 표시 이름을 KJournal로 통일하고, 개발자·기여자 표시, 영어 잔여 문구, ingestion·Today·Now·ago·peak·equivalent·Stop 등 화면 문구를 단계별로 한국어화했다. 삼성 기기에서 OTA 자동 설치가 차단되는 경우를 고려해 공용 다운로드 폴더와 공식 Package Installer를 이용하는 흐름으로 변경했다.

## 5 PB1~PB5: 공개 베타와 OTA 안정화

PB1부터 PB5까지 OTA 안내 UI, APK 파일명, NAS 공개 링크, `version.json`을 갱신했다. 다운로드 실패·잘못된 JSON·네트워크 오류는 앱을 종료시키지 않도록 예외 처리했다. 알림 타임라인의 시작·중지 토글과 한국어 표시를 보정했다.

## 5 PB6: 알림 및 Android 16 수정

Android 12 이상에서 포그라운드 서비스 권한과 시작 조건을 보정했다. Android 16에서 `Paint.getTextBounds()`가 문자열 길이보다 큰 종료 인덱스를 거부해 발생한 `IndexOutOfBoundsException`을 수정했다. `FOREGROUND_SERVICE_DATA_SYNC` 권한을 추가하고 모든 해상도에서 버전 표기를 PB6로 통일했다.

## 보존 자료

각 단계의 빌드 스크립트는 `scripts/build-history/`, 역공학 전체 결과는 `reverse-engineering/kjournal-pb6-decoded/`, 재빌드 명령은 `build/`, APK와 SHA-256 목록은 `release/`에 있다.

## 5 PB8.3~PB8.6: 한글화 심화 및 OTA 설치 안정화

- **5 PB8.3 (5027)**: 미번역 UI 한글화(물질 상세·상대시간 표기·릴리즈 노트), OTA 다운로드 파일명 수정.
- **5 PB8.4 (5028)**: 5027 사용자 OTA 복구, 삼성에서 설치 화면이 자동으로 열리지 않던 경우 완화(출처 허용 안내), 다운로드 파일명 보정.
- **5 PB8.5 (5029)**: OTA 다운로드 파일명을 URL에서 자동 도출, 설치 안내 문구를 실제 파일명으로 동적 표시.
- **5 PB8.6 (5030)**: KA-17·KA-18.
  - `OtaFileProvider`에 `FILE_PROVIDER_PATHS`(res/xml/ota_paths) meta-data 누락 → 설치 화면(Package Installer)이 APK를 읽지 못하던 문제 수정.
  - 설치 화면이 열린 경우에도 '내 파일' 안내가 위로 덮던 조건 반전(`if-eqz`→`if-nez`) 수정.
  - 설치 안내가 다운로드 스레드에서 `Toast.show()`를 호출해 `NullPointerException`(오탐 '네트워크 확인' + 파일 삭제)이 나던 문제 제거.
  - `Handler;->post(Landroid/os/Runnable;)` 오타 → `Ljava/lang/Runnable;` 수정.
  - 다운로드 요청에 `Connection: close` + 실패 시 최대 2회 재시도.
  - 통계 카드('일부 타임라인이 불완전합니다…')와 타임라인 정보 화면(단순화/잘못된 가정, 지속시간 정의 등)의 잔여 영어를 PB6 포크 문구로 번역.
  - PB6 포크도 영어로 둔 항목(`of peak`, `equivalent`, `active`, `Info`)은 임의 번역 금지 원칙에 따라 유지.
