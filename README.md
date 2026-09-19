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

