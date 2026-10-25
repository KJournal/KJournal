# Android 16 알림 활성화 크래시

## 증상
Android 11에서는 정상이나 Android 16에서 알림을 켜거나 섭취를 추가할 때 앱이 종료됨.

## 원인 1 — 포그라운드 서비스 타입 불일치 (Android 14+)
`TimelineNotificationService`가 `startForeground(id, notification, FOREGROUND_SERVICE_TYPE_SPECIAL_USE=0x40000000)`(헬퍼 `fs.q`)을 호출하지만, 매니페스트는 `foregroundServiceType="dataSync"`(0x1)로 선언돼 있어
`IllegalArgumentException: foregroundServiceType 0x40000000 is not a subset of foregroundServiceType attribute 0x00000001` 로 크래시.

## 원인 2 — `Paint.getTextBounds()` 범위 오류 (Android 16)
`Paint.getTextBounds()`에 문자열 `지금`의 길이보다 큰 종료 인덱스가 전달됨. Android 16의 범위 검사가 엄격해져 `IndexOutOfBoundsException` 발생.

## 해결
- `fs.q`의 포그라운드 서비스 타입을 `dataSync`(0x1)로 수정.
- `au.smali`의 `지금` 종료 인덱스를 문자열 길이인 2로 수정.
- `FOREGROUND_SERVICE_DATA_SYNC` 권한을 선언.
