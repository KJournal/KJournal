from pathlib import Path
import shutil, re
src = Path('/home/ubuntu/kjournal_dp3_verify')
root = Path('/home/ubuntu/kjournal_dp31_verify')
if root.exists(): shutil.rmtree(root)
shutil.copytree(src, root)
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5008', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 DP3.1', s, count=1)
yml.write_text(s)
# Replace any visible DP3 title variant in the decompiled title classes.
for rel in ['smali/xh0.smali', 'smali/pi0.smali']:
    p = root / rel
    if p.exists(): p.write_text(p.read_text().replace('KJournal 5 DP3', 'KJournal 5 DP3.1').replace('KJournal 5 DP2', 'KJournal 5 DP3.1'))
print(root)
print('versionCode=5008 versionName=5 DP3.1')
