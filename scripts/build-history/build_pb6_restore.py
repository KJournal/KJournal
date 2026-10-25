from pathlib import Path
import shutil
import subprocess

src = Path('/home/ubuntu/pb6_decode_tmp')
root = Path('/home/ubuntu/pb6_restore_work')
for p in (root, Path('/home/ubuntu/pb6_restore_unsigned.apk'), Path('/home/ubuntu/pb6_restore_aligned.apk'), Path('/home/ubuntu/KJournal-5-FB1.apk')):
    if p.is_dir(): shutil.rmtree(p)
    elif p.exists(): p.unlink()
shutil.copytree(src, root)
yml = root / 'apktool.yml'
s = yml.read_text()
s = s.replace('versionCode: 5016', 'versionCode: 5024')
s = s.replace('versionName: 5 PB6', 'versionName: 5 FB1.7')
yml.write_text(s)
subprocess.run(['java','-jar','/home/ubuntu/android_tools/apktool.jar','b',str(root),'-o','/home/ubuntu/pb6_restore_unsigned.apk','-f'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/zipalign','-f','4','/home/ubuntu/pb6_restore_unsigned.apk','/home/ubuntu/pb6_restore_aligned.apk'], check=True)
subprocess.run(['/home/ubuntu/android_sdk/build-tools/35.0.0/apksigner','sign','--key','/home/ubuntu/android_tools/testkey/testkey.pk8','--cert','/home/ubuntu/android_tools/testkey/testkey.x509.pem','--out','/home/ubuntu/KJournal-5-FB1.apk','/home/ubuntu/pb6_restore_aligned.apk'], check=True)
print('/home/ubuntu/KJournal-5-FB1.apk')
print('versionCode=5024 versionName=5 FB1.7; base=previous KJournal PB6')
