# OTA 다운로드 후 설치 흐름

## 증상
삼성 기기에서 앱 내부 자동 설치가 악성 앱 또는 설치 차단으로 거부됨.

## 해결 방향
HTTPS/NAS version.json, SHA-256 검증, 공용 Download 저장, Android 공식 Package Installer 인텐트를 사용하도록 OTA 흐름을 분리함. 삼성 보안 정책 자체를 우회하지 않고 사용자가 공식 설치 화면에서 승인하도록 함.
