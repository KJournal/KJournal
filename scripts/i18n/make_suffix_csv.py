#!/usr/bin/env python3
r"""3차 번역 CSV: 접미 라벨(" dose"/" route"/" color") 번역.

`<물질명> <투여경로> dose` / `<물질명> route` / `<물질명> color` 처럼
문자열 뒤에 영문 라벨이 붙어 표시되는 것을 한국어로 바꾼다.
"""
import csv
import io
import os
import re
import sys

ROOT = r"C:\Users\junse\Downloads\kjournal\.kilo\worktrees\ka26-i18n"
SMALI = os.path.join(ROOT, "reverse-engineering", "kjournal-157-decoded", "smali")
OUT = os.path.join(ROOT, "docs", "i18n", "pb810-ui-suffix.csv")

CONST = re.compile(r'const-string(?:/jumbo)?\s+[vp]\d+,\s+"((?:[^"\\]|\\.)*)"')
ESC = re.compile(r'\\(u[0-9a-fA-F]{4}|.)')


def unescape(s):
    def rep(m):
        c = m.group(1)
        if c.startswith("u") and len(c) == 5:
            return chr(int(c[1:], 16))
        return {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\"}.get(c, c)
    return ESC.sub(rep, s)


# (file, line, korean, note)
ENTRIES = [
    ("fv3.smali", 661, " 용량", "substance + route + ' dose'"),
    ("gc.smali", 1789, " 경로", "substance + ' route'"),
    ("d12.smali", 2560, " 색상", "substance + ' color'"),
]


def main():
    rows = []
    for f, ln, ko, note in ENTRIES:
        lines = io.open(os.path.join(SMALI, f), encoding="utf-8", newline="").read().split("\r\n")
        m = CONST.search(lines[ln - 1])
        if not m:
            print("NO LITERAL %s:%d" % (f, ln), file=sys.stderr)
            return 1
        rows.append({"file": f, "line": ln, "english": unescape(m.group(1)), "korean": ko, "note": note})

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "line", "english", "korean", "note"], quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print("  %-14s %5d %r -> %r" % (r["file"], r["line"], r["english"], r["korean"]))
    print("wrote %s (%d rows)" % (OUT, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
