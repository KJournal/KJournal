# 재현 가능한 APK 빌드

## 목표
디코드된 apktool 프로젝트에서 누구나 같은 구조의 unsigned APK를 만들 수 있도록 함.

## 상태
`build/build.sh`가 Apktool 3.0.3으로 실제 APK 생성까지 검증됨. 서명은 개인 키를 저장소에 넣지 않고 `KEYSTORE` 환경변수로 주입함.
