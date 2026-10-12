#!/usr/bin/env python3
r"""PB8.x 미번역 UI 문자열 2차 적용 (파일:줄 지정 방식).

1차(apply_translations.py)는 전역 치환이라 짧은 단어(common/light/…)를
로직 키까지 바꿀 위험이 있어, 2차는 (file, line)로 정확한 리터럴만 바꾼다.

입력 CSV: file,line,english,korean,note
사용:
    python scripts/i18n/apply_untranslated2.py --csv docs/i18n/pb810-ui-remaining.csv
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import sys

DECODED = os.path.join("reverse-engineering", "kjournal-157-decoded")
CONST = re.compile(r'(const-string(?:/jumbo)?\s+[vp]\d+,\s+")((?:[^"\\]|\\.)*)(")')
ESC = re.compile(r'\\(u[0-9a-fA-F]{4}|.)')


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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--decoded", default=DECODED)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = list(csv.DictReader(io.open(args.csv, encoding="utf-8-sig")))
    smali_root = os.path.join(args.decoded, "smali")

    by_file: dict[str, list[dict]] = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)

    changed = 0
    problems = []
    for rel, items in by_file.items():
        path = os.path.join(smali_root, rel.replace("/", os.sep))
        if not os.path.isfile(path):
            problems.append("file not found: %s" % rel)
            continue
        text = io.open(path, encoding="utf-8", newline="").read()
        lines = text.split("\r\n")
        for r in items:
            ln = int(r["line"])
            eng = r["english"]
            kor = r["korean"]
            if not (1 <= ln <= len(lines)):
                problems.append("%s:%d out of range" % (rel, ln))
                continue
            m = CONST.search(lines[ln - 1])
            if not m or unescape(m.group(2)) != eng:
                got = unescape(m.group(2))[:50] if m else lines[ln - 1][:60]
                problems.append("%s:%d mismatch: expected %r got %r" % (rel, ln, eng[:50], got))
                continue
            lines[ln - 1] = lines[ln - 1][:m.start(2)] + escape(kor) + lines[ln - 1][m.end(2):]
            changed += 1
        if not args.dry_run:
            io.open(path, "w", encoding="utf-8", newline="").write("\r\n".join(lines))

    print("rows            : %d" % len(rows))
    print("replacements    : %d" % changed)
    print("problems        : %d" % len(problems))
    for p in problems[:20]:
        print("   ", p)
    if args.dry_run:
        print("(dry-run: no files written)")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
