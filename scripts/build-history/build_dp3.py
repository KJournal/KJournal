from pathlib import Path
import re, shutil
src = Path('/home/ubuntu/kjournal_dp2_nas_decode')
root = Path('/home/ubuntu/kjournal_dp3_verify')
if root.exists(): shutil.rmtree(root)
shutil.copytree(src, root)
manifest = root / 'AndroidManifest.xml'
s = manifest.read_text()
old = 'android:foregroundServiceType="" android:name="com.isaakhanimann.journal.ui.tabs.journal.experience.timeline.notification.TimelineNotificationService"'
new = 'android:foregroundServiceType="specialUse" android:name="com.isaakhanimann.journal.ui.tabs.journal.experience.timeline.notification.TimelineNotificationService"'
if old not in s: raise SystemExit('foreground service declaration not found')
s = s.replace(old, new)
# Use an explicit, safe service subtype declaration for Android 14+.
if 'android.permission.FOREGROUND_SERVICE_SPECIAL_USE' not in s:
    raise SystemExit('special-use permission missing')
manifest.write_text(s)
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5007', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 DP3', s, count=1)
yml.write_text(s)
for rel in ['smali/xh0.smali', 'smali/pi0.smali']:
    p = root / rel
    s = p.read_text().replace('KJournal 5 DP2', 'KJournal 5 DP3')
    p.write_text(s)
print(root)
print('versionCode=5007 versionName=5 DP3')
print('foregroundServiceType=specialUse')
