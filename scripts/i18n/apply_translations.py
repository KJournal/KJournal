#!/usr/bin/env python3
r"""사람 번역 CSV를 PB8.x 디코드 smali에 적용한다.

- 입력 CSV: id,screen,english,korean,evidence,file,line,AI번역,인간번역,인간번역
  '인간번역' 열의 값을 사용한다.
- 대상: reverse-engineering/kjournal-157-decoded/smali 의 앱 파일
  (한글 리터럴이 있는 파일 + com/isaakhanimann|com/jwxn3 패키지)
- 같은 영문 문자열이 여러 위치/파일에 있으면 모두 바꾼다(화면 간 일관성).
- 한글은 기존 포크 관례대로 \uXXXX 로 이스케이프한다.
- 줄바꿈(CRLF)은 그대로 유지한다.

사용:
    python scripts/i18n/apply_translations.py --csv docs/i18n/pb89-untranslated-human-translated.csv
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import sys

DECODED = os.path.join("reverse-engineering", "kjournal-157-decoded")
CONST = re.compile(r'(const-string(?:/jumbo)?\s+v\d+,\s+")((?:[^"\\]|\\.)*)(")')
ESC = re.compile(r'\\(u[0-9a-fA-F]{4}|.)')
HANGUL = re.compile("[\uac00-\ud7a3\u3131-\u318e]")


def unescape(s: str) -> str:
    def rep(m: re.Match) -> str:
        c = m.group(1)
        if c.startswith("u") and len(c) == 5:
            return chr(int(c[1:], 16))
        return {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\"}.get(c, c)
    return ESC.sub(rep, s)


def escape(s: str) -> str:
    out = []
    for ch in s:
        if ch == "\n":
            out.append("\\n")
        elif ch == "\t":
            out.append("\\t")
        elif ch == "\r":
            out.append("\\r")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif ord(ch) <= 0x7E:
            out.append(ch)
        else:
            out.append("\\u%04x" % ord(ch))
    return "".join(out)


def load_map(csv_path: str) -> dict[str, str]:
    rows = list(csv.DictReader(io.open(csv_path, encoding="utf-8-sig")))
    if not rows:
        raise SystemExit("CSV is empty: %s" % csv_path)
    keys = [k for k in rows[0] if k and "번역" in k and k != "AI번역"]
    if not keys:
        raise SystemExit("no human-translation column found: %s" % list(rows[0].keys()))
    ko_key = keys[0]
    mapping: dict[str, str] = {}
    conflict = []
    for r in rows:
        eng = r["english"]
        ko = (r.get(ko_key) or "").strip("\n")
        if not eng:
            continue
        if eng in mapping and mapping[eng] != ko:
            conflict.append((eng, mapping[eng], ko))
        mapping[eng] = ko
    if conflict:
        for e, a, b in conflict[:10]:
            print("CONFLICT %r: %r vs %r" % (e[:40], a[:40], b[:40]))
        raise SystemExit("conflicting translations")
    return mapping


def is_app_file(rel: str, text: str) -> bool:
    if rel.startswith("com/isaakhanimann/journal/") or rel.startswith("com/jiwxn3/"):
        return True
    for m in CONST.finditer(text):
        if HANGUL.search(unescape(m.group(2))):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--decoded", default=DECODED)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mapping = load_map(args.csv)
    smali_root = os.path.join(args.decoded, "smali")
    if not os.path.isdir(smali_root):
        raise SystemExit("smali root not found: %s" % smali_root)

    used: dict[str, int] = {}
    files_changed = 0
    total_repl = 0

    for dp, _, fns in os.walk(smali_root):
        for fn in fns:
            if not fn.endswith(".smali"):
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, smali_root).replace("\\", "/")
            text = io.open(path, encoding="utf-8", newline="").read()
            if not is_app_file(rel, text):
                continue

            count = 0

            def repl(m: re.Match) -> str:
                nonlocal count
                val = unescape(m.group(2))
                if val not in mapping:
                    return m.group(0)
                count += 1
                used[val] = used.get(val, 0) + 1
                return m.group(1) + escape(mapping[val]) + m.group(3)

            new = CONST.sub(repl, text)
            if count:
                files_changed += 1
                total_repl += count
                if not args.dry_run:
                    io.open(path, "w", encoding="utf-8", newline="").write(new)

    missing = sorted(set(mapping) - set(used))
    print("csv entries      : %d" % len(mapping))
    print("files changed    : %d" % files_changed)
    print("replacements     : %d" % total_repl)
    print("entries not found: %d" % len(missing))
    for m in missing[:20]:
        print("   MISSING %r" % m[:60])
    if args.dry_run:
        print("(dry-run: no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
