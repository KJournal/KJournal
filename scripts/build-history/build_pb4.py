from pathlib import Path
import shutil, re

base = Path('/home/ubuntu/kjournal_pb3_final_decode')
root = Path('/home/ubuntu/kjournal_pb4_verify')
if root.exists():
    shutil.rmtree(root)
shutil.copytree(base, root)

yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5014', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 PB4', s, count=1)
yml.write_text(s)

# The visible substance title is generated in d53.smali, not op0.smali.
p = root / 'smali/d53.smali'
s = p.read_text()
for old, new in [
    ('const-string v9, " ingestion"', 'const-string v9, " 섭취"'),
    ('const-string v8, " ingestions"', 'const-string v8, " 섭취 기록"'),
]:
    if old not in s:
        raise SystemExit(f'missing visible literal: {old}')
    s = s.replace(old, new)
p.write_text(s)
print(root)
print('versionCode=5014 versionName=5 PB4')
print('patched d53 visible title and plural label')
