from pathlib import Path

root = Path('/home/ubuntu/ota_final_verify')

yml = root / 'apktool.yml'
s = yml.read_text()
s = s.replace('versionCode: 4901', 'versionCode: 5001')
s = s.replace('versionName: 4.9.1', 'versionName: 5 DP1')
yml.write_text(s)

manifest = root / 'AndroidManifest.xml'
s = manifest.read_text()
s = s.replace('android:label="KJournal"', 'android:label="K저널"', 1)
manifest.write_text(s)

smali = root / 'smali' / 'x74.smali'
s = smali.read_text()
old = 'const-string v10, "App"'
new = 'const-string v10, "\\uc571\\n\\uac1c\\ubc1c\\uc790:\uc815\ubcd1\uc774\\n\\uae30\\uc5ec\uc790:\uc720\ub974\ubbf8"'
if s.count(old) != 1:
    raise SystemExit(f'expected one App literal, found {s.count(old)}')
s = s.replace(old, new, 1)
smali.write_text(s)
print('patched', yml, manifest, smali)
