# KJournal 빌드

`build/build.sh`는 `reverse-engineering/kjournal-pb6-decoded/`의 apktool 프로젝트를 APK로 빌드합니다.

```bash
./build/build.sh
```

서명까지 하려면 Android SDK Build Tools의 `zipalign`, `apksigner`를 PATH에 넣고 키스토리를 지정합니다.

```bash
KEYSTORE=/path/to/keystore.jks KEY_ALIAS=key0 ./build/build.sh
```

`APKTOOL_JAR`, `ZIPALIGN`, `APKSIGNER`, `KJOURNAL_SOURCE`, `KJOURNAL_OUT` 환경변수로 경로를 바꿀 수 있습니다. 저장소에는 비밀 서명키를 넣지 않았습니다.
