from pathlib import Path
import shutil, re
src = Path('/home/ubuntu/kjournal_dp4_final_decode')
root = Path('/home/ubuntu/kjournal_pb1_verify')
if root.exists():
    shutil.rmtree(root)
shutil.copytree(src, root)
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5011', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 PB1', s, count=1)
yml.write_text(s)
# Fix strings shown in the supplied screenshot.
for rel, replacements in {
    'smali/s33.smali': {'const-string v3, "Today"': 'const-string v3, "오늘"'},
    'smali/qy4.smali': {'const-string v15, "Now"': 'const-string v15, "지금"'},
}.items():
    p = root / rel
    text = p.read_text()
    for old, new in replacements.items():
        if old not in text:
            raise SystemExit(f'missing expected string in {rel}: {old}')
        text = text.replace(old, new)
    p.write_text(text)
# The obfuscated UI contains the same relative-time label in several
# generated screen classes; translate every remaining literal in app smali.
for p in root.glob('smali*/**/*.smali'):
    text = p.read_text()
    new = text.replace('"Today"', '"오늘"').replace('"Now"', '"지금"')
    if new != text:
        p.write_text(new)
# Ensure any visible DP4 title from the previous patch is PB1.
for p in root.glob('smali*/**/*.smali'):
    text = p.read_text()
    new = text.replace('KJournal 5 DP4', 'KJournal 5 PB1')
    if new != text:
        p.write_text(new)
print(root)
        
# expected output: /home/ubuntu/kjournal_pb1_verify
        
