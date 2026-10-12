#!/usr/bin/env python3
r"""2차 번역 CSV 생성기.

(file, line, korean) 목록을 smali에서 실제 영문 원문과 대조해
docs/i18n/pb810-ui-remaining.csv 를 만든다. 영문은 파일에서 직접 읽으므로
전사 오류가 없다.
"""
import csv
import io
import os
import re
import sys

ROOT = r"C:\Users\junse\Downloads\kjournal\.kilo\worktrees\ka26-i18n"
SMALI = os.path.join(ROOT, "reverse-engineering", "kjournal-157-decoded", "smali")
OUT = os.path.join(ROOT, "docs", "i18n", "pb810-ui-remaining.csv")

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
    # --- 복용량 등급 이름 (용량 차트 y축) ---
    ("yf0.smali", 5019, "역치  ", "dose chart label"),
    ("yf0.smali", 5260, "낮음", "dose chart label"),
    ("yf0.smali", 5656, "보통", "dose chart label"),
    ("yf0.smali", 6056, "강함", "dose chart label"),
    ("yf0.smali", 6418, "매우 강함", "dose chart label"),
    ("wv0.smali", 2546, "역치, 낮음, 보통, 강함, 매우 강함", "dose scale caption"),
    # --- 복용량 등급 편집 라벨 (물질/단위 편집) ---
    ("rd.smali", 311, "역치", "dose class row label"),
    ("rd.smali", 557, "매우 강함 최소", "dose class row label"),
    ("rd.smali", 803, "강함 최소", "dose class row label"),
    ("rd.smali", 1049, "보통 최소", "dose class row label"),
    ("rd.smali", 1294, "보통 최소", "dose class row label"),
    ("rd.smali", 1535, "매우 강함 최소", "dose class row label"),
    ("rd.smali", 1780, "강함 최소", "dose class row label"),
    # --- 복용량 등급 설명 ---
    ("bt1.smali", 87,
     "역치 용량은 물질로 인한 정신적·신체적 변화가 처음으로 나타나기 시작하는 용량입니다.\n"
     "이 효과는 위약과는 분명히 다르지만, 주의를 외부 환경으로 돌리면 어느 정도 노력으로 무시할 수도 있습니다.\n"
     "이 단계에서는 막연히 '무언가'가 느껴지거나 뒤에서 기대감 같은 에너지가 쌓이는 것을 감지할 수 있습니다.",
     "THRESHOLD description"),
    ("zs1.smali", 87,
     "낮은 용량은 술을 마시지 않은 상태와 어느 정도 구분되지만, 평소의 자각을 덮어쓸 정도는 아닌 상태를 만듭니다.\n"
     "주의를 외부 환경으로 더 돌리고 복잡한 작업을 하면 효과를 무시할 수 있습니다.\n"
     "물질의 효과를 알아차리려면 특별히 주의를 기울여야 하거나, 약간 느껴지더라도 계속 주의를 끌지는 않습니다.",
     "LIGHT description"),
    ("ct1.smali", 256,
     "보통 용량은 물질의 효과와 성질이 꽤 분명하고 뚜렷하게 나타나는 용량으로, 평소의 자각이 흐려져 효과를 무시하기 어려워집니다.\n"
     "대체로 일상적인 행동을 할 수 있고 기능과 의사소통 능력도 유지되지만, 이는 개인차가 있습니다.\n"
     "효과가 주된 역할을 하도록 둘 수도 있고, 충분히 노력하거나 긴급한 상황에서는 다른 활동에 우선하도록 억누를 수도 있습니다.",
     "COMMON description"),
    ("at1.smali", 82,
     "강한 용량에서는 대부분 기능을 하거나 정상적으로 상호작용하거나 논리적으로 생각하기 어려워집니다.\n"
     "물질의 효과가 뚜렷해 더 이상 무시하거나 억누를 수 없으며, 원하든 원하지 않든 경험에 완전히 몰입하게 됩니다. 이 단계에서는 부정적인 효과가 더 흔해집니다.\n"
     "강한 용량에서는 행동의 방향을 스스로 바꾸기 어려우므로, 미리 환경과 활동을 준비하고 필요한 예방 조치를 취해 두는 것이 매우 중요합니다.",
     "STRONG description"),
    ("ys1.smali", 83,
     "매우 강한 용량은 물질이 정신활성 효과 면에서 낼 수 있는 상한에 해당하며, 이 범위를 넘어서면 부작용이 빠르게 늘고 바람직한 효과는 거의 늘지 않습니다.\n"
     "섭취한 물질에 따라 기능과 의사소통이 불가능해질 수 있고, 낮은 용량에서 느꼈던 긍정적 효과를 덮어쓸 정도로 극도로 불편한 부작용이 나타날 수 있습니다.\n"
     "매우 강한 용량에서는 응급 상황이 생겨도 스스로를 제대로 돌보기 어려우므로 위해 감소 조치를 반드시 취해야 합니다. 트립 시터를 두는 것을 강력히 권장합니다.\n"
     "또한 매우 강한 용량과 과다복용의 경계는 흔히 매우 모호하다는 점을 알아야 하며, 매우 강한 용량을 택할 때마다 부상, 입원, 사망 위험이 크게 높아집니다.\n"
     "매우 강한 용량을 규칙적으로 섭취하려는 욕구나 강박('만성 사용')은 내성, 중독 또는 다른 정신 건강 문제의 신호일 수 있습니다.",
     "HEAVY description"),
    # --- 타임라인/저널 ---
    ("we6.smali", 8650, "즐겨찾기", "content description"),
    ("we6.smali", 9892, "함께: ", "concat prefix"),
    ("we6.smali", 18259, "cd (보통 용량)", "chart legend"),
    ("we6.smali", 19276, "알 수 없는 용량 ", "content description prefix"),
    ("we6.smali", 19548, "개의 경험", "count suffix"),
    ("we6.smali", 19583, "개의 경험", "count suffix"),
    # --- 기타 UI ---
    ("tf.smali", 730, "보관된 단위는 섭취를 추가할 때 표시되지 않습니다", "description"),
    ("bc.smali", 497, "사용자 정의 물질 ", "concat prefix"),
    ("fm0.smali", 632, "성분", "label"),
    ("fm0.smali", 934, "메모", "label"),
    ("g0.smali", 3255, "단위 생성 대상: ", "concat prefix"),
    ("ua5.smali", 1061, "판매처", "label"),
    ("i40.smali", 370, "최고 슐긴 등급 ", "concat prefix"),
    ("xb4.smali", 7755, "자세히 보기", "button"),
    ("wv0.smali", 1162, "닫기", "button"),
    ("r71.smali", 68, "캡슐", "default custom unit name"),
    ("r71.smali", 78, "캡슐", "default custom unit unit"),
    ("r71.smali", 82, "캡슐", "default custom unit unitPlural"),
    ("r71.smali", 86, "메모", "default note placeholder"),
    ("ha.smali", 934,
     "물질은 보통 용량(cd)을 기준으로 한 번만 집계됩니다. 섭취 기록의 용량을 알 수 없거나 해당 물질에 정의된 보통 용량이 없으면 전혀 집계되지 않습니다.",
     "stats explanation"),
]


def main():
    rows = []
    for f, ln, ko, note in ENTRIES:
        path = os.path.join(SMALI, f)
        lines = io.open(path, encoding="utf-8", newline="").read().split("\r\n")
        m = CONST.search(lines[ln - 1])
        if not m:
            print("NO LITERAL %s:%d" % (f, ln), file=sys.stderr)
            return 1
        eng = unescape(m.group(1))
        rows.append({"file": f, "line": ln, "english": eng, "korean": ko, "note": note})

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "line", "english", "korean", "note"], quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print("wrote %s (%d rows)" % (OUT, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
