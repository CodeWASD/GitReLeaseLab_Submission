# گزارش عیب‌یابی پروژه GitReleaseLab

این فایل سه خطای واقعی را که در طول اجرای تمرین‌های Git، Python و CI رخ داده‌اند ثبت می‌کند. برای هر خطا، پیام خطا، روند بررسی، علت اصلی، راه‌حل و روش تأیید نتیجه توضیح داده شده است.

---

# خطای اول — اجرای تست‌ها از مسیر اشتباه

## Problem — مشکل

تست‌های خودکار پیدا نمی‌شدند یا نمی‌توانستند ماژول‌های پروژه را Import کنند.

فرمان تست ابتدا از مسیر زیر اجرا شده بود:

```text
C:\Program Files\Microsoft VS Code
```

در تلاش دیگری نیز فرمان از داخل پوشه زیر اجرا شد:

```text
GitReleaseLab\repository\tests
```

هیچ‌کدام از این مسیرها برای ساختار فعلی پروژه مناسب نبودند.

## Error Message — پیام خطا

اجرای دستور زیر:

```powershell
python -m unittest discover -s tests -v
```

این خطا را تولید کرد:

```text
ImportError: Start directory is not importable: 'tests'
```

در اجرای دیگری از داخل پوشه `tests`، Import زیر شکست خورد:

```python
from src.report import build_report, save_report
```

پیام خطا:

```text
ModuleNotFoundError: No module named 'src'
```

## Investigation — روند بررسی

ابتدا مسیر فعلی Terminal و ساختار پروژه بررسی شد.

ساختار مربوط به تست‌ها به این شکل بود:

```text
repository/
├── src/
│   └── report.py
└── tests/
    └── test_basic.py
```

همچنین محل واقعی ماژول Import‌شده با دستور زیر بررسی شد:

```powershell
python -c "import src.report; print(src.report.__file__)"
```

مسیر صحیح ماژول:

```text
GitReleaseLab\repository\src\report.py
```

بررسی‌ها نشان دادند که برای دسترسی هم‌زمان Python به پوشه‌های `src` و `tests`، تست‌ها باید از داخل پوشه `repository` اجرا شوند.

## Root Cause — علت اصلی

علت اصلی، اجرای فرمان تست از Working Directory اشتباه بود.

وقتی فرمان از داخل `tests` اجرا می‌شد، Python نمی‌توانست پوشه هم‌سطح `src` را به‌عنوان ماژول پروژه پیدا کند.

همچنین هنگام اجرای فرمان از مسیر `C:\Program Files\Microsoft VS Code`، پوشه `tests` پروژه اصلاً در مسیر فعلی وجود نداشت.

## Fix — راه‌حل

ابتدا وارد پوشه اصلی برنامه شدیم:

```powershell
cd C:\Users\11\Desktop\file\GitReLeaseLab_Submission\GitReLeaseLab_Submission\repository
```

سپس تست‌ها را از همان مسیر اجرا کردیم:

```powershell
python -m pytest -q
```

در README نیز باید مشخص شود که تست‌ها از پوشه `repository` اجرا می‌شوند.

## Verification — تأیید نتیجه

بعد از اجرای تست‌ها از مسیر صحیح، ماژول `src.report` به‌درستی Import شد و تمام تست‌ها موفق شدند:

```text
...                                              [100%]
3 passed in 0.05s
```

## Source Used — منبع استفاده‌شده

- پیام‌های خطای واقعی Terminal
- بررسی مسیر ماژول با `src.report.__file__`
- ساختار فایل‌های پروژه
- مستندات Test Discovery در Python:

https://docs.python.org/3/library/unittest.html#test-discovery

---

# خطای دوم — استفاده تست‌ها از تابع تکراری به‌جای تابع اصلی

## Problem — مشکل

با وجود اینکه قابلیت `category` در فایل `src/report.py` پیاده‌سازی شده بود، تست‌ها همچنان اعلام می‌کردند که کلید `category` در گزارش وجود ندارد.

همچنین تابع `save_report` در یکی از تست‌ها مقدار `None` برمی‌گرداند.

## Error Message — پیام خطا

دو تست مربوط به Category با این خطا شکست خوردند:

```text
FAILED tests/test_basic.py::test_category_default_behavior
KeyError: 'category'
```

```text
FAILED tests/test_basic.py::test_explicit_category
KeyError: 'category'
```

تست Backward Compatibility نیز با خطای زیر شکست خورد:

```text
TypeError: 'NoneType' object is not subscriptable
```

خط شکست‌خورده:

```python
assert report["project"] == "GitReleaseLab"
```

این خطاها در حالی رخ می‌دادند که فایل `src/report.py` شامل کد صحیح زیر بود:

```python
"category": data.get("category", DEFAULT_CATEGORY)
```

و تابع `save_report` نیز شامل این دستور بود:

```python
return report
```

## Investigation — روند بررسی

ابتدا مسیر فایل واقعی `src.report` بررسی شد:

```powershell
python -c "import src.report; print(src.report.__file__)"
```

خروجی به فایل صحیح اشاره می‌کرد:

```text
repository\src\report.py
```

سپس با استفاده از ماژول `inspect` بررسی شد که تست‌ها دقیقاً کدام تابع `build_report` را اجرا می‌کنند:

```powershell
python -c "import inspect; from tests.test_basic import build_report as f; print(inspect.getsourcefile(f)); print(inspect.getsource(f))"
```

خروجی نشان داد که تابع استفاده‌شده از این فایل می‌آید:

```text
tests/test_basic.py
```

نسخه تابع موجود در فایل تست چنین بود:

```python
def build_report(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "project": data["project"],
        "status": data["status"],
        "summary": f"{data['project']} is {data['status']}",
    }
```

این تابع تکراری، فیلد `category` را نداشت.

## Root Cause — علت اصلی

در فایل `tests/test_basic.py` نسخه‌های تکراری از توابع برنامه، مانند `build_report` و `save_report`، تعریف شده بودند.

این توابع محلی روی توابع Import‌شده زیر سایه انداخته بودند:

```python
from src.report import build_report, save_report
```

بنابراین تست‌ها به‌جای اجرای پیاده‌سازی اصلی موجود در `src/report.py`، توابع تکراری داخل فایل تست را اجرا می‌کردند.

نسخه محلی `save_report` نیز مقدار گزارش را برنمی‌گرداند و به همین دلیل مقدار `None` دریافت می‌شد.

## Fix — راه‌حل

تعریف‌های تکراری `build_report` و `save_report` از فایل زیر حذف شدند:

```text
tests/test_basic.py
```

فایل تست فقط از توابع واقعی برنامه استفاده کرد:

```python
import json

from src.report import build_report, save_report
```

پیاده‌سازی اصلی فقط در فایل زیر باقی ماند:

```text
src/report.py
```

تابع `build_report` شامل مقدار پیش‌فرض Category بود:

```python
"category": data.get("category", DEFAULT_CATEGORY)
```

تابع `save_report` نیز گزارش را برمی‌گرداند:

```python
return report
```

## Verification — تأیید نتیجه

بعد از حذف توابع تکراری، تست‌ها مجدداً اجرا شدند:

```powershell
python -m pytest -q
```

نتیجه نهایی:

```text
...                                              [100%]
3 passed in 0.05s
```

سه سناریوی زیر با موفقیت اجرا شدند:

```text
category default behavior
explicit category
backward compatibility
```

## Source Used — منبع استفاده‌شده

- Traceback واقعی pytest
- خروجی دستور `inspect.getsourcefile`
- خروجی دستور `inspect.getsource`
- مقایسه فایل‌های `src/report.py` و `tests/test_basic.py`
- مستندات Assertion در pytest:

https://docs.pytest.org/en/stable/how-to/assert.html

---

# خطای سوم — واگرایی تاریخچه Branch محلی و Remote

## Problem — مشکل

Branch محلی `lab/ci-failure` یک‌بار حذف و سپس با همان نام دوباره ساخته شده بود.

در همین زمان، Branch متناظر در GitHub همچنان تاریخچه قبلی خود را داشت. بنابراین Branch محلی و Remote دارای نام یکسان، اما تاریخچه متفاوت بودند.

به همین دلیل Push کردن Branch محلی رد شد.

## Error Message — پیام خطا

اجرای Push این خطا را تولید کرد:

```text
! [rejected]        lab/ci-failure -> lab/ci-failure (non-fast-forward)
error: failed to push some refs
```

Git همچنین اعلام کرد:

```text
Updates were rejected because the tip of your current branch is behind
its remote counterpart.
```

سپس دستور زیر اجرا شد:

```bash
git pull --ff-only origin lab/ci-failure
```

اما به دلیل واگرایی تاریخچه‌ها شکست خورد:

```text
Diverging branches can't be fast-forwarded, you need to either:

git merge --no-ff

or:

git rebase
```

پیام نهایی:

```text
fatal: Not possible to fast-forward, aborting.
```

## Investigation — روند بررسی

ابتدا آخرین اطلاعات Remote دریافت شد:

```bash
git fetch origin
```

سپس تاریخچه تمام Branchها بررسی شد:

```bash
git log --oneline --graph --decorate --all
```

اطلاعات Tracking Branchها نیز مشاهده شد:

```bash
git branch -vv
```

نتیجه بررسی نشان داد:

- `origin/lab/ci-failure` به تاریخچه قبلی Remote اشاره می‌کرد.
- Branch محلی `lab/ci-failure` از Commit دیگری دوباره ساخته شده بود.
- هر دو Branch دارای Commitهایی بودند که در Branch دیگر وجود نداشتند.
- هیچ‌کدام از Branchها ادامه مستقیم دیگری نبودند.
- بنابراین Fast-forward امکان‌پذیر نبود.

## Root Cause — علت اصلی

حذف یک Branch محلی، Branch متناظر روی GitHub را حذف نمی‌کند.

Branch محلی با همان نام، اما از نقطه متفاوتی در تاریخچه ایجاد شده بود. Remote نیز تاریخچه قبلی خود را حفظ کرده بود.

وضعیت کلی به این شکل بود:

```text
                 Commitهای محلی
                /
Commit مشترک
                \
                 Commitهای Remote
```

Push معمولی نمی‌توانست Remote را به‌روزرسانی کند؛ زیرا این کار باعث حذف تاریخچه موجود Remote می‌شد.

همچنین `git pull --ff-only` فقط زمانی کار می‌کند که تاریخچه‌ها واگرا نشده باشند.

## Fix — راه‌حل

ابتدا وضعیت Remote دریافت شد:

```bash
git fetch origin
```

سپس روی Branch محلی صحیح قرار گرفتیم:

```bash
git switch lab/ci-failure
```

تاریخچه Remote با Branch محلی ادغام شد:

```bash
git merge origin/lab/ci-failure
```

پس از ایجاد Conflict، فایل‌های درگیر بررسی شدند:

```bash
git status
git diff --name-only --diff-filter=U
```

Conflictها به‌صورت محلی اصلاح شدند. سپس فایل‌های اصلاح‌شده Stage شدند:

```bash
git add repository/src/report.py
git add repository/tests/test_basic.py
```

Merge تکمیل شد:

```bash
git commit
```

در نهایت Branch اصلاح‌شده Push شد:

```bash
git push origin lab/ci-failure
```

از Force Push استفاده نشد؛ زیرا لازم بود Commit خراب و Commit اصلاحی هر دو در تاریخچه باقی بمانند.

## Verification — تأیید نتیجه

تاریخچه نهایی بررسی شد:

```bash
git log --oneline --graph --decorate --all
```

Commit مربوط به شکست عمدی CI در تاریخچه باقی ماند:

```text
647f2510626d91a0d3ea260e8c478ee77b1265a2
```

Commit اصلاحی نیز حفظ شد:

```text
8123e1b0029585527f0ff9296338a35d54885c65
```

پس از اصلاح، تست‌ها اجرا شدند:

```powershell
python -m pytest -q
```

نتیجه:

```text
...                                              [100%]
3 passed in 0.05s
```

این نتیجه تأیید کرد که تاریخچه Branch حفظ شده، Conflictها برطرف شده و نسخه اصلاحی توسط تست‌ها تأیید شده است.

## Source Used — منبع استفاده‌شده

- پیام واقعی ردشدن `git push`
- پیام واقعی شکست `git pull --ff-only`
- نمودار تاریخچه Repository با دستور زیر:

```bash
git log --oneline --graph --decorate --all
```

- مستندات رسمی `git pull`:

https://git-scm.com/docs/git-pull

- مستندات رسمی `git push`:

https://git-scm.com/docs/git-push

---

# نتیجه‌گیری

سه خطای ثبت‌شده نشان دادند که مشکلات پروژه فقط از کد برنامه ایجاد نمی‌شوند و می‌توانند از موارد زیر نیز ناشی شوند:

- اجرای دستور از Working Directory اشتباه
- استفاده ناخواسته از تابع یا فایل اشتباه
- ناهماهنگی تاریخچه Branch محلی و Remote

برای عیب‌یابی صحیح، بررسی مرحله‌ای پیام خطا، مسیر اجرای برنامه، فایل واقعی Import‌شده و نمودار تاریخچه Git ضروری است.