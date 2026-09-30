# دستورات ارتباط با Remote Repository

## `git fetch`

<div dir="rtl">

دستور `git fetch` آخرین Commitها، Branchها و Tagهای موجود در Remote Repository را دریافت می‌کند و Remote-tracking Branchهایی مانند `origin/master` را به‌روزرسانی می‌کند.

این دستور Branch فعلی و فایل‌های Working Tree را تغییر نمی‌دهد؛ بنابراین می‌توانیم پیش از ادغام، تغییرات Remote را بررسی کنیم.

مثال:

</div>

```bash
git fetch origin

## git pull
<div dir="rtl">
این دستور ترکیبی ازgit pull وmerge بوده .
چرا که اطلاعات ریموت را در ابتدا دریافت و به روز میکند سپس آنها را بر روی برنچ مورد نظر از ریپاسیتوری لوکال اعمال میکند 
</div> 

## git clone
<div dir="rtl">
این دستور اطلاعات یک Repository موجود Remoteرا از Githubدریافت میکند برای من برای پروژه هایم از روش sshاستفاده کردم و قبل از آن به کمک ssh-keygen,sshسیستم را دریافت کرده وبه Githubمتصل کردم
</div> 