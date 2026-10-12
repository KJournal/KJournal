from pathlib import Path
import shutil, subprocess, re

src = Path('/home/ubuntu/upload_pb6_decode')
root = Path('/home/ubuntu/pb6_notification_fix_work')
for p in (root, Path('/home/ubuntu/pb6_notification_fix_unsigned.apk'), Path('/home/ubuntu/pb6_notification_fix_aligned.apk'), Path('/home/ubuntu/KJournal-5-PB6.apk')):
    if p.is_dir(): shutil.rmtree(p)
    elif p.exists(): p.unlink()
shutil.copytree(src, root)

# Keep PB6 identity in package metadata.
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode:\s*\d+', 'versionCode: 5016', s, count=1)
s = re.sub(r'versionName:\s*.*', 'versionName: 5 PB6', s, count=1)
yml.write_text(s)

# Android 14/15/16 requires the matching runtime permission for dataSync FGS.
manifest = root / 'AndroidManifest.xml'
ms = manifest.read_text()
perm = '<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC"/>'
if perm not in ms:
    ms = ms.replace('<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>', '<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>\n    ' + perm)
manifest.write_text(ms)

# Normalize any visible PB3/PB4/PB5 labels in resource XML and smali constants.
for p in list((root / 'res').rglob('*.xml')) + list(root.glob('smali*/**/*.smali')):
    try:
        t = p.read_text()
    except UnicodeDecodeError:
        continue
    nt = re.sub(r'5\s+PB[1-5](?:\.\d+)?', '5 PB6', t, flags=re.I)
    nt = re.sub(r'KJournal-5-PB[1-5](?:\.\d+)?', 'KJournal-5-PB6', nt, flags=re.I)
    if nt != t:
        p.write_text(nt)

# Android 16 validates Paint#getTextBounds ranges strictly. The Korean label
# "지금" has two UTF-16 code units, so the original end index 3 is invalid.
fk = root / 'smali/fk.smali'
if fk.exists():
    t = fk.read_text()
    old = 'const/4 v8, 0x3\n\n    .line 151\n    const-string v9, "\\uc9c0\\uae08"'
    new = 'const/4 v8, 0x2\n\n    .line 151\n    const-string v9, "\\uc9c0\\uae08"'
    if old not in t:
        raise RuntimeError('fk.e invalid range pattern not found')
    fk.write_text(t.replace(old, new, 1))

subprocess.run(['java','-jar','/home/ubuntu/android_tools/apktool.jar','b',str(root),'-o','/home/ubuntu/pb6_notification_fix_unsigned.apk','-f'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/zipalign','-f','4','/home/ubuntu/pb6_notification_fix_unsigned.apk','/home/ubuntu/pb6_notification_fix_aligned.apk'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/apksigner','sign','--key','/home/ubuntu/android_tools/testkey/testkey.pk8','--cert','/home/ubuntu/android_tools/testkey/testkey.x509.pem','--out','/home/ubuntu/KJournal-5-PB6.apk','/home/ubuntu/pb6_notification_fix_aligned.apk'], check=True)
print('/home/ubuntu/KJournal-5-PB6.apk')
