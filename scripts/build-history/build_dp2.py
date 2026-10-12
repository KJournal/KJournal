from pathlib import Path
import re, shutil
src = Path('/home/ubuntu/kjournal_5005_verify')
root = Path('/home/ubuntu/kjournal_dp2_verify')
if root.exists(): shutil.rmtree(root)
shutil.copytree(src, root)
# Version metadata
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5006', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 DP2', s, count=1)
yml.write_text(s)
# Visible English labels from the supplied screenshot
repls = {
    'smali/k70.smali': [('const-string v5, " ago"', 'const-string v5, " 전"'), ('const-string v4, "Now "', 'const-string v4, "현재 "'), ('const-string v5, " in (since start)"', 'const-string v5, " (시작 후)"')],
    'smali/l20.smali': [('const-string v11, "Now"', 'const-string v11, "현재"')],
    'smali/q82.smali': [('const-string v1, " contains:"', 'const-string v1, " 포함:"')],
}
for rel, pairs in repls.items():
    p = root / rel
    s = p.read_text()
    for old, new in pairs:
        if old not in s: raise SystemExit(f'missing {old} in {rel}')
        s = s.replace(old, new)
    p.write_text(s)
# Keep the visible app title synchronized with the DP2 metadata.
for rel, old, new in [
    ('smali/xh0.smali', 'const-string v8, "KJournal 5 DP1"', 'const-string v8, "KJournal 5 DP2"'),
    ('smali/pi0.smali', 'const-string v4, "KJournal 5 DP1"', 'const-string v4, "KJournal 5 DP2"'),
]:
    p = root / rel
    s = p.read_text()
    if old not in s: raise SystemExit(f'missing title in {rel}')
    p.write_text(s.replace(old, new))
print(root)
print('versionCode=5006 versionName=5 DP2')
print('translated: ago, Now, contains:')
print('note: Samsung malware warning cannot be bypassed by app code; it is a device security verdict')
