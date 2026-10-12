#!/usr/bin/env python3
r"""public-beta(PB8.x) 디코드 smali에서 "아직 한국어로 번역되지 않은 영문 UI 문자열"을
뽑아 번역 작업용 CSV로 정리한다.

규칙
  1) 근거는 코드(smali) 1순위: origin/public-beta 의
     reverse-engineering/kjournal-157-decoded/smali 의 const-string 리터럴을 스캔한다.
  2) 한글(\uXXXX)이 포함된 리터럴은 "이미 번역됨" → 제외.
  3) assets/Substances.json 의 문자열(물질명·카테고리·요약 등) → 제외.
  4) 라이브러리/프레임워크/디버그 문자열 → 제외.
  5) 데이터성 목록(약물검사 기관명·물질명 사전) → 제외.
  6) 남은 영문만 CSV 로 출력. CSV 는 `english`/`korean` 외에는 ASCII 만 쓴다
     (한글이 섞여 "번역된 것처럼" 보이지 않도록).

출력 컬럼: id, screen, english, korean, evidence, file, line
  - screen  : ASCII 화면 키 (settings, timeline, faq …)
  - english : 번역할 영문 원문
  - korean  : 번역 입력란 (비어 있음)
  - evidence: dump = 실제 화면 덤프에서 영문으로 확인됨, smali = smali 근거만

사용:
    python scripts/i18n/extract_untranslated.py
    python scripts/i18n/extract_untranslated.py --ref origin/public-beta --out docs/reimpl/i18n
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import subprocess
import sys
import tempfile

DECODED = "reverse-engineering/kjournal-157-decoded"

CONST = re.compile(r'const-string(?:/jumbo)?\s+(v\d+),\s+"((?:[^"\\]|\\.)*)"')
ESC = re.compile(r'\\(u[0-9a-fA-F]{4}|.)')
HANGUL = re.compile("[\uac00-\ud7a3\u3131-\u318e]")

# 파일 전체가 라이브러리/프레임워크/디버그 성격 → 제외
LIB_FILES = {
    "sj1.smali", "ab4.smali", "f80.smali", "ch4.smali", "k90.smali", "me.smali",
    "la.smali", "hl1.smali", "wv5.smali", "oe4.smali", "df0.smali", "dx0.smali",
    "kh6.smali", "i07.smali", "uc4.smali", "hb6.smali",
}

# 데이터성 목록(번역 대상 아님) → 제외
DATA_FILES = {
    "dw0.smali",                                              # 약물검사 기관/도시
    "b73.smali",                                              # 물질명 사전
}

# 라이브러리/프레임워크/디버그 문자열 조각 → 제외
NOISE_SUBSTR = [
    "Serializer", "serializer", "Serializable", "@Serializable", "polymorphic",
    "coroutine", "'resume'", "ViewModelStoreOwner", "ViewModelProvider",
    "unattached node", "visitAncestors", "visitChildren", "ActiveParent",
    "ImageVector.Builder", "non-wrap", "SavedStateHandle", "enableSavedStateHandles",
    "Lifecycle", "snapshot", "Snapshot", "Okio Watchdog", "room_master_table",
    "SELECT changes()", "Cannot collect column names", "Available columns",
    "Glance App Widget", "webkit", "emoji font provider", "TextureVideoView",
    "CustomerInfo", "paywall", "Paywall", "checkout", "Checkout",
    "UNKNOWN_BILLING_RESPONSE_CODE", "UNKNOWN_SUB_RESPONSE_CODE",
    "Block store", "Blockstore", "Block Store", "user ID", "UserID", "userId",
    "prefetch blob", "Illegal value", "Illegal index", "Invalid byte order",
    "invalid tag", "array.size", "DataStore scope was cancelled",
    "initiating package purchase", "Web checkout", "web checkout",
    "Auto-dismissing", "Activity is null", "InterruptionHandlingOffset",
    "EnterExitTransition", "Aliasing Block", "null current looper",
    "No recompose scope", "no recompose scope", "single-line",
    "Must be called on", "No valid saved state", "is not concrete", "base class",
    "not found in step", "Workflow step", "Workflow singleStepFallbackId",
    "Incompatible store", "Unsupported type", "Required value was null",
    "Check failed", "An error occurred while retrieving", "Error when decoding",
    "Error when reading", "Error attempting to load resource", "Error in Glance",
    "No localization found", "No localized tier name", "No packages found",
    "No tier found", "None of the tiers", "has no available products",
    "Package with id", "No path data available", "No start tag found",
    "Non-window condition", "Unexpected protocol", "Unexpected TLS",
    "2-D focus search", "onMainFrameNavigationStarted", "onContentGestureVerdict",
    "onChangeIsPartOfTimeline", "saveIsFavorite",
    "saveMissingTimelineDurationDisclaimerIsHidden", "saveOralDisclaimerIsHidden",
    "load()V", "DebugMessage", "error sending pendingIntent", "System property",
    "Failed to ", "Failed ", "Error when ", "Unexpected", "Unknown error",
    "Decoding file failed", "File not found", "Please try again",
    "unidentified replacement mode", "there already exists", "does not exist",
    "Ignoring.", "not found. Ignoring", "Attempt to ", "Cannot ", "cannot ",
    "Invalid ", "invalid ", "Illegal ", "illegal ", "must be ", "must not be ",
    "Expected ", "expected ", "Provided class", "Only KClass",
    "Only VectorDrawables", "Unable to call isTagEnabled", "Unable to log",
    "This function should only be used for", "Failed to format the number",
    "Label must not be blank", "Purity must be between", "Height must be positive",
    "At least one point must be provided", "ActiveParent must",
    "Current mutation had a higher priority", "no timeline",
    "call to 'resume'", "Operation is not supported for read-only collection",
    "Collection contains no element matching the predicate", "Expected NON-NULL",
    "LayoutCoordinate operations", "Blank serial names",
    "Cannot create a mutable snapshot", "Index must be between",
    "Could not convert ", "Cannot coerce value", "Char sequence is empty",
    "Connection", "Warning", "Trace", "Check", "Estimated standard deviation",
    "Unknown", "Invalid", "None", "column '",
    "Android release:", "Android SDK:", "Device:", "Timezone:", "Package name:",
    "Installer package:", "First install time:", "Last update time:",
    "Generated at:", "Active subscriptions:", "All purchased product IDs:",
    "Entitlement verification:", "CustomerInfo ", "RevenueCat ", "Premium ",
    "UI has premium", "Premium debug", "Premium entitlement", "Premium expiration",
    "Premium latest", "Premium original", "Premium ownership", "Premium period",
    "Premium product", "Premium store", "Premium unsubscribe", "Premium verification",
    "Premium will renew", "Premium billing issue", "App version:", "Build type:",
    "Debug build:", "PsychonautWiki Journal support info", "Amazon Appstore",
    "Galaxy Store", "Play Store", "Test Store",
    "Customer Center is not yet implemented", "The Loop", "Get Your Drugs Tested",
    " in 68% of cases", " in 95% of cases", " means:", ":memory:", "Tier ",
    "Duration: ", " in (since start)", "compose.foundation.Image", " of kind ",
    " for key ", "' for ", "' is not found ", " are affected by this edit",
    "The suggested name '", "With: ", "Is favorite", "enum value",
    "cd (common doses)", "unknown dose ", "0 dots means",
    "Archived custom units don't show up", "Archived units don't show up",
    "Remembering ", "Thread", "Committed ", "Awaiting ",
    # Compose/Material 내부
    "Built-in ", "Hint", "Label", "Leading", "Trailing", "Prefix", "Suffix",
    "Supporting", "after effects:", "total:", "Go to", "Explore",
    "If you wish to display this", "Dismiss", "Longer explanations",
    "Threshold, light, common", "d MMM yyyy", "Here", "androidx.",
    "Experience", "Ingestion", "Show more info",
    "contains:", ". ErrorCode: ", ". SubResponseCode: ", "Time",
    "Bunk Police",
]

# 파일 → ASCII 화면 키
AREA = {
    "iw0.smali": "settings", "iw5.smali": "settings", "gw5.smali": "release_notes",
    "k15.smali": "preferences", "va.smali": "preferences", "bg0.smali": "preferences",
    "ew0.smali": "timeline", "ow0.smali": "substance_docs", "rv0.smali": "safer_use",
    "pv0.smali": "safer_sniffing", "jt1.smali": "dosage_guide",
    "d12.smali": "substance_detail", "vb3.smali": "substance_detail",
    "xv0.smali": "drugs_screen", "qv0.smali": "search", "er5.smali": "filters",
    "ha.smali": "stats", "ra6.smali": "stats", "u86.smali": "stats",
    "ga.smali": "stats", "kc.smali": "premium", "we6.smali": "journal",
    "ev3.smali": "journal", "hw0.smali": "experience_edit", "fw0.smali": "experience_edit",
    "de4.smali": "experience", "nf2.smali": "widget_notification",
    "oh1.smali": "date_picker", "b96.smali": "stats_range",
    "id.smali": "custom_units_archive", "tf.smali": "custom_units_archive",
    "ww0.smali": "contribution", "ra.smali": "substance_colors",
    "a2.smali": "safer_use", "gc.smali": "common", "ie.smali": "timeline",
    "fa2.smali": "timeline", "g90.smali": "timeline", "p07.smali": "timeline",
    "p31.smali": "custom_unit_edit", "pw0.smali": "ingestion_edit",
    "kk3.smali": "custom_unit", "xw0.smali": "add_ingestion",
    "xb4.smali": "relative_time", "ma6.smali": "import_export",
    "t02.smali": "import_export", "kb4.smali": "import_export",
    "com/isaakhanimann/journal/ota/OtaUpdater.smali": "ota",
    "com/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService.smali": "notification",
    "com/isaakhanimann/journal/util/CategoryKo.smali": "category",
}


def unescape(s: str) -> str:
    def rep(m: re.Match) -> str:
        c = m.group(1)
        if c.startswith("u") and len(c) == 5:
            return chr(int(c[1:], 16))
        return {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\"}.get(c, c)
    return ESC.sub(rep, s)


def extract_smali(root: str) -> dict[str, list[tuple[int, str]]]:
    out: dict[str, list[tuple[int, str]]] = {}
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if not fn.endswith(".smali"):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace("\\", "/")
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            lits = []
            for m in CONST.finditer(t):
                line = t.count("\n", 0, m.start()) + 1
                lits.append((line, unescape(m.group(2))))
            out[rel] = lits
    return out


def load_substance_strings(path: str) -> set[str]:
    try:
        data = json.load(io.open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    vals: set[str] = set()

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str):
            vals.add(o.strip().lower())
    walk(data)
    return vals


def load_dump_english(paths: list[str]) -> set[str]:
    out: set[str] = set()
    targets: list[str] = []
    for p in paths:
        if os.path.isdir(p):
            for dp, _, fns in os.walk(p):
                for fn in fns:
                    if fn.lower().endswith((".txt", ".xml")):
                        targets.append(os.path.join(dp, fn))
        elif os.path.isfile(p):
            targets.append(p)
    for p in targets:
        for line in io.open(p, encoding="utf-8", errors="replace").read().split("\n"):
            t = line.strip()
            if not t or HANGUL.search(t) or not re.search(r"[A-Za-z]", t):
                continue
            out.add(t)
    return out


def is_app_file(rel: str, lits: list[tuple[int, str]]) -> bool:
    if any(HANGUL.search(v) for _, v in lits):
        return True
    return rel.startswith("com/isaakhanimann/journal/") or rel.startswith("com/jiwxn3/")


def is_english_candidate(s: str) -> bool:
    if not re.search(r"[A-Za-z]", s):
        return False
    if HANGUL.search(s):
        return False
    st = s.strip()
    if not st:
        return False
    if "://" in st or st.startswith("http"):
        return False
    if re.match(r"^L[\w/$]+;$", st):
        return False
    if st[0] in "[(" or st.startswith("<"):
        return False
    tmp = re.sub(r"%[0-9$#+.,\-]*[sdfxXeEgGocbBhHn%]", "", st)
    if not re.search(r"[A-Za-z]", tmp):
        return False
    if "/" in st and " " not in st:
        return False
    if "\\" in st:
        return False
    if re.match(r"^[A-Za-z0-9_.\-]+$", st) and " " not in st:
        return bool(re.match(r"^[A-Z][a-z]+(?:['\u2019][A-Za-z]+)?[.!?:]?$", st))
    if re.match(r"^[A-Z0-9_]{2,}$", st):
        return False
    if re.search(r"[{};=]", st):
        return False
    return True


def is_noise(s: str) -> bool:
    return any(n in s for n in NOISE_SUBSTR)


def ensure_source(ref: str) -> str:
    tmp = os.path.join(tempfile.gettempdir(), "kilo", "i18n-pb")
    os.makedirs(tmp, exist_ok=True)
    root = os.path.join(tmp, "dec", DECODED.replace("/", os.sep))
    if os.path.isdir(os.path.join(root, "smali")):
        return root
    tar = os.path.join(tmp, "pb.tar")
    dec = os.path.join(tmp, "dec")
    os.makedirs(dec, exist_ok=True)
    subprocess.run(
        ["git", "archive", "-o", tar, ref, f"{DECODED}/smali", f"{DECODED}/res",
         f"{DECODED}/assets", f"{DECODED}/AndroidManifest.xml"],
        check=True,
    )
    subprocess.run(["tar", "-x", "-f", tar, "-C", dec], check=True)
    return root


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/public-beta")
    ap.add_argument("--out", default=os.path.join("docs", "reimpl", "i18n"))
    ap.add_argument("--decoded", default=None)
    ap.add_argument("--dumps", nargs="*", default=[
        os.path.join("docs", "reimpl", "golden", "cmp-original"),
    ], help="실제 화면 영문 대조용 UI 덤프 경로")
    args = ap.parse_args()

    root = args.decoded or ensure_source(args.ref)
    smali_root = os.path.join(root, "smali")
    sub_path = os.path.join(root, "assets", "Substances.json")

    files = extract_smali(smali_root)
    app_files = {r: l for r, l in files.items() if is_app_file(r, l)}
    substance = load_substance_strings(sub_path)
    dump_en = load_dump_english(args.dumps)

    rows = []
    for rel, lits in app_files.items():
        if rel in LIB_FILES or rel in DATA_FILES:
            continue
        for line, v in lits:
            if not is_english_candidate(v):
                continue
            if v.strip().lower() in substance:
                continue
            if is_noise(v):
                continue
            rows.append((rel, line, v))

    seen: dict[str, tuple[str, int]] = {}
    for rel, line, v in rows:
        seen.setdefault(v, (rel, line))

    items = []
    for v, (fpath, ln) in seen.items():
        screen = AREA.get(fpath, "misc")
        ev = "dump" if any(v.strip() == d or (len(v.strip()) >= 6 and v.strip() in d)
                           for d in dump_en) else "smali"
        items.append((v, fpath, ln, screen, ev))

    items.sort(key=lambda r: (0 if r[4] == "dump" else 1, r[3], r[0].lower()))

    os.makedirs(args.out, exist_ok=True)
    csvp = os.path.join(args.out, "pb89-untranslated.csv")
    with io.open(csvp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["id", "screen", "english", "korean", "evidence", "file", "line"])
        for i, (v, fpath, ln, screen, ev) in enumerate(items, 1):
            w.writerow([f"t{i:04d}", screen, v, "", ev, fpath, ln])

    shown = sum(1 for r in items if r[4] == "dump")
    print(f"scanned smali: {len(files)} / app files: {len(app_files)}")
    print(f"substances.json excluded: {len(substance)}")
    print(f"rows: {len(items)}  (dump-confirmed {shown} / smali-only {len(items) - shown})")
    print(f"wrote: {csvp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
