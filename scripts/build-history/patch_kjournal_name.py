from pathlib import Path
root = Path('/home/ubuntu/ota_dp1_verify')
yml = root / 'apktool.yml'
s = yml.read_text().replace('versionCode: 5001', 'versionCode: 5002')
yml.write_text(s)
manifest = root / 'AndroidManifest.xml'
s = manifest.read_text().replace('android:label="K저널"', 'android:label="KJournal"', 1)
manifest.write_text(s)
for p in root.glob('res/values*/strings.xml'):
    s = p.read_text()
    if '<string name="app_name">K저널</string>' in s:
        p.write_text(s.replace('<string name="app_name">K저널</string>', '<string name="app_name">KJournal</string>'))
print('patched app name and version')
