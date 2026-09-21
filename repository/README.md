# GitReleaseLab

## Repository

<div dir="rtl">

به‌صورت پیش‌فرض، <span dir="ltr">Git</span> در یک دایرکتوری تعریف نشده است و فایل‌های آن دایرکتوری را ردیابی نمی‌کند.

اگر به‌صورت محلی (<span dir="ltr">Local</span>) کار می‌کنیم، با استفاده از دستور زیر می‌توانیم یک <span dir="ltr">Repository</span> جدید ایجاد کنیم:

</div>

```bash
git init
```

<div dir="rtl">

با اجرای این دستور، یک پوشه‌ی مخفی به نام `.git` ایجاد می‌شود.

پوشه‌ی `.git` مانند یک پایگاه داده برای <span dir="ltr">Repository</span> عمل می‌کند و اطلاعات مربوط به تاریخچه‌ی <span dir="ltr">Commit</span>ها، <span dir="ltr">Branch</span>ها، تنظیمات <span dir="ltr">Repository</span> و سایر اطلاعات موردنیاز <span dir="ltr">Git</span> را نگهداری می‌کند.

</div>

## Working Tree

<div dir="rtl">

هر <span dir="ltr">Git Repository</span> از چند بخش اصلی تشکیل شده است که <span dir="ltr">Working Tree</span> یکی از آن‌هاست.

<span dir="ltr">Working Tree</span> شامل فایل‌های پروژه در وضعیت فعلی آن‌ها است؛ یعنی فایل‌هایی که در حال حاضر روی آن‌ها کار می‌کنیم و ممکن است تغییراتی در آن‌ها ایجاد شده باشد.

</div>

## Staging Area

<div dir="rtl">

یکی دیگر از بخش‌های مهم <span dir="ltr">Git Repository</span>، بخش <span dir="ltr">Staging Area</span> است.

وقتی روی فایل‌های موجود در <span dir="ltr">Working Tree</span> تغییراتی اعمال می‌کنیم یا فایل جدیدی به پروژه اضافه می‌کنیم، می‌توانیم تغییرات موردنظر را برای ثبت شدن آماده کنیم.

فایل‌ها و تغییراتی که برای <span dir="ltr">commit</span> بعدی انتخاب و آماده شده‌اند، در <span dir="ltr">Staging Area</span> قرار می‌گیرند.

برای اضافه کردن یک فایل به <span dir="ltr">Staging Area</span> می‌توان از دستور زیر استفاده کرد:

</div>

```bash
git add <file-name>
```

<div dir="rtl">

برای اضافه کردن تمام تغییرات می‌توان از دستور زیر استفاده کرد:

</div>

```bash
git add -A
```
## Commit / Snapshot

<div dir="rtl">

بعد از اینکه تغییرات فایل‌ها در <span dir="ltr">Staging Area</span> آماده‌ی ثبت شدند، با استفاده از دستور زیر می‌توان آن‌ها را ثبت کرد:

</div>

```bash
git commit -m "commit message"
```

<div dir="rtl">

با اجرای دستور <span dir="ltr">`git commit`</span>، از تغییراتی که در <span dir="ltr">Staging Area</span> قرار دارند یک <span dir="ltr">Snapshot</span> ایجاد می‌شود.

هر <span dir="ltr">Commit</span> در واقع یک نقطه‌ی ثبت‌شده از وضعیت پروژه است که می‌توان بعداً در تاریخچه‌ی <span dir="ltr">Git</span> به آن مراجعه کرد.

نکته: <span dir="ltr">Commit</span> فقط تغییراتی را ثبت می‌کند که قبلاً با دستور <span dir="ltr">`git add`</span> به <span dir="ltr">Staging Area</span> اضافه شده‌اند.

</div>

## Branch

<div dir="rtl">

از آنجایی که <span dir="ltr">Git</span> یک سیستم <span dir="ltr">Version Control</span> است، امکان کار روی چند شاخه یا <span dir="ltr">Branch</span> مختلف را فراهم می‌کند.

استفاده از <span dir="ltr">Branch</span> باعث می‌شود چند توسعه‌دهنده بتوانند هم‌زمان روی بخش‌های مختلف یک پروژه کار کنند. همچنین می‌توان برای توسعه‌ی یک قابلیت جدید، رفع یک مشکل یا آزمایش تغییرات، یک شاخه‌ی جداگانه ایجاد کرد.

شاخه‌ی اصلی پروژه معمولاً <span dir="ltr">`main`</span> یا در برخی پروژه‌های قدیمی‌تر <span dir="ltr">`master`</span> نام دارد.

برای ایجاد یک <span dir="ltr">Branch</span> جدید می‌توان از دستور زیر استفاده کرد:

</div>

```bash
git branch <branch-name>
```

<div dir="rtl">

برای رفتن به <span dir="ltr">Branch</span> موردنظر می‌توان از دستور زیر استفاده کرد:

</div>

```bash
git Checkout <branch-name>
```

<div dir="rtl">

هر <span dir="ltr">Branch</span> مسیر مستقلی از <span dir="ltr">Commit</span>ها را دنبال می‌کند. بنابراین <span dir="ltr">Commit</span>هایی که روی یک <span dir="ltr">Branch</span> انجام می‌شوند، مستقیماً شاخه‌های دیگر را تغییر نمی‌دهند.

در صورت نیاز، می‌توان تغییرات یک <span dir="ltr">Branch</span> را بعداً با استفاده از عملیاتی مانند <span dir="ltr">`merge`</span> وارد شاخه‌ی دیگری کرد.

</div>
## Merge

<div dir="rtl">

بعد از اینکه رفع باگ یا توسعه یک قابلیت در Branchها انجام و به وضعیت نهایی در آن شاخه رسیدیم برای اعمال کردن روی پروژه اصلی و ادغام آن با فایل های قبلی دستور Mergeوجود دارد که به این صورت استفاده می شود

</div>

```bash
git merge <Branch name>
```
## TAG

<div dir="rtl">

در گیت برای مشخص کردن یک Commit مهم یا برچسب از Tag استفاده میشود.

و همچنین برای نمایش نسخه های مختلف یک برنامه از آن نیز استفاده میشود و برای استفاده از آن:

</div>

```bash
git tag v1.0
```

<div dir="rtl">

یک Tag همواره به همان Commit اشاره میکند و با پیشروی برنامه تغییری نمی کند.

</div>

## HEAD
<div dir='rtl'>
در git برای دیدن log از دستور زیر استفاده می شود:
</div>

```bash
git log
```
<div dir='rtl'>
HEAD به اخرین  Snapshot موجود اشاره میکند
</div>

## .gitignore

<div dir="rtl">

Git فایل‌های موجود در <span dir="ltr">Working Tree</span> پروژه را مشاهده می‌کند، اما همه‌ی فایل‌ها لزوماً نباید تحت کنترل نسخه‌ی Git قرار بگیرند.

برخی از فایل‌های موجود در هر <span dir="ltr">Repository</span> به دلایلی مانند امنیت، فایل‌های موقت، فایل‌های تولیدشده توسط برنامه یا تنظیمات شخصی سیستم، نیازی به قرار گرفتن تحت کنترل Git و در دسترس قرار گرفتن برای سایر افراد پروژه ندارند.

برای مشخص کردن این فایل‌ها و پوشه‌ها، آن‌ها را در فایل `.gitignore` قرار می‌دهیم.

</div>

## Clean Working Tree

<div dir="rtl">

یکی از پرکاربردترین دستورات <span dir="ltr">Git</span> دستور زیر است:

</div>

```bash
git status
```

<div dir="rtl">

این دستور وضعیت کلی پروژه را نمایش می‌دهد؛ از جمله اینکه چه فایل‌هایی در <span dir="ltr">Staging Area</span> قرار دارند، چه فایل‌هایی تغییر کرده ولی هنوز <span dir="ltr">Stage</span> نشده‌اند و چه فایل‌هایی هنوز <span dir="ltr">Track</span> نشده‌اند.

هنگامی که همه‌ی تغییرات موردنظر ثبت شده باشند و فایل تغییرکرده یا جدیدی برای ثبت وجود نداشته باشد، در خروجی دستور <span dir="ltr">`git status`</span> عبارت زیر نمایش داده می‌شود:

</div>

```text
nothing to commit, working tree clean
```

<div dir="rtl">

این وضعیت به این معناست که <span dir="ltr">Working Tree</span> تمیز است و در حال حاضر تغییری برای <span dir="ltr">Commit</span> کردن وجود ندارد.

</div>

## SHA / Commit Hash

<div dir="rtl">

هر <span dir="ltr">Commit</span> علاوه بر <span dir="ltr">Commit Message</span> دارای یک شناسه یا <span dir="ltr">Commit Hash</span> است که آن را از سایر <span dir="ltr">Commit</span>ها متمایز می‌کند و این امکان را می‌دهد که با استفاده از آن به یک <span dir="ltr">Commit</span> مشخص دسترسی داشته باشیم.

در <span dir="ltr">Git</span> برای ایجاد این شناسه از الگوریتم‌های هش خانواده <span dir="ltr">SHA</span> استفاده می‌شود.

</div>

## DIFF
<div dir="rtl">
درستور diffبه تنهایی برای مقایسه دو برنامه استفاده می شود 
و در gitهم کاربرد دارد ولی چند حالت  برای استفاده از این دستور وجود دارد یکی از آنها :
</div>

```bash
git diff
```
<div dir="rtl">
این دستور وضعیت تغییرات stage نشده را با Working Tree
</div>

```bash
git diff --staged
```
<div dir="rtl">
دستور بالا تفاوت تغییرات Stageشده را با Working Tree نمایش می دهد به عبارتی نشان میدهد در Commit بعدی دقیقا چه اتفاقی می افتد
</div>

```bash
git diff <commit1> <commit2>
```
<div dir="rtl">
دستور بالا هم تفاوت دو Commit دلخواه را به کمک HashID آنها برسی میکند
</div>
# Git Release Lab

این پروژه یک تمرین عملی برای یادگیری چرخه کامل مدیریت نسخه و انتشار نرم‌افزار با Git است.

در این پروژه فرایند زیر انجام می‌شود:

```text
Source Code
    ↓
Git Repository
    ↓
Commit History
    ↓
Feature Branch
    ↓
Merge and Bugfix
    ↓
Release Commit
    ↓
Git Tag
    ↓
Release Package
    ↓
SHA256
    ↓
Release Verification
```

## هدف پروژه

هدف پروژه، یادگیری عملی مفاهیم زیر است:

- مدیریت Source Code با Git
- ایجاد Commitهای معنی‌دار
- توسعه قابلیت‌ها در Feature Branch
- ادغام Branchها
- آماده‌سازی نسخه نهایی
- استفاده از Semantic Versioning
- ایجاد Annotated Tag
- ساخت بسته Release از یک Tag مشخص
- تولید SHA256 برای بسته انتشار
- بررسی سلامت و اصالت بسته Release

## ساختار پروژه

```text
GitReleaseLab_Submission/
│
├── repository/
│   ├── .venv/
│   ├── src/
│   │   ├── app.py
│   │   ├── report.py
│   │   └── .env
│   ├── config/
│   │   └── settings.json
│   ├── tests/
│   │   └── tests_basic.py
│   ├── README.md
│   ├── VERSION
│   └── .gitignore
│
├── release/
│   ├── GitReleaseLab_v0.1.0.zip
│   └── SHA256SUMS
│
├── tools/
│   └── verify_release.py
│
├── evidence/
│   ├── git_evidence.txt
│   └── verification_result.json
│
└── test_cases.md
```

### کاربرد پوشه‌ها و فایل‌ها

- `repository/`: مخزن اصلی Git و فایل‌های Source Code پروژه
- `repository/src/`: کدهای اصلی برنامه
- `repository/config/`: تنظیمات برنامه
- `repository/tests/`: تست‌های خودکار پروژه
- `repository/VERSION`: شماره نسخه فعلی پروژه
- `repository/.gitignore`: مشخص‌کردن فایل‌هایی که نباید وارد Git شوند
- `release/`: بسته نهایی انتشار و فایل SHA256 آن
- `tools/verify_release.py`: ابزار بررسی صحت بسته انتشار
- `evidence/`: مدارک اجرای دستورات Git و نتیجه Verification
- `test_cases.md`: سناریوها و نتایج تست پروژه

> فایل‌های `.venv`، `.env`، `__pycache__` و فایل‌های حاوی اطلاعات محرمانه نباید وارد Git یا بسته Release شوند.

## ساخت Release

قبل از ساخت Release باید تمام تغییرات Commit شده باشند:

```powershell
cd .\repository
git status
```

خروجی مورد انتظار:

```text
nothing to commit, working tree clean
```

سپس Tag موردنظر را بررسی می‌کنیم:

```powershell
git show --no-patch --decorate v0.1.0
```

بسته Release مستقیماً از Tag ساخته می‌شود:

```powershell
New-Item -ItemType Directory -Force ..\release | Out-Null

git archive `
    --format=zip `
    --prefix=GitReleaseLab_v0.1.0/ `
    --output=..\release\GitReleaseLab_v0.1.0.zip `
    v0.1.0
```

استفاده از `git archive` باعث می‌شود بسته انتشار دقیقاً از محتوای Commit مربوط به Tag ساخته شود و فایل‌های Untracked، پوشه `.git` و فایل‌های Ignoreشده وارد بسته نشوند.

## تولید SHA256

پس از ساخت فایل ZIP، مقدار SHA256 آن با PowerShell محاسبه می‌شود:

```powershell
$archive = "..\release\GitReleaseLab_v0.1.0.zip"
$checksum = "..\release\SHA256SUMS"

$hash = (Get-FileHash $archive -Algorithm SHA256).Hash.ToLower()

"$hash  $(Split-Path $archive -Leaf)" |
    Set-Content $checksum -Encoding ascii
```

برای مشاهده مقدار ذخیره‌شده:

```powershell
Get-Content ..\release\SHA256SUMS
```

ساختار فایل `SHA256SUMS`:

```text
<sha256-hash>  GitReleaseLab_v0.1.0.zip
```

SHA256 مانند اثر انگشت دیجیتال فایل عمل می‌کند. اگر حتی بخش کوچکی از فایل ZIP تغییر کند، مقدار SHA256 آن نیز تغییر خواهد کرد.

## بررسی صحت Release

برای اجرای ابزار Verification ابتدا به پوشه اصلی Submission برمی‌گردیم:

```powershell
cd ..
```

اگر محیط مجازی فعال است:

```powershell
python .\tools\verify_release.py
```

بدون فعال‌کردن محیط مجازی:

```powershell
.\repository\.venv\Scripts\python.exe .\tools\verify_release.py
```

اسکریپت مراحل زیر را انجام می‌دهد:

1. مقدار مورد انتظار را از `release/SHA256SUMS` می‌خواند.
2. مقدار واقعی SHA256 فایل ZIP را محاسبه می‌کند.
3. دو مقدار را مقایسه می‌کند.
4. نتیجه را در `evidence/verification_result.json` ذخیره می‌کند.

## وضعیت‌های Verification

| وضعیت | مفهوم |
|---|---|
| `PASS` | فایل موجود است و SHA256 واقعی با مقدار مورد انتظار برابر است. |
| `FAIL` | فایل موجود است، اما SHA256 آن با مقدار مورد انتظار تفاوت دارد. |
| `MISSING` | فایل ZIP، فایل `SHA256SUMS` یا مقدار معتبر Hash پیدا نشده است. |

نمونه نتیجه موفق:

```json
{
  "file": "GitReleaseLab_v0.1.0.zip",
  "algorithm": "SHA256",
  "expected_hash": "...",
  "actual_hash": "...",
  "status": "PASS"
}
```

## نسخه پروژه

نسخه فعلی:

```text
0.1.0
```

Tag انتشار:

```text
v0.1.0
```