from pathlib import Path
root = Path('/home/ubuntu/kjournal_5003_decode')
for rel in ['smali/xh0.smali', 'smali/pi0.smali']:
    p = root / rel
    s = p.read_text()
    old = r'const-string v8, "K\uc800\ub110 4.9"' if rel.endswith('xh0.smali') else r'const-string v4, "K\uc800\ub110 4.9"'
    new = r'const-string v8, "KJournal 5 DP1"' if rel.endswith('xh0.smali') else r'const-string v4, "KJournal 5 DP1"'
    if old not in s:
        raise SystemExit(f'not found: {rel}')
    p.write_text(s.replace(old, new))
yml = root / 'apktool.yml'
s = yml.read_text()
import re
s = re.sub(r'versionCode: \d+', 'versionCode: 5004', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 DP1', s, count=1)
yml.write_text(s)
print('patched title and versionCode=5004')
remaining = False
for base in [root/'smali', root/'smali_classes2', root/'smali_classes3']:
    for p in base.rglob('*.smali'):
        if 'K저널 4.9' in p.read_text(errors='ignore'):
            print('remaining:', p)
            remaining = True
if remaining:
    raise SystemExit('remaining visible title string')
print('no remaining K저널 4.9')
print('note: previous OTA sha mismatch was fixed separately in deployment JSON')
