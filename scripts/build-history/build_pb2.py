from pathlib import Path
import shutil
import re

src = Path('/home/ubuntu/kjournal_pb1_final_decode')
root = Path('/home/ubuntu/kjournal_pb2_verify')
if root.exists():
    shutil.rmtree(root)
shutil.copytree(src, root)

yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5012', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 PB2', s, count=1)
yml.write_text(s)

for p in root.glob('smali*/**/*.smali'):
    text = p.read_text()
    new = text.replace('KJournal 5 PB1', 'KJournal 5 PB2')
    if new != text:
        p.write_text(new)

print(root)
print('versionCode=5012 versionName=5 PB2')
