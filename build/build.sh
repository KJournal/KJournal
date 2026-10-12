#!/usr/bin/env bash
# 재현 가능한 빌드: reverse-engineering 디코드 트리 → APK (서명 선택)
#
# 환경변수:
#   KEYSTORE       서명 키스토어 경로 (없으면 unsigned)
#   KEY_ALIAS      키 별칭 (기본 key0)
#   KEYSTORE_PASS  키스토어 비밀번호 (있으면 apksigner 에 env: 로 전달)
#   KEY_PASS       키 비밀번호
#   KJOURNAL_SOURCE  소스 트리 (기본 reverse-engineering/kjournal-pb6-decoded)
#   KJOURNAL_OUT     출력 디렉터리 (기본 build/out)
#   APK_NAME         출력 파일 접두어 (기본 KJournal-PB6)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${KJOURNAL_SOURCE:-$ROOT/reverse-engineering/kjournal-pb6-decoded}"
OUT_DIR="${KJOURNAL_OUT:-$ROOT/build/out}"
APKTOOL="${APKTOOL_JAR:-$ROOT/build/apktool.jar}"
NAME="${APK_NAME:-KJournal-PB6}"
ZIPALIGN="${ZIPALIGN:-$(command -v zipalign || true)}"
APKSIGNER="${APKSIGNER:-$(command -v apksigner || true)}"

# Android SDK 의 build-tools 로 폴백 (PATH 에 zipalign/apksigner 가 없을 때)
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}"
if [[ ( -z "$ZIPALIGN" || -z "$APKSIGNER" ) && -n "$SDK" && -d "$SDK/build-tools" ]]; then
  BT="$(ls -1 "$SDK/build-tools" 2>/dev/null | sort -V | tail -n1 || true)"
  if [[ -n "$BT" ]]; then
    for cand in "$SDK/build-tools/$BT/zipalign" "$SDK/build-tools/$BT/zipalign.exe"; do
      [[ -z "$ZIPALIGN" && -f "$cand" ]] && ZIPALIGN="$cand"
    done
    for cand in "$SDK/build-tools/$BT/apksigner" "$SDK/build-tools/$BT/apksigner.bat"; do
      [[ -z "$APKSIGNER" && -f "$cand" ]] && APKSIGNER="$cand"
    done
  fi
fi

[[ -f "$APKTOOL" ]] || { echo "apktool.jar not found: $APKTOOL" >&2; exit 1; }
[[ -d "$SRC" ]] || { echo "source not found: $SRC" >&2; exit 1; }
mkdir -p "$OUT_DIR" "$ROOT/build/work"

# Apktool 3.0.3 selects its bundled aapt2 tool automatically.
# smali 파일만 수정하면 디렉터리 mtime 이 그대로라 apktool 이 변경을 놓친다.
touch "$SRC/smali" 2>/dev/null || true
java -jar "$APKTOOL" b "$SRC" -o "$ROOT/build/work/unsigned.apk"

if [[ -n "$ZIPALIGN" && -n "$APKSIGNER" ]]; then
  "$ZIPALIGN" -f 4 "$ROOT/build/work/unsigned.apk" "$OUT_DIR/${NAME}-aligned.apk"
  if [[ -n "${KEYSTORE:-}" ]]; then
    SIGN_ARGS=(sign --ks "$KEYSTORE" --ks-key-alias "${KEY_ALIAS:-key0}" --out "$OUT_DIR/${NAME}.apk")
    [[ -n "${KEYSTORE_PASS:-}" ]] && SIGN_ARGS+=(--ks-pass "env:KEYSTORE_PASS")
    [[ -n "${KEY_PASS:-}" ]] && SIGN_ARGS+=(--key-pass "env:KEY_PASS")
    "$APKSIGNER" "${SIGN_ARGS[@]}" "$OUT_DIR/${NAME}-aligned.apk"
    echo "Signed APK: $OUT_DIR/${NAME}.apk"
  else
    cp "$OUT_DIR/${NAME}-aligned.apk" "$OUT_DIR/${NAME}.apk"
    echo "No KEYSTORE supplied; produced aligned unsigned APK." >&2
  fi
else
  cp "$ROOT/build/work/unsigned.apk" "$OUT_DIR/${NAME}-unsigned.apk"
  echo "zipalign/apksigner not found; produced unsigned APK." >&2
fi
printf 'Build output: %s\n' "$OUT_DIR"
