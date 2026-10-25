from pathlib import Path
import shutil, re, subprocess

base = Path('/home/ubuntu/kjournal_pb4_final_decode')
root = Path('/home/ubuntu/kjournal_pb6_verify')
if root.exists(): shutil.rmtree(root)
shutil.copytree(base, root)
yml = root / 'apktool.yml'
s = yml.read_text()
s = re.sub(r'versionCode: \d+', 'versionCode: 5016', s, count=1)
s = re.sub(r'versionName: .*', 'versionName: 5 PB6', s, count=1)
yml.write_text(s)
manifest = root / 'AndroidManifest.xml'
ms = manifest.read_text().replace('android:foregroundServiceType="specialUse"', 'android:foregroundServiceType="dataSync"')
manifest.write_text(ms)
repls = {
 'smali/d53.smali': [('const-string v9, " ingestion"','const-string v9, " 섭취"'),('const-string v8, " ingestions"','const-string v8, " 섭취 기록"')],
 'smali/op0.smali': [('const-string v2, " ingestion"','const-string v2, " 섭취"'),('const-string v2, " ingestions"','const-string v2, " 섭취 기록"')],
 'smali/com/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService.smali': [('const-string p0, "Stop"','const-string p0, "중지"')],
 'smali/r20.smali': [('const-string v5, " years"','const-string v5, "년 전"'),('const-string v5, " months"','const-string v5, "개월 전"'),('const-string v5, " weeks"','const-string v5, "주 전"'),('const-string v5, " days"','const-string v5, "일 전"'),('const-string v0, " hours"','const-string v0, "시간 전"'),('const-string v5, " minutes"','const-string v5, "분 전"')],
 'smali/s33.smali': [('const-string v3, "Yesterday"','const-string v3, "어제"'),('const-string v3, "Tomorrow"','const-string v3, "내일"'),('const-string v0, "Start"','const-string v0, "시작"'),('const-string v0, "End"','const-string v0, "종료"')],
}
for rel, pairs in repls.items():
    p = root / rel
    if p.exists():
        t = p.read_text()
        for old, new in pairs: t = t.replace(old, new)
        p.write_text(t)
fg = root / 'smali/hq.smali'
if fg.exists():
    t = fg.read_text()
    t = t.replace('const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x0', 'const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x1')
    t = t.replace('const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/high16 v1, 0x40000000', 'const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x1')
    fg.write_text(t)
compile_dir = Path('/home/ubuntu/ota_pb6_compile')
dex_dir = Path('/home/ubuntu/ota_pb6_dex')
for p in (compile_dir, dex_dir):
    if p.exists(): shutil.rmtree(p)
    p.mkdir(parents=True)
jar = '/home/ubuntu/android_sdk/platforms/android-35/android.jar'
subprocess.run(['javac','-source','8','-target','8','-cp',jar,'-d',str(compile_dir),'/home/ubuntu/ota_kjournal_src/OtaUpdater.java','/home/ubuntu/ota_kjournal_src/OtaFileProvider.java'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/d8','--min-api','28','--output',str(dex_dir),*map(str, compile_dir.glob('**/*.class'))], check=True)
unsigned = Path('/home/ubuntu/kjournal_pb6_unsigned.apk')
if unsigned.exists(): unsigned.unlink()
subprocess.run(['java','-jar','/home/ubuntu/android_tools/apktool.jar','b',str(root),'-o',str(unsigned),'-f'], check=True)
subprocess.run(['zip','-q','-d',str(unsigned),'classes3.dex'], check=True)
shutil.copy2(dex_dir/'classes.dex', '/home/ubuntu/classes3.dex')
subprocess.run(['zip','-q','-j',str(unsigned),'/home/ubuntu/classes3.dex'], check=True)
aligned = Path('/home/ubuntu/kjournal_pb6_aligned.apk')
out = Path('/home/ubuntu/KJournal-5-PB6.apk')
for p in (aligned, out):
    if p.exists(): p.unlink()
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/zipalign','-f','4',str(unsigned),str(aligned)], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/apksigner','sign','--key','/home/ubuntu/android_tools/testkey/testkey.pk8','--cert','/home/ubuntu/android_tools/testkey/testkey.x509.pem','--out',str(out),str(aligned)], check=True)
print(out)
print('versionCode=5016 versionName=5 PB6')
print('download to public Downloads/KJournalUpdates and open Samsung My Files')
