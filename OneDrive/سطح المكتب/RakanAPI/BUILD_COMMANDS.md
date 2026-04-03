# 📦 أوامر البناء اليدوية

## iOS Build Commands

### المتطلبات:
- macOS (لبناء iOS لا بد من جهاز Mac)
- Xcode مثبت
- Flutter SDK مثبت
- CocoaPods مثبت

```bash
# 1. الانتقال إلى مجلد المشروع
cd flutter

# 2. تحديث المتعلقات
flutter pub get

# 3. بناء iOS Release
flutter build ios --release

# 4. تحديد الإصدار (اختياري)
flutter build ios --release --build-name=1.0.0 --build-number=1
```

### النتيجة:
- سيتم إنشاء مجلد: `flutter/build/ios/iphoneos/`
- يمكنك رفع التطبيق على App Store أو توزيعه عبر TestFlight

---

## Android Build Commands

### المتطلبات:
- JDK 11 أو أحدث
- Android SDK
- Flutter SDK

```bash
# 1. الانتقال إلى مجلد المشروع
cd flutter

# 2. تحديث المتعلقات
flutter pub get

# 3. بناء APK (لجهاز واحد)
flutter build apk --release

# 4. بناء AAB (لـ Google Play Store)
flutter build appbundle --release

# 5. بناء بأسماء مخصصة
flutter build apk --release --build-name=1.0.0 --build-number=1
flutter build appbundle --release --build-name=1.0.0 --build-number=1
```

### النتيجة:
- APK: `flutter/build/app/outputs/flutter-apk/app-release.apk`
- AAB: `flutter/build/app/outputs/bundle/release/app-release.aab`

---

## Windows EXE (جاهز بالفعل ✅)

**المسار:**
```
c:\Users\Admin\OneDrive\سطح المكتب\RakanAPI\RakanMaadid_WPF_NET8\bin\Release\publish\RakanMaadid.Wpf.exe
```

**لتشغيل من جديد:**
```powershell
cd "c:\Users\Admin\OneDrive\سطح المكتب\RakanAPI\RakanMaadid_WPF_NET8"
C:\Program Files\dotnet\dotnet.exe publish -c Release -o "./bin/Release/publish"
```

---

## GitHub Actions (بناء تلقائي 🤖)

تم إنشاء ملف: `.github/workflows/build_mobile.yml`

هذا سيبني تلقائياً iOS و Android كل مرة:
- تدفع كود إلى `main` أو `develop`
- تفتح Pull Request

**خطوات التفعيل:**
1. ادفع الملف إلى GitHub
2. اذهب إلى Actions في مستودعك
3. اختر `Build Mobile Apps`
4. ستجد المبنيات في Artifacts

---

## ملخص ✅

| المنصة | الحالة | المسار |
|--------|--------|--------|
| ✅ Windows EXE | جاهز | `bin/Release/publish/RakanMaadid.Wpf.exe` |
| 🍎 iOS | أوامر يدوية | بحاجة macOS |
| 🤖 iOS | تلقائي | GitHub Actions |
| 📱 Android APK | أوامر يدوية | `build/app/outputs/flutter-apk/` |
| 📦 Android AAB | تلقائي | GitHub Actions |
