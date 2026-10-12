from pathlib import Path
import shutil, re
src=Path('/home/ubuntu/kjournal_dp31_verify')
root=Path('/home/ubuntu/kjournal_dp4_verify')
if root.exists(): shutil.rmtree(root)
shutil.copytree(src, root)
yml=root/'apktool.yml'
s=yml.read_text()
s=re.sub(r'versionCode: \d+', 'versionCode: 5010', s, count=1)
s=re.sub(r'versionName: .*', 'versionName: 5 DP4', s, count=1)
yml.write_text(s)
for rel in ['smali/xh0.smali','smali/pi0.smali']:
 p=root/rel
 if p.exists(): p.write_text(p.read_text().replace('KJournal 5 DP3.1','KJournal 5 DP4').replace('KJournal 5 DP3','KJournal 5 DP4'))
repls={
 'smali/m43.smali': {'"onset"':'"발현"','"comeup"':'"상승"','"peak"':'"정점"','"offset"':'"감소"','"total: "':'"총 지속 시간: "','"after effects: "':'"잔여 효과: "'},
 'smali/l71.smali': {'"threshold "':'"기준 "'},
 'smali/lb0.smali': {'"Estimate"':'"추정"'},
 'smali/fk.smali': {'"Now"':'"지금"'},
}
for rel,rs in repls.items():
 p=root/rel
 if p.exists():
  t=p.read_text()
  for a,b in rs.items(): t=t.replace(a,b)
  p.write_text(t)
print(root)
