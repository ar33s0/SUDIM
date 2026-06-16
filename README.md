# SUDIM

![Python](https://img.shields.io/badge/Python-3+%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Open Source](https://img.shields.io/badge/Open%20Source-❤️-red)

**S**crap **U**ser **D**ata From **I**ranian **M**essengers

یک ابزار برای جمع‌آوری پروفایل هدف از پیام‌رسان‌های ایرانی

An automated tool for scraping target profiles from Iranian messengers

---

## 🖼 Screenshot

<p align="center">
  <img src="https://raw.githubusercontent.com/ar33s0/SUDIM/main/screenshots/01.png" alt="SUDIM Screenshot" width="600" />
</p>

---

## 📝 Description | توضیحات

**🇮🇷 فارسی**

سودیم یک ابزار پایتونی هست که فرایند جمع‌آوری اطلاعات راجب هدف از پیام‌رسان رو اتوماتیک می‌کنه.
چون همچین ابزاری وجود نداشت تصمیم گرفتم خودم یدونه بسازم (یا حداقل من پیداش نکردم).
شاید براتون پیش اومده باشه که بخواید ببینید یه نفر تو پیام‌رسان‌های مختلف چه پروفایلایی گذاشته باشه.
این ابزار واسه شما ساخته شده
و میتونه اطلاعات رو از پیام‌رسان‌های بله، روبیکا، ایتا، سروش پلاس و شاد جمع‌آوری کنه.
(در آینده پیام‌رسان‌های دیگر مانند ایگپ هم اضافه خواهد شد)

**🇬🇧 English**

SUDIM is a Python tool that automates the process of gathering target information from Iranian messengers.
Since no such tool existed, I decided to build one myself (or at least I couldn't find one).
Have you ever wondered what profiles someone has across different messengers?
This tool is made for you.
It can collect data from Bale, Rubika, Eitaa, Soroush+, and Shad.
(More messengers like iGap will be added in the future)

---

## ✨ Features | ویژگی‌ها

| English | فارسی |
|---------|-------|
| Uses persistent_context for better speed and session management | استفاده از persistent_context برای سرعت و مدیریت بهتر نشست |
| Auto-adds the target as a contact | افزودن خودکار مخاطب |
| Extracts profile pictures, usernames, display names, etc. | گرفتن عکس‌های پروفایل، نام کاربری، اسم و... |
| Detects premium status, birthday, and gender on Soroush+ | تشخیص وضعیت پریمیوم، تاریخ تولد و جنسیت در سروش پلاس |
| Error handling for unstable internet connections | ارور هندلینگ برای اینترنت ضعیف |
| Multi-threading support (requires manual modification in main.py) | امکان مولتی‌تردینگ (نیاز به دستکاری در main.py) |
| Checks whether the target number has an account on each messenger | بررسی داشتن اکانت شماره مورد نظر در هر پیام‌رسان |
| Command-line argument support | قابلیت گرفتن آرگومان از خط فرمان |

---

## 📦 Requirements | نیازمندی‌ها

- Python 3+
- Rich
- Playwright
- Playwright Chromium

---

## 🚀 Installation | نصب

```bash
git clone https://github.com/ar33s0/SUDIM.git
cd sudim
pip3 install -r requirements.txt
playwright install chromiu
```

---

## ⚠️ Notice | نکات مهم

- **از یک اکانت خالی و بدون هیچ پیام و مخاطب استفاده کنید، در غیر این صورت به خطا برخورد می‌کنید! 🔴**
- **Use an empty account with no messages or contacts, otherwise you'll run into errors! 🔴**
- پروفایل‌ها در پوشه `profiles` ذخیره می‌شوند.
- Profiles are saved in the `profiles` directory.

---

## 🎮 Usage | نحوه استفاده

```bash
python3 login.py  # ابتدا در پیام‌رسان‌ها لاگین کنید | First, log into the messengers

python3 main.py
# یا|OR
python3 main.py {phone_number}
```
---

## 🤝 Contribution | مشارکت
🇮🇷 پیشنهادات و مشارکت شما باعث پیشرفت این پروژه می‌شه 🌱

🇬🇧 Suggestions and contributions help this project grow 🌱

---

## 📜 License | لایسنس
این پروژه تحت لایسنس MIT منتشر شده. | This project is licensed under the MIT License.
