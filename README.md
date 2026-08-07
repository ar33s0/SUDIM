# SUDIM
<p align="center">
  <img src="https://img.shields.io/badge/Python-3+%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Open%20Source-❤️-red" alt="Open Source">
</p>

**S**crap **U**ser **D**ata From **I**ranian **M**essengers

یک ابزار برای جمع‌آوری پروفایل هدف از پیام‌رسان‌های ایرانی

An automated tool for scraping target profiles from Iranian messengers

---

## 🖼 Demo

<p align="center">
  <img src="https://raw.githubusercontent.com/ar33s0/SUDIM/main/gif/GIF.gif" alt="SUDIM Demo" width="600" />
</p>

---

## 📝 Description | توضیحات

**🇮🇷 فارسی**

سودیم یک ابزار پایتونی هست که فرایند جمع‌آوری اطلاعات راجب هدف از پیام‌رسان رو اتوماتیک می‌کنه.
چون همچین ابزاری وجود نداشت تصمیم گرفتم خودم یدونه بسازم (یا حداقل من پیداش نکردم).
شاید براتون پیش اومده باشه که بخواید ببینید یه نفر تو پیام‌رسان‌های مختلف چه پروفایلایی گذاشته باشه.
این ابزار واسه شما ساخته شده
و میتونه اطلاعات رو از پیام‌رسان‌های بله، روبیکا، ایتا، سروش پلاس، آیگپ و شاد جمع‌آوری کنه.

**🇬🇧 English**

SUDIM is a Python tool that automates the process of gathering target information from Iranian messengers.
Since no such tool existed, I decided to build one myself (or at least I couldn't find one).
Have you ever wondered what profiles someone has across different messengers?
This tool is made for you.
It can collect data from Bale, Rubika, Eitaa, Soroush+, IGap and Shad.

---


## 📊 Messengers Status | وضعیت پیامرسان ها

| پیامرسان / Messenger | نام / Name | آخرین بازدید / Last Seen | نام کاربری / Username | بیوگرافی / Bio | آیدی عددی / Numeric ID | پرمیوم / Premium | جنسیت / Gender | تاریخ تولد / Birthdate |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| بله / Bale | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| ایتا / Eitaa | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| ایگپ / iGap | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| روبیکا / Rubika | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| شاد / Shad | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| سروش / Soroush | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

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
cd SUDIM
pip3 install -r requirements.txt
playwright install chromium
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

## ⭐ Support | حمایت
اگر این پروژه براتون مفید بود، لطفاً یک ستاره ⭐ به ریپازیتوری بدید.
این کار به دیده‌ شدن پروژه کمک میکنه.


If you found this project useful, please give the repository a ⭐ star.
This helps the project get noticed.

---

## 📜 License | لایسنس
این پروژه تحت لایسنس MIT منتشر شده. | This project is licensed under the MIT License.
