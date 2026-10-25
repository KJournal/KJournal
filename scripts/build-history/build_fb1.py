from pathlib import Path
import shutil, re, subprocess

base = Path('/home/ubuntu/fb1_original_decode')
root = Path('/home/ubuntu/fb1_work')
if root.exists(): shutil.rmtree(root)
shutil.copytree(base, root)
# Merge PB6-only OTA classes onto the newer original.
pb6 = Path('/home/ubuntu/pb6_decode_tmp')
for source_dir, target_dir, prefix in [
    (pb6 / 'smali_classes3/com/isaakhanimann/journal/ota', root / 'smali_classes3/com/isaakhanimann/journal/ota', 'Ota'),
]:
    target_dir.mkdir(parents=True, exist_ok=True)
    for f in source_dir.glob(prefix + '*.smali'):
        shutil.copy2(f, target_dir / f.name)
# The XAPK keeps Compose/DataStore native libraries in the arm64 split. A
# standalone APK must carry those .so files or it can crash during startup.
split_apk = Path('/home/ubuntu/fb1_xapk_extract/split_config.arm64_v8a.apk')
native_root = root / 'lib' / 'arm64-v8a'
native_root.mkdir(parents=True, exist_ok=True)
subprocess.run(['unzip','-o','-j',str(split_apk),'lib/arm64-v8a/libandroidx.graphics.path.so','-d',str(native_root)], check=True, stdout=subprocess.DEVNULL)
subprocess.run(['unzip','-o','-j',str(split_apk),'lib/arm64-v8a/libdatastore_shared_counter.so','-d',str(native_root)], check=True, stdout=subprocess.DEVNULL)
yml = root / 'apktool.yml'
ys = yml.read_text()
ys = re.sub(r'versionCode:\s*\d+', 'versionCode: 6001', ys, count=1)
ys = re.sub(r'versionName:\s*.*', 'versionName: 6 Prototype', ys, count=1)
yml.write_text(ys)
old_pkg = 'com.isaakhanimann.journal'
new_pkg = 'com.isaakhanimann.journal.kr4812.premiumtest'
manifest = root / 'AndroidManifest.xml'
ms = manifest.read_text()
# Standalone APK: do not rely on split/native extraction behavior on Android 16.
ms = ms.replace(' android:extractNativeLibs="false"', '')
ms = ms.replace(' android:requiredSplitTypes="base__abi,base__density"', '')
ms = ms.replace(' android:splitTypes=""', '')
ms = ms.replace('package="' + old_pkg + '"', 'package="' + new_pkg + '"')
ms = ms.replace(' android:requiredSplitTypes="base__abi,base__density"', '')
ms = ms.replace(' android:splitTypes=""', '')
ms = ms.replace(old_pkg + '.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION', new_pkg + '.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION')
ms = ms.replace('android:authorities="' + old_pkg + '.androidx-startup"', 'android:authorities="' + new_pkg + '.androidx-startup"')
ms = ms.replace('android:foregroundServiceType="specialUse"', 'android:foregroundServiceType="dataSync"')
ms = ms.replace('android:name="com.pairip.application.Application"', 'android:name="com.isaakhanimann.journal.di.JournalApplication" android:networkSecurityConfig="@xml/ota_network_security_config"')
ms = re.sub(r'\n\s*<meta-data android:name="com.android.vending.splits.required"[^>]*/>', '', ms)
ms = re.sub(r'\n\s*<meta-data android:name="com.android.vending.splits"[^>]*/>', '', ms)
ms = re.sub(r'\n\s*<meta-data android:name="com.android.vending.derived.apk.id"[^>]*/>', '', ms)
ms = ms.replace('<uses-permission android:name="android.permission.FOREGROUND_SERVICE_SPECIAL_USE"/>', '<uses-permission android:name="android.permission.FOREGROUND_SERVICE_SPECIAL_USE"/>')
provider = '''\n        <provider android:authorities="com.isaakhanimann.journal.kr4812.premiumtest.ota.provider" android:exported="false" android:grantUriPermissions="true" android:name="com.isaakhanimann.journal.ota.OtaFileProvider"/>\n'''
ms = ms.replace('    </application>', provider + '    </application>')
manifest.write_text(ms)

# Keep a startup exception from killing the process before MainActivity opens.
# This is especially important on newer Android releases where provider and
# native initialization ordering is stricter.
safe = root / 'smali/com/isaakhanimann/journal/di/SafeJournalApplication.smali'
safe.write_text('''.class public Lcom/isaakhanimann/journal/di/SafeJournalApplication;\n.super Lcom/isaakhanimann/journal/di/JournalApplication;\n.source "SafeJournalApplication.kt"\n\n.method public constructor <init>()V\n    .locals 0\n    invoke-direct {p0}, Lcom/isaakhanimann/journal/di/JournalApplication;-><init>()V\n    return-void\n.end method\n\n.method public onCreate()V\n    .locals 0\n    :try_start_0\n    invoke-super {p0}, Lcom/isaakhanimann/journal/di/JournalApplication;->onCreate()V\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catch_init\n    return-void\n\n    :catch_init\n    return-void\n.end method\n''')

# Preserve the established KJournal branding while using the latest original code/resources.
for p in [root / 'res/values/strings.xml']:
    if p.exists():
        t = p.read_text()
        t = re.sub(r'(<string name="app_name"[^>]*>).*?(</string>)', r'\1KJournal\2', t, count=1)
        p.write_text(t)

# Apply known visible English fixes from the KJournal patches where the latest build has the same literals.
repls = {
 'smali/d53.smali': [('const-string v9, " ingestion"','const-string v9, " 섭취"'),('const-string v8, " ingestions"','const-string v8, " 섭취 기록"')],
 'smali/op0.smali': [('const-string v2, " ingestion"','const-string v2, " 섭취"'),('const-string v2, " ingestions"','const-string v2, " 섭취 기록"')],
 'smali/com/isaakhanimann/journal/ui/tabs/journal/experience/timeline/notification/TimelineNotificationService.smali': [('const-string p0, "Stop"','const-string p0, "중지"')],
 'smali/s33.smali': [('const-string v3, "Yesterday"','const-string v3, "어제"'),('const-string v3, "Tomorrow"','const-string v3, "내일"'),('const-string v0, "Start"','const-string v0, "시작"'),('const-string v0, "End"','const-string v0, "종료"')],
}
for rel, pairs in repls.items():
    p = root / rel
    if p.exists():
        t = p.read_text()
        for old, new in pairs: t = t.replace(old, new)
        p.write_text(t)

# Android 12+ foreground service type must agree with the manifest.
fg = root / 'smali/hq.smali'
if fg.exists():
    t = fg.read_text()
    t = t.replace('const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x0', 'const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x1')
    t = t.replace('const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/high16 v1, 0x40000000', 'const v0, 0xafc9\n\n    .line 2\n    .line 3\n    .line 4\n    const/4 v1, 0x1')
    fg.write_text(t)

xml = root / 'res/xml/ota_network_security_config.xml'
xml.parent.mkdir(parents=True, exist_ok=True)
xml.write_text('''<?xml version="1.0" encoding="utf-8"?>\n<network-security-config>\n    <base-config cleartextTrafficPermitted="false" />\n    <domain-config cleartextTrafficPermitted="true">\n        <domain includeSubdomains="false">budo.kro.kr</domain>\n    </domain-config>\n</network-security-config>\n''')

compile_dir = Path('/home/ubuntu/fb1_ota_compile')
dex_dir = Path('/home/ubuntu/fb1_ota_dex')
for p in (compile_dir, dex_dir):
    if p.exists(): shutil.rmtree(p)
    p.mkdir(parents=True)
jar = '/home/ubuntu/android_sdk/platforms/android-35/android.jar'
subprocess.run(['javac','-source','8','-target','8','-cp',jar,'-d',str(compile_dir),'/home/ubuntu/ota_kjournal_src/OtaUpdater.java','/home/ubuntu/ota_kjournal_src/OtaFileProvider.java'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/d8','--min-api','32','--output',str(dex_dir),*map(str, compile_dir.glob('**/*.class'))], check=True)
unsigned = Path('/home/ubuntu/fb1_unsigned.apk')
if unsigned.exists(): unsigned.unlink()
subprocess.run(['java','-jar','/home/ubuntu/android_tools/apktool.jar','b',str(root),'-o',str(unsigned),'-f'], check=True)
aligned = Path('/home/ubuntu/fb1_aligned.apk')
out = Path('/home/ubuntu/KJournal-5-FB1.apk')
for p in (aligned, out):
    if p.exists(): p.unlink()
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/zipalign','-f','4',str(unsigned),str(aligned)], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/apksigner','sign','--key','/home/ubuntu/android_tools/testkey/testkey.pk8','--cert','/home/ubuntu/android_tools/testkey/testkey.x509.pem','--out',str(out),str(aligned)], check=True)
print(out)
print('package=' + new_pkg + ' versionCode=6001 versionName=6 Prototype')
