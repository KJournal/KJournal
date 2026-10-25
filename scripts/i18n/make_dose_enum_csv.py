#!/usr/bin/env python3
r"""5차 번역 CSV: 복용량 등급 enum 표시명 + " DOSAGE" 타이틀.

cw0.smali 는 `DoseClass.name() + " DOSAGE"` 로 제목을 만든다(예: "HEAVY DOSAGE").
DoseClass(ct1) enum 은 직렬화/DB 저장/ valueOf 호출이 없어(전수 확인)
이름을 한국어로 바꿔도 안전하다.
"""
import csv
import io
import os
import re
import sys

ROOT = r"C:\Users\junse\Downloads\kjournal\.kilo\worktrees\ka26-i18n"
SMALI = os.path.join(ROOT, "reverse-engineering", "kjournal-157-decoded", "smali")
OUT = os.path.join(ROOT, "docs", "i18n", "pb810-ui-dose-enum.csv")

CONST = re.compile(r'const-string(?:/jumbo)?\s+[vp]\d+,\s+"((?:[^"\\]|\\.)*)"')
ESC = re.compile(r'\\(u[0-9a-fA-F]{4}|.)')


def unescape(s):
    def rep(m):
        c = m.group(1)
        if c.startswith("u") and len(c) == 5:
            return chr(int(c[1:], 16))
        return {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\"}.get(c, c)
    return ESC.sub(rep, s)


ENTRIES = [
    ("bt1.smali", 11, "역치", "DoseClass.THRESHOLD enum name"),
    ("zs1.smali", 11, "낮음", "DoseClass.LIGHT enum name"),
    ("xs1.smali", 11, "보통", "DoseClass.COMMON enum name"),
    ("at1.smali", 11, "강함", "DoseClass.STRONG enum name"),
    ("ys1.smali", 11, "매우 강함", "DoseClass.HEAVY enum name"),
    ("cw0.smali", 319, " 용량", "'{class} DOSAGE' title"),
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
        print("  %-14s %5d %-14r -> %r" % (r["file"], r["line"], r["english"], r["korean"]))
    print("wrote %s (%d rows)" % (OUT, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
