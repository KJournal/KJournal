package com.isaakhanimann.journal.ota;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.pm.PackageInfo;
import android.graphics.Color;
import android.graphics.Typeface;
import android.net.Uri;
import android.provider.MediaStore;
import android.os.Build;
import android.os.Environment;
import android.os.Handler;
import android.os.Looper;
import android.view.Gravity;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONObject;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.util.Locale;

public final class OtaUpdater {
    private static final String VERSION_URL = "https://kjournal.github.io/kjournal-site/ota/version.json";
    private static final String AUTH_SUFFIX = ".ota.provider";
    private static final int TIMEOUT_MS = 10000;
    private OtaUpdater() {}

    public static void check(final Context context) {
        if (!(context instanceof Activity)) return;
        final Activity activity = (Activity) context;
        new Thread(() -> {
            HttpURLConnection c = null;
            try {
                JSONObject json = getJson(VERSION_URL);
                final int remoteCode = json.optInt("versionCode", 0);
                final int localCode = currentVersionCode(context);
                final String remoteName = json.optString("versionName", "새 버전");
                final String url = json.optString("downloadUrl", "");
                final String changelog = json.optString("changelog", "버그 수정 및 안정성 개선");
                final String sha256 = json.optString("sha256", "").trim();
                if (remoteCode <= 0 || remoteCode <= localCode || !isAllowedUpdateUrl(url)) return;
                new Handler(Looper.getMainLooper()).post(() -> {
                    if (!activity.isFinishing() && (Build.VERSION.SDK_INT < 17 || !activity.isDestroyed()))
                        showUpdateDialog(activity, remoteName, url, changelog, sha256, localCode, remoteCode);
                });
            } catch (Throwable ignored) { }
        }, "ota-version-check").start();
    }

    private static boolean isAllowedUpdateUrl(String url) {
        return url != null && url.startsWith("https://kjournal.github.io/kjournal-site/");
    }

    private static int currentVersionCode(Context c) {
        try {
            PackageInfo p = c.getPackageManager().getPackageInfo(c.getPackageName(), 0);
            return Build.VERSION.SDK_INT >= 28 ? (int)p.getLongVersionCode() : p.versionCode;
        } catch (Throwable e) { return 0; }
    }

    private static JSONObject getJson(String address) throws Exception {
        HttpURLConnection c = (HttpURLConnection)new URL(address).openConnection();
        c.setConnectTimeout(TIMEOUT_MS); c.setReadTimeout(TIMEOUT_MS); c.setRequestMethod("GET");
        c.setRequestProperty("Accept", "application/json"); c.setRequestProperty("Cache-Control", "no-cache");
        if (c.getResponseCode() < 200 || c.getResponseCode() >= 300) throw new IOException("http");
        InputStream in = new BufferedInputStream(c.getInputStream()); ByteArrayOutputStream out = new ByteArrayOutputStream();
        byte[] b = new byte[4096]; int n; while ((n = in.read(b)) != -1) out.write(b, 0, n);
        in.close(); c.disconnect(); return new JSONObject(out.toString("UTF-8"));
    }

    private static TextView text(Context context, String value, int size, int color, boolean bold) {
        TextView t = new TextView(context);
        t.setText(value); t.setTextSize(size); t.setTextColor(color); t.setPadding(0, 5, 0, 5);
        if (bold) t.setTypeface(Typeface.DEFAULT, Typeface.BOLD); return t;
    }

    private static void showUpdateDialog(final Activity a, String name, final String url, String log, final String hash, int local, int remote) {
        final int white = Color.WHITE, muted = Color.rgb(190, 205, 215), cyan = Color.rgb(80, 210, 255);
        LinearLayout box = new LinearLayout(a); box.setOrientation(LinearLayout.VERTICAL); box.setPadding(56, 34, 56, 22); box.setBackgroundColor(Color.rgb(18, 29, 38));
        TextView badge = text(a, "  NEW UPDATE  ", 12, Color.rgb(10, 30, 40), true); badge.setBackgroundColor(cyan); badge.setGravity(Gravity.CENTER); box.addView(badge, new LinearLayout.LayoutParams(-1, 42));
        TextView title = text(a, "KJournal 업데이트", 24, white, true); title.setPadding(0, 24, 0, 2); box.addView(title);
        box.addView(text(a, "새로운 버전이 준비됐어요", 15, muted, false));
        TextView versions = text(a, "현재  v" + local + "   →   최신  v" + remote + "  ·  " + name, 14, cyan, true); versions.setPadding(0, 18, 0, 14); box.addView(versions);
        ScrollView scroll = new ScrollView(a); TextView notes = text(a, log, 15, white, false); scroll.addView(notes); box.addView(scroll, new LinearLayout.LayoutParams(-1, 120));
        AlertDialog dialog = new AlertDialog.Builder(a).setView(box).setNegativeButton("나중에", null).setPositiveButton("지금 업데이트", (d,w) -> downloadAndInstall(a, url, hash)).create();
        dialog.setOnShowListener(d -> {
            if (dialog.getWindow() != null) dialog.getWindow().setBackgroundDrawable(new android.graphics.drawable.ColorDrawable(Color.rgb(18, 29, 38)));
            dialog.getButton(AlertDialog.BUTTON_POSITIVE).setTextColor(cyan);
            dialog.getButton(AlertDialog.BUTTON_NEGATIVE).setTextColor(muted);
            android.view.View buttons = dialog.getButton(AlertDialog.BUTTON_POSITIVE).getParent() instanceof android.view.View
                    ? (android.view.View) dialog.getButton(AlertDialog.BUTTON_POSITIVE).getParent() : null;
            if (buttons != null) buttons.setBackgroundColor(Color.rgb(18, 29, 38));
        });
        dialog.show();
    }

    private static void downloadAndInstall(final Activity a, final String address, final String expected) {
        Toast.makeText(a, "KJournal 업데이트를 준비하고 있어요.", Toast.LENGTH_SHORT).show();
        new Thread(() -> { File target = null; try {
            HttpURLConnection c = (HttpURLConnection)new URL(address).openConnection(); c.setConnectTimeout(15000); c.setReadTimeout(60000); c.setRequestMethod("GET");
            if (c.getResponseCode() < 200 || c.getResponseCode() >= 300) throw new IOException("download");
            File dir = a.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS); if (dir == null) throw new IOException("storage");
            if (!dir.exists() && !dir.mkdirs()) throw new IOException("mkdir"); target = new File(dir, "KJournal-5-FB1.apk");
            InputStream in = new BufferedInputStream(c.getInputStream()); FileOutputStream out = new FileOutputStream(target); byte[] b = new byte[8192]; int n;
            while ((n = in.read(b)) != -1) out.write(b, 0, n); in.close(); out.close(); c.disconnect();
            if (!expected.isEmpty() && !expected.equalsIgnoreCase(sha256(target))) throw new IOException("sha256");
            final File apk = target;
            final Uri publicUri = copyToPublicDownloads(a, apk);
            new Handler(Looper.getMainLooper()).post(() -> openMyFiles(a, publicUri));
        } catch (Throwable e) { if (target != null) target.delete(); new Handler(Looper.getMainLooper()).post(() -> Toast.makeText(a, "업데이트를 준비하지 못했어요. 네트워크를 확인해 주세요.", Toast.LENGTH_LONG).show()); }
        }, "ota-download").start();
    }

    private static String sha256(File f) throws Exception { MessageDigest md = MessageDigest.getInstance("SHA-256"); InputStream in = new BufferedInputStream(new FileInputStream(f)); byte[] b = new byte[8192]; int n; while ((n = in.read(b)) != -1) md.update(b, 0, n); in.close(); StringBuilder s = new StringBuilder(); for (byte x : md.digest()) s.append(String.format(Locale.US, "%02x", x)); return s.toString(); }

    private static Uri copyToPublicDownloads(Context context, File source) throws Exception {
        if (Build.VERSION.SDK_INT < 29) return null;
        ContentValues values = new ContentValues();
        values.put(MediaStore.MediaColumns.DISPLAY_NAME, "KJournal-5-FB1.apk");
        values.put(MediaStore.MediaColumns.MIME_TYPE, "application/vnd.android.package-archive");
        values.put(MediaStore.MediaColumns.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS + "/KJournalUpdates");
        values.put(MediaStore.MediaColumns.IS_PENDING, 1);
        ContentResolver resolver = context.getContentResolver();
        Uri uri = resolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values);
        if (uri == null) throw new IOException("downloads");
        try (InputStream in = new BufferedInputStream(new FileInputStream(source)); OutputStream out = resolver.openOutputStream(uri)) {
            if (out == null) throw new IOException("downloads-output");
            byte[] b = new byte[8192]; int n; while ((n = in.read(b)) != -1) out.write(b, 0, n);
        }
        ContentValues done = new ContentValues(); done.put(MediaStore.MediaColumns.IS_PENDING, 0); resolver.update(uri, done, null, null);
        return uri;
    }

    private static void openMyFiles(Activity a, Uri uri) {
        try {
            Intent files = a.getPackageManager().getLaunchIntentForPackage("com.sec.android.app.myfiles");
            if (files != null) {
                files.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
                a.startActivity(files);
                Toast.makeText(a, "내 파일 > 내장 저장공간 > Download > KJournalUpdates에서 KJournal-5-FB1.apk를 눌러 설치하세요.", Toast.LENGTH_LONG).show();
                return;
            }
            if (uri != null) {
                Intent view = new Intent(Intent.ACTION_VIEW).setDataAndType(uri, "application/vnd.android.package-archive");
                view.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_ACTIVITY_NEW_TASK); a.startActivity(view); return;
            }
            Toast.makeText(a, "다운로드가 완료됐어요. Download/KJournalUpdates 폴더에서 KJournal-5-FB1.apk를 열어 주세요.", Toast.LENGTH_LONG).show();
        } catch (Throwable e) { Toast.makeText(a, "내 파일 앱을 열지 못했어요. Download/KJournalUpdates에서 KJournal-5-FB1.apk를 열어 주세요.", Toast.LENGTH_LONG).show(); }
    }

    private static void installApkDirectly(Activity a, File apk) {
        try {
            Uri uri = Uri.parse("content://com.isaakhanimann.journal.kr4812.premiumtest.ota.provider/" + Uri.encode(apk.getName()));
            Intent installer = new Intent(Intent.ACTION_VIEW);
            installer.setDataAndType(uri, "application/vnd.android.package-archive");
            installer.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_ACTIVITY_NEW_TASK);
            a.startActivity(installer);
        } catch (Throwable e) {
            Toast.makeText(a, "설치 화면을 열지 못했어요. 삼성의 알 수 없는 출처 설치 허용을 확인해 주세요.", Toast.LENGTH_LONG).show();
        }
    }

}
