#!/usr/bin/env python3
r"""4차 번역 CSV: 복용량 등급 범위 라벨 / 반복 복용 경고 / 국가명 등.

스크린샷에서 확인된 미번역:
  - mx1.smali: "heavy 700 mg-.." 형태의 복용량 등급 범위 라벨
  - qg0.smali: "more than 47 heavy doses" 경고
그 외 전수 스캔에서 남은 표시 문자열:
  - d12.smali: "Long-term" 섹션, " color" 접미
  - we6.smali: 물질명 없을 때 "Unknown"
  - wv0.smali: 약물검사 국가 버튼
"""
import csv
import io
import os
import re
import sys

ROOT = r"C:\Users\junse\Downloads\kjournal\.kilo\worktrees\ka26-i18n"
SMALI = os.path.join(ROOT, "reverse-engineering", "kjournal-157-decoded", "smali")
OUT = os.path.join(ROOT, "docs", "i18n", "pb810-ui-dose-labels.csv")

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
    # --- 복용량 등급 범위 라벨 (mx1) : "heavy 700 mg-.." ---
    ("mx1.smali", 270, "매우 강함 ", "dose range: heavy"),
    ("mx1.smali", 365, "강함 ", "dose range: strong"),
    ("mx1.smali", 455, "보통 ", "dose range: common"),
    ("mx1.smali", 545, "낮음 ", "dose range: light"),
    ("mx1.smali", 608, "역치 ", "dose range: threshold"),
    ("mx1.smali", 274, " 이상", "dose range: and above (mg-..)"),
    # --- 반복 복용 경고 (qg0) : "more than 47 heavy doses" ---
    ("qg0.smali", 4998, "매우 강한 용량 ", "warning prefix"),
    ("qg0.smali", 5012, "회 이상", "warning suffix"),
    # --- 물질 상세 (d12) ---
    ("d12.smali", 4464, "장기 효과", "section header"),
    ("d12.smali", 7670, " 색상", "substance + ' color'"),
    # --- 저널 (we6) ---
    ("we6.smali", 9312, "알 수 없음", "fallback when substance name is null"),
    # --- 약물검사 국가 버튼 (wv0) ---
    ("wv0.smali", 689, "오스트리아", "country"),
    ("wv0.smali", 706, "호주", "country"),
    ("wv0.smali", 719, "벨기에", "country"),
    ("wv0.smali", 732, "캐나다", "country"),
    ("wv0.smali", 745, "체코", "country"),
    ("wv0.smali", 758, "독일", "country"),
    ("wv0.smali", 771, "프랑스", "country"),
    ("wv0.smali", 784, "이탈리아", "country"),
    ("wv0.smali", 797, "네덜란드", "country"),
    ("wv0.smali", 810, "노르웨이", "country"),
    ("wv0.smali", 823, "포르투갈", "country"),
    ("wv0.smali", 836, "슬로베니아", "country"),
    ("wv0.smali", 849, "스페인", "country"),
    ("wv0.smali", 862, "스위스", "country"),
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
        print("  %-14s %5d %-22r -> %r" % (r["file"], r["line"], r["english"], r["korean"]))
    print("wrote %s (%d rows)" % (OUT, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
