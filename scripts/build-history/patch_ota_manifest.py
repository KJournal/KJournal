from pathlib import Path
p=Path('/home/ubuntu/ota_kjournal_decode/AndroidManifest.xml')
s=p.read_text()
needle='android:label="KJournal"'
if 'android:networkSecurityConfig="@xml/ota_network_security_config"' not in s:
    s=s.replace(needle, needle+' android:networkSecurityConfig="@xml/ota_network_security_config"',1)
p.write_text(s)
