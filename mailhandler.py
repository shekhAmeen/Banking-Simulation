import smtplib
import random
import os
from email.message import EmailMessage

mail_id = ''  # Your Gmail id
app_pwd = os.environ.get('BANK_APP_PWD', '')  # app password of Gmail id 

def send_openacn_email(to, name, acn, pwd):
    try:
        msg = EmailMessage()
        msg['From'] = mail_id
        msg['To'] = to
        msg['Subject'] = 'Account Opened'
        msg.set_content(f'''Hello {name},
We have successfully opened your account with the following credentials:
Account No = {acn}
Password = {pwd}
Kindly change your password on first login.

Thanks
ABC Bank
Noida
''')
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=20) as server:
            server.starttls()
            server.login(mail_id, app_pwd)
            server.send_message(msg)
        return True
    except Exception as e:
        print("Email error:", e)
        return False


def send_fp_email(to, name, otp):
    try:
        msg = EmailMessage()
        msg['From'] = mail_id
        msg['To'] = to
        msg['Subject'] = 'Password Reset OTP'
        msg.set_content(f'''Hello {name},
Your OTP to reset your password is {otp}

Kindly share with Bank Admin

Thanks
ABC Bank
Noida
''')
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=20) as server:
            server.starttls()
            server.login(mail_id, app_pwd)
            server.send_message(msg)
        return True
    except Exception as e:
        print("Email error:", e)
        return False

def send_closeacn_email(to, name, otp):
    try:
        msg = EmailMessage()
        msg['From'] = mail_id
        msg['To'] = to
        msg['Subject'] = 'Account Closure OTP'
        msg.set_content(f'''Hello {name},
Here is the OTP to close your account
OTP = {otp}

Kindly share with Bank Admin
Thanks
ABC Bank
Noida
''')
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=20) as server:
            server.starttls()
            server.login(mail_id, app_pwd)
            server.send_message(msg)
        return True
    except Exception as e:
        print("Email error:", e)
        return False        