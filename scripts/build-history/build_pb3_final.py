from pathlib import Path
import shutil
import re

src = Path('/home/ubuntu/kjournal_pb1_final_decode')
root = Path('/home/ubuntu/kjournal_pb3_verify')
if root.exists():
    shutil.rmtree(root)
shutil.copytree(src, root)

yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5013', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 PB3', s, count=1)
yml.write_text(s)

# Visible UI translations from the supplied screenshots.
for p in root.glob('smali*/**/*.smali'):
    text = p.read_text()
    new = text.replace('KJournal 5 PB1', 'KJournal 5 PB3')
    if new != text:
        p.write_text(new)

# The visible title suffix shown as “... ingestion”. Keep database/navigation keys intact.
p = root / 'smali/op0.smali'
s = p.read_text()
if 'const-string v2, " ingestion"' not in s:
    raise SystemExit('visible ingestion title literal not found')
p.write_text(s.replace('const-string v2, " ingestion"', 'const-string v2, " 섭취"'))

# Translate the app-owned notification action label. “Stop” is not the Samsung system UI label.
p = root / 'smali/com/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService.smali'
s = p.read_text()
if 'const-string p0, "Stop"' not in s:
    raise SystemExit('notification Stop literal not found')
p.write_text(s.replace('const-string p0, "Stop"', 'const-string p0, "중지"'))

# Start while the activity is foreground; this avoids Android 11+ FGS start crashes.
for rel in ['smali/sq2.smali', 'smali/e75.smali']:
    p = root / rel
    s = p.read_text()
    old = 'startForegroundService(Landroid/content/Intent;)Landroid/content/ComponentName;'
    if old not in s:
        raise SystemExit(f'foreground start call not found in {rel}')
    p.write_text(s.replace(old, 'startService(Landroid/content/Intent;)Landroid/content/ComponentName;'))

print(root)
print('versionCode=5013 versionName=5 PB3')
print('translated visible ingestion title and notification action; changed notification startup to startService')
