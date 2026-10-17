# Banking Simulation

This is a small banking project I made using Python. It uses Tkinter for the screens and SQLite to store the data.

## What it does

Admin can:
- open a new account (the account number and password are sent to the customer's email)
- search an account by its number
- close an account (an OTP is sent to the customer's email first)

Customer can:
- see their details and balance
- update name, email, password and mobile number
- deposit, withdraw and transfer money to another account
- reset a forgotten password using an OTP on email

The login screen also has a captcha.

## Built with

Python 3, Tkinter, SQLite, smtplib (for emails) and Pillow (for the logo image).

## How to run

1. Install Pillow: `pip install -r requirements.txt`
2. Run `python dbhandler.py` once. It creates the database.
3. Run `python mainproject.py`

Admin login: ACN `0`, password `Admin`.

## Email setup

Emails go out through Gmail. In `mailhandler.py` put your Gmail address in `mail_id`. Then set your Gmail App Password as an environment variable named `BANK_APP_PWD`. On Windows:

    setx BANK_APP_PWD "your_16_letter_app_password"

Close and reopen the terminal after this. You need 2-Step Verification turned on in your Google account to create an App Password.

## Things to improve

- Passwords are stored as plain text right now. They should be hashed.
- The admin login is hardcoded.
- Transaction history is not added yet.

---

## Hinglish

Ye ek chhota sa banking project hai jo maine Python mein banaya hai. Screens ke liye Tkinter aur data ke liye SQLite use kiya hai.

**Admin:** naya account kholna (ACN aur password email par jaate hain), account search karna, aur account close karna (pehle OTP jaata hai).

**Customer:** details aur balance dekhna, details update karna, deposit, withdraw aur transfer karna, aur password bhool jaye to OTP se reset karna.

**Kaise chalayein:**
1. `pip install -r requirements.txt`
2. `python dbhandler.py` (ek baar, database banane ke liye)
3. `python mainproject.py`

Admin login: ACN `0`, password `Admin`.

**Email setup:** `mailhandler.py` mein apna Gmail `mail_id` mein daalein, aur Gmail App Password ko `BANK_APP_PWD` naam ke environment variable mein rakhein (Windows par `setx BANK_APP_PWD "password"`).

Made by Shekh Aameen