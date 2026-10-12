from pathlib import Path
p=Path('/home/ubuntu/ota_kjournal_src/OtaUpdater.java')
s=p.read_text()
bad='    private static boolean isAllowedUpdateUrl(String url) {\\n        return url.startsWith("http://budo.kro.kr:1231/api/public/dl/") || url.startsWith("https://budo.kro.kr:1231/api/public/dl/");\\n    }\\n\\n    private static int currentVersionCode(Context c) {'
good='''    private static boolean isAllowedUpdateUrl(String url) {
        return url.startsWith("http://budo.kro.kr:1231/api/public/dl/") || url.startsWith("https://budo.kro.kr:1231/api/public/dl/");
    }

    private static int currentVersionCode(Context c) {'''
if bad not in s:
    raise SystemExit('bad block not found')
p.write_text(s.replace(bad,good,1))
