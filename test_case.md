# Git Release Lab — Test Cases

## Test Environment

- Operating System: Windows
- Shell: PowerShell
- Release Tag: `v0.1.0`
- Release Archive: `release/GitReleaseLab_v0.1.0.zip`
- Checksum File: `release/SHA256SUMS.txt`
- Verification Tool: `tools/verify_release.py`

## Result Definitions

| Result | Meaning |
|---|---|
| `PASS` | تست با نتیجه مورد انتظار مطابقت دارد. |
| `FAIL` | فایل وجود دارد، اما مقدار یا رفتار آن صحیح نیست. |
| `MISSING` | فایل Archive یا Checksum موردنیاز وجود ندارد. |
| `PENDING` | تست هنوز اجرا نشده است. |

## Test Matrix

| ID | سناریو | روش بررسی | نتیجه مورد انتظار | نتیجه واقعی | Evidence |
|---|---|---|---|---|---|
| `GIT-01` | Repository ایجاد شده است | `git rev-parse --is-inside-work-tree` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `GIT-02` | Working Tree بعد از Release تمیز است | `git status --porcelain` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `GIT-03` | حداقل چهار Commit وجود دارد | `git rev-list --count HEAD` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `GIT-04` | Feature Branch ایجاد شده است | `git branch --list addingFeature feature/report` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `GIT-05` | Feature Branch با `master` ادغام شده است | `git merge-base --is-ancestor addingFeature master` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `GIT-06` | Tag نسخه `v0.1.0` وجود دارد | `git tag --list v0.1.0` | `PASS` | `PASS` | `evidence/git_evidence.txt` |
| `REL-01` | Release ZIP از Tag ساخته شده است | `Test-Path release/GitReleaseLab_v0.1.0.zip` | `PASS` | `PASS` | `evidence/release_contents.txt` |
| `REL-02` | Hash فایل اصلی معتبر است | اجرای Verifier روی Archive اصلی | `PASS` | `PASS` | `evidence/original_pass.json` |
| `REL-03` | تغییر فایل Release تشخیص داده می‌شود | اجرای Verifier روی Archive دست‌کاری‌شده | `FAIL` | `FAIL` | `evidence/tampered_fail.json` |
| `REL-04` | نبودن فایل Release تشخیص داده می‌شود | اجرای Verifier با مسیر Archive ناموجود | `MISSING` | `MISSING` | `evidence/missing_missing.json` |
| `SEC-01` | فایل `.env` و پوشه `.venv` داخل Release نیستند | بررسی فهرست فایل‌های ZIP | `PASS` | `PASS` | `evidence/security_checks.txt` |
| `SEC-02` | پوشه `.git` داخل Release نیست | بررسی فهرست فایل‌های ZIP | `PASS` | `PASS` | `evidence/security_checks.txt` |