from tkinter import Tk,Label,Frame,Entry,Button,messagebox,simpledialog
from tkinter.ttk import Combobox
import random
import mygenerator
import dbhandler
import mailhandler
import time
import sqlite3
from PIL import Image, ImageTk
import shutil
import os
import re


def update_time():
    t=time.strftime("%A,%b %d %y ⏰%r")
    lbl_dt.configure(text=t)
    lbl_dt.after(1000,update_time)

def customer_screen():
    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='light yellow')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.74)

    def Logout_click():
        frm.destroy()
        main_screen()  

    def viewdetails_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(x=215,y=120,relwidth=.88,relheight=.6)

        lbl_ftitle=Label(ifrm,text="This is view details screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        query='select * from users where acn=?'
        curobj.execute(query,(user_acn,))
        row=curobj.fetchone()
        conobj.close()
        details=(f'Name = {row[1]}\n'
                 f'ACN = {row[0]}\n'
                 f'Bal = {row[7]}\n'
                 f'Open Date = {row[9]}')

        lbl_details=Label(ifrm,text=details,justify='left',
                          font=('arial',15,'bold'),bg='white')
        lbl_details.place(relx=.5,y=70,anchor='n')
        

    def updatedetails_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(x=215,y=120,relwidth=.88,relheight=.6)

        lbl_ftitle=Label(ifrm,text="This is Update details screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')


        def up_details():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            query='select name,password,email,mob from users where acn=?'
            curobj.execute(query,(user_acn,))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update","Details updated")
            frm.destroy()
            customer_screen()

        lbl_name=Label(ifrm,text="Name",font=('arial',15,'bold'),bg='white')
        lbl_name.place(relx=.10,rely=.25,anchor='w')
        e_name=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_name.place(relx=.18,rely=.25,width=280,height=32,anchor='w')
        
        lbl_email=Label(ifrm,text="Email",font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.10,rely=.45,anchor='w')
        e_email=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_email.place(relx=.18,rely=.45,width=280,height=32,anchor='w')
        
        lbl_pass=Label(ifrm,text="Pass",font=('arial',15,'bold'),bg='white')
        lbl_pass.place(relx=.10,rely=.65,anchor='w')
        e_pass=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_pass.place(relx=.18,rely=.65,width=280,height=32,anchor='w')
        
        lbl_mob=Label(ifrm,text="Mob",font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.55,rely=.25,anchor='w')
        e_mob=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_mob.place(relx=.63,rely=.25,width=280,height=32,anchor='w')

        up_btn=Button(ifrm,text='Update Details',bd=3,font=('arial',12,'bold'),
              bg='blue',fg='white',cursor='hand2',command=up_details)
        up_btn.place(relx=.5,rely=.85,width=190,height=42,anchor='center')

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        query='select name,pass,email,mob from users where acn=?'
        curobj.execute(query,(user_acn))
        tup=curobj.fetchone()
        conobj.close()

        e_name.insert(0,tup[0])
        e_pass.insert(0,tup[1])
        e_email.insert(0,tup[2])
        e_mob.insert(0,tup[3])

    def deposit_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(x=215,y=120,relwidth=.88,relheight=.6)

        lbl_ftitle=Label(ifrm,text="This is Deposit screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

    def withdraw_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(x=215,y=120,relwidth=.88,relheight=.6)

        lbl_ftitle=Label(ifrm,text="This is Withdraw screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

    def transfer_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(x=215,y=120,relwidth=.88,relheight=.6)

        lbl_ftitle=Label(ifrm,text="This is Transfer screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')


    # Logout - top right
    logout_btn=Button(frm,text='Logout',bd=3,font=('arial',12,'bold'),
                      command=Logout_click,cursor='hand2')
    logout_btn.place(relx=1,x=-125,y=4,width=110,height=35)

    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    query='select name,password,email,mob from users where acn=?'
    curobj.execute(query,(user_acn,))
    name=curobj.fetchone()[0]
    conobj.close()

    # Welcome - top left
    lbl_wel=Label(frm,text=f"Welcome, {name}",
                  font=('arial',18,'bold'),bg='light yellow')
    lbl_wel.place(x=10,y=8)

   # Left side vertical buttons
    view_btn=Button(frm,text='View Details',bd=3,font=('arial',12,'bold'),
                    bg='blue',fg='white',cursor='hand2',command=viewdetails_screen)
    view_btn.place(x=10,y=130,width=190,height=42)

    update_btn=Button(frm,text='Update Details',bd=3,font=('arial',12,'bold'),
                      bg='purple',fg='white',cursor='hand2',command=updatedetails_screen)
    update_btn.place(x=10,y=198,width=190,height=42)

    deposit_btn=Button(frm,text='Deposit',bd=3,font=('arial',12,'bold'),
                       bg='green',fg='white',cursor='hand2',command=deposit_screen)
    deposit_btn.place(x=10,y=266,width=190,height=42)

    def deposit():
        amt=simpledialog.askfloat("Deposit Amount","Enter Amount")
        if amt is None or amt<=0:
            return
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        query='update users set bal=ifnull(bal,0)+? where acn=?'
        curobj.execute(query,(amt,user_acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Deposit","Amount Deposit")
        viewdetails_screen()

    deposit_btn.configure(command=deposit)

    withdraw_btn=Button(frm,text='Withdraw',bd=3,font=('arial',12,'bold'),
                        bg='red',fg='white',cursor='hand2',command=lambda:withdraw())
    withdraw_btn.place(x=10,y=334,width=190,height=42)

    def withdraw():
        amt=simpledialog.askfloat("Withdraw Amount","Enter Amount")
        if amt is None:
            return
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select bal from users where acn=?',(user_acn,))
        bal=curobj.fetchone()[0] or 0
        conobj.close()

        if amt>bal:
            messagebox.showerror("Withdraw","Insufficient Bal")
            return

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('update users set bal=ifnull(bal,0)-? where acn=?',(amt,user_acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Withdraw","Amount Withdraw")
        viewdetails_screen()

    withdraw_btn=Button(frm,text='Withdraw',bd=3,font=('arial',12,'bold'),
                        bg='red',fg='white',cursor='hand2',command=withdraw)
    withdraw_btn.place(x=10,y=334,width=190,height=42)

    def transfer():
        to_acn=simpledialog.askinteger("Transfer Amount","Enter To ACN")
        if to_acn is None:
            return
        amt=simpledialog.askfloat("Transfer Amount","Enter Amount")
        if amt is None:
            return
        if to_acn==int(user_acn):
            messagebox.showerror("Transfer Amount","Apne hi account mein transfer nahi ho sakta")
            return

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select bal from users where acn=?',(user_acn,))
        bal=curobj.fetchone()[0] or 0
        curobj.execute('select acn from users where acn=?',(to_acn,))
        row=curobj.fetchone()
        conobj.close()

        if row is None:
            messagebox.showerror("Transfer Amount","To ACN does not exist")
            return
        if amt>bal:
            messagebox.showerror("Transfer Amount","Insufficient Bal")
            return

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('update users set bal=ifnull(bal,0)-? where acn=?',(amt,user_acn))
        curobj.execute('update users set bal=ifnull(bal,0)+? where acn=?',(amt,to_acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Transfer Amount",f"{amt} Amount Transferred to ACN {to_acn}")
        viewdetails_screen()

    transfer_btn=Button(frm,text='Transfer',bd=3,font=('arial',12,'bold'),
                        bg='brown',fg='white',cursor='hand2',command=transfer)
    transfer_btn.place(x=10,y=402,width=190,height=42)

def admin_screen():
    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='light yellow')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.74)

    def Logout_click():
        frm.destroy()
        main_screen()

    def openacn_screen():
        ifrm=Frame(root,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.012,rely=.37,relwidth=.976,relheight=.55)

        def create_account():
            name = e_name.get().strip()
            email = e_email.get().strip()
            adhar = e_adhar.get().strip()
            mob = e_mob.get().strip()
            age = e_age.get().strip()
            gender = cb_gender.get()

            if len(name)==0:
                messagebox.showerror("Open Account","Name is required")
                return
            if len(email)==0:
                messagebox.showerror("Open Account","Email is required")
                return

            match=re.fullmatch(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+",email)
            if match==None:
                messagebox.showerror("Open Account","Invalid Email")
                return
                  
            if len(adhar)==0:
                messagebox.showerror("Open Account","Adhar is required")
                return

            if len(mob)==0:
                messagebox.showerror("Open Account","Mob is required")
                return

            if not (name and email and adhar and mob and age) or gender == '--select--':
              messagebox.showerror("Open Account", "plese fill all feilds")
              return

            bal = 0
            opendate = time.strftime("%d-%m-%Y %H:%M:%S")
            pwd = mygenerator.generate_password()

            conobj = sqlite3.connect('bank.sqlite')
            curobj = conobj.cursor()
            query = '''insert into users(name,password,email,mob,adhar,age,bal,gender,opendate)
               values(?,?,?,?,?,?,?,?,?)'''
            curobj.execute(query, (name, pwd, email, mob, adhar, age, bal, gender, opendate))
            acn = curobj.lastrowid
            conobj.commit()
            conobj.close()

            sent = mailhandler.send_openacn_email(email, name, acn, pwd)
            if sent:
             messagebox.showinfo("Create Account", "Credentials are sent to email")
            else:
              messagebox.showwarning("Create Account", "Account Opened, but email could not be sent")

    
        lbl_ftitle=Label(ifrm,text="This is open account screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

        lbl_name=Label(ifrm,text="Name",font=('arial',15,'bold'),bg='white')
        lbl_name.place(relx=.10,rely=.25,anchor='w')
        e_name=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_name.place(relx=.18,rely=.25,width=280,height=32,anchor='w')

        lbl_email=Label(ifrm,text="Email",font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.10,rely=.45,anchor='w')
        e_email=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_email.place(relx=.18,rely=.45,width=280,height=32,anchor='w')

        lbl_adhar=Label(ifrm,text="Adhar",font=('arial',15,'bold'),bg='white')
        lbl_adhar.place(relx=.10,rely=.65,anchor='w')
        e_adhar=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_adhar.place(relx=.18,rely=.65,width=280,height=32,anchor='w')

        lbl_mob=Label(ifrm,text="Mob",font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.55,rely=.25,anchor='w')
        e_mob=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_mob.place(relx=.63,rely=.25,width=280,height=32,anchor='w')

        lbl_age=Label(ifrm,text="Age",font=('arial',15,'bold'),bg='white')
        lbl_age.place(relx=.55,rely=.45,anchor='w')
        e_age=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_age.place(relx=.63,rely=.45,width=280,height=32,anchor='w')

        lbl_gender=Label(ifrm,text="Gender",font=('arial',15,'bold'),bg='white')
        lbl_gender.place(relx=.55,rely=.65,anchor='w')
        cb_gender=Combobox(ifrm,values=['Male','Female','Other','--select--'],
                           font=('arial',12,'bold'),state='readonly')
        cb_gender.current(3)
        cb_gender.place(relx=.63,rely=.65,width=280,height=32,anchor='w')

        submit_btn=Button(ifrm,text='Submit',bd=3,font=('arial',13,'bold'),
                          bg='green',fg='white',cursor='hand2',command=create_account)
        submit_btn.place(relx=.5,x=-100,rely=.85,width=120,height=38,anchor='center')

        reset_btn=Button(ifrm,text='Reset',bd=3,font=('arial',13,'bold'),
                         bg='red',fg='white',cursor='hand2')
        reset_btn.place(relx=.5,x=100,rely=.85,width=120,height=38,anchor='center')

    def viewacn_screen():
        ifrm=Frame(root,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.012,rely=.37,relwidth=.976,relheight=.55)

        lbl_result=Label(ifrm,text='',font=('arial',16,'bold'),
                         bg='white',justify='left')
        lbl_result.place(relx=.38,rely=.4)

        def search():
            try:
                acn = int(e_acn.get())
            except ValueError:
                lbl_result.configure(text='')
                messagebox.showerror("Search", "Please enter a valid ACN")
                return

            conobj = sqlite3.connect('bank.sqlite')
            curobj = conobj.cursor()
            query = 'select name,email,bal,opendate,adhar from users where acn=?'
            curobj.execute(query, (acn,))
            row = curobj.fetchone()
            conobj.close()

            if row is None:
                lbl_result.configure(text='')
                messagebox.showerror("Search", "Account does not exist")
            else:
                details = (f'Name : {row[0]}\n\n'
                           f'Email : {row[1]}\n\n'
                           f'Balance : ₹ {row[2]}\n\n'
                           f'Opened On : {row[3]}\n\n'
                           f'Adhar : XXXX-XXXX-{row[4][-4:]}')
                lbl_result.configure(text=details)


        lbl_ftitle=Label(ifrm,text="This is view account screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

        lbl_acn=Label(ifrm,text="ACN",font=('arial',15,'bold'),bg='white')
        lbl_acn.place(relx=.32,rely=.2,anchor='w')

        e_acn=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_acn.place(relx=.38,rely=.2,width=280,height=32,anchor='w')

        search_btn=Button(ifrm,command=search,text='Search',bd=3,font=('arial',12,'bold'),
                          bg='pink',fg='black',cursor='hand2')
        search_btn.place(relx=.38,x=295,rely=.2,width=100,height=32,anchor='w')

    def closeacn_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.012,rely=.23,relwidth=.976,relheight=.74)

        def close():
            try:
                acn = int(e_acn.get())
            except ValueError:
                messagebox.showerror("Close Account", "Please enter a valid ACN")
                return

            conobj = sqlite3.connect('bank.sqlite')
            curobj = conobj.cursor()
            curobj.execute('select name,email from users where acn=?', (acn,))
            row = curobj.fetchone()
            conobj.close()

            if row is None:
                messagebox.showerror("Close Account", "Account does not exist")
                return

            gen_otp = random.randint(1000, 9999)
            sent = mailhandler.send_closeacn_email(row[1], row[0], gen_otp)
            if not sent:
                messagebox.showerror("Close Account", "OTP email could not be sent")
                return

            user_otp = simpledialog.askinteger("Close Account", "Enter OTP")
            if user_otp == gen_otp:
                conobj = sqlite3.connect('bank.sqlite')
                curobj = conobj.cursor()
                curobj.execute('delete from users where acn=?', (acn,))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Close Account", "Account closed")
            else:
                messagebox.showerror("Close Account", "Invalid OTP")
           

                
        lbl_ftitle=Label(ifrm,text="This is close account screen",
                         font=('arial',15,'bold'),bg='light yellow')
        lbl_ftitle.place(relx=.5,y=25,anchor='center')

        lbl_acn=Label(ifrm,text="ACN",font=('arial',15,'bold'),bg='white')
        lbl_acn.place(relx=.32,rely=.2,anchor='w')
        
        e_acn=Entry(ifrm,font=('arial',14,'bold'),bd=3)
        e_acn.place(relx=.38,rely=.2,width=280,height=32,anchor='w')
        
        close_btn=Button(ifrm,command=close,text='Close',bd=3,font=('arial',12,'bold'),
                                  bg='pink',fg='black',cursor='hand2')
        close_btn.place(relx=.38,x=295,rely=.2,width=100,height=32,anchor='w')

    logout_btn=Button(frm,text='Logout',bd=3,font=('arial',12,'bold'),
                      command=Logout_click,cursor='hand2')
    logout_btn.place(x=6,y=4,width=110,height=35)

    lbl_wel=Label(frm,text="Welcome Admin",
                  font=('arial',20,'bold'),bg='light yellow')
    lbl_wel.place(relx=1,x=-20,y=22,anchor='e')

    openacn_btn=Button(frm,text='Open Account',bd=3,
                       font=('arial',12,'bold'),bg='royal blue',fg='white',
                       cursor='hand2',command=openacn_screen)
    openacn_btn.place(x=15,y=55,width=180,height=45)

    viewacn_btn=Button(frm,text='View Account',bd=3,
                       font=('arial',12,'bold'),bg='green',fg='white',
                       cursor='hand2',command=viewacn_screen)
    viewacn_btn.place(relx=.5,x=-90,y=55,width=180,height=45)

    closeacn_btn=Button(frm,text='Close Account',bd=3,
                        font=('arial',12,'bold'),bg='red',fg='white',
                        cursor='hand2',command=closeacn_screen)
    closeacn_btn.place(relx=1,x=-200,y=55,width=180,height=45)


def fp_screen():
    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='light yellow')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.74)

    def back_click():
        frm.destroy()
        main_screen()


    back_btn=Button(frm,text='Back',bd=3,font=('arial',12,'bold'),
                    command=back_click,cursor='hand2')
    back_btn.place(x=6,y=4,width=110,height=35)

    lbl_acn=Label(frm,text="User ACN",
                  font=('arial',20,'bold'),bg='light yellow')
    lbl_acn.place(relx=.32,rely=.12,anchor='w')

    e_acn=Entry(frm,font=('arial',15,'bold'),bd=3)
    e_acn.place(relx=.47,rely=.12,width=300,height=35,anchor='w')

    lbl_Email=Label(frm,text="User Email",
                    font=('arial',20,'bold'),bg='light yellow')
    lbl_Email.place(relx=.32,rely=.24,anchor='w')

    e_Email=Entry(frm,font=('arial',15,'bold'),bd=3)
    e_Email.place(relx=.47,rely=.24,width=300,height=35,anchor='w')
    def send_otp():
        try:
            acn = int(e_acn.get())
        except ValueError:
            messagebox.showerror("Forgot Password", "Please enter a valid ACN")
            return
        email = e_Email.get().strip()

        conobj = sqlite3.connect('bank.sqlite')
        curobj = conobj.cursor()
        curobj.execute('select name,password from users where acn=? and email=?', (acn, email))
        row = curobj.fetchone()
        conobj.close()

        if row is None:
            messagebox.showerror("Forgot Password", "ACN does not exist")
            return

        otp = random.randint(1000, 9999)
        if not mailhandler.send_fp_email(email, row[0], otp):
            messagebox.showerror("Forgot Password", "OTP email could not be sent")
            return

        user_otp = simpledialog.askinteger("Forgot Password", "Enter OTP")
        if user_otp != otp:
            messagebox.showerror("Forgot Password", "Invalid OTP")
            return

        new_pwd = simpledialog.askstring("Forgot Password", "Enter new password", show='*')
        if not new_pwd:
            return
        conobj = sqlite3.connect('bank.sqlite')
        curobj = conobj.cursor()
        curobj.execute('update users set password=? where acn=?', (new_pwd, acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Forgot Password", "Password changed")

    OTP_btn=Button(frm,text='Validate & Send OTP',bd=3,
                   font=('arial',12,'bold'),cursor='hand2',command=send_otp)
    OTP_btn.place(relx=.47,rely=.36,width=230,height=35,anchor='w')


def main_screen():
    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.74)

    def fp_click():
        frm.destroy()
        fp_screen()

    def reset():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_captcha.delete(0,"end")
        cb_user.current(2)    

    def login_click():
        global user_acn
        user_type=cb_user.get()
        user_acn=e_acn.get().strip()
        user_pass=e_pass.get().strip()
        user_captcha=e_captcha.get().strip().upper()
        if user_type=="Admin" and user_acn=='0' and user_pass== "Admin" and user_captcha==captcha.replace(' ',''):
            frm.destroy()
            admin_screen()
        elif user_type=="Customer" and user_acn.isdigit() and user_pass and user_captcha==captcha.replace(' ',''):
             conobj = sqlite3.connect('bank.sqlite')
             curobj = conobj.cursor()
             curobj.execute('select name,email from users where acn=? and password=?', (user_acn,user_pass))
             row = curobj.fetchone()
             conobj.close()
             if row==None:
                 messagebox.showerror("Login","Invalid ACN/Pass")
             else:    
                 frm.destroy()
                 customer_screen()
        else:
            messagebox.showerror("User Type","Invalid credentials")

    lbl_user=Label(frm,text="User Type",
                   font=('arial',20,'bold'),bg='powder blue')
    

    lbl_user=Label(frm,text="User Type",
                   font=('arial',20,'bold'),bg='powder blue')
    lbl_user.place(relx=.32,rely=.12,anchor='w')

    cb_user=Combobox(frm,values=['Customer','Admin','----select----'],
                     font=('arial',12,'bold'),state='readonly')
    cb_user.current(2)
    cb_user.config(state='readonly')
    cb_user.place(relx=.47,rely=.12,width=300,height=35,anchor='w')

    lbl_acn=Label(frm,text="User ACN",
                  font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.32,rely=.24,anchor='w')

    e_acn=Entry(frm,font=('arial',15,'bold'),bd=3)
    e_acn.place(relx=.47,rely=.24,width=300,height=35,anchor='w')

    lbl_pass=Label(frm,text="User Pass",
                   font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.32,rely=.36,anchor='w')

    e_pass=Entry(frm,font=('arial',15,'bold'),bd=3,show='*')
    e_pass.place(relx=.47,rely=.36,width=300,height=35,anchor='w')

    captcha=mygenerator.generate_captcha()
    lbl_show_captcha=Label(frm,text=captcha,
                           font=('arial',20,'bold'),bg='white',fg='purple',
                           bd=3,relief='groove')
    lbl_show_captcha.place(relx=.47,rely=.48,width=300,height=35,anchor='w')

    def refresh_captcha():
        nonlocal captcha
        captcha=mygenerator.generate_captcha()
        lbl_show_captcha.configure(text=captcha)

    ref_btn=Button(frm,text='⟳ Refresh',bd=3,font=('arial',12,'bold'),
                   cursor='hand2',command=refresh_captcha)
    ref_btn.place(relx=.47,x=310,rely=.48,width=110,height=35,anchor='w')

    lbl_captcha=Label(frm,text="User Captcha",
                      font=('arial',20,'bold'),bg='powder blue')
    lbl_captcha.place(relx=.32,rely=.60,anchor='w')

    e_captcha=Entry(frm,font=('arial',15,'bold'),bd=3)
    e_captcha.place(relx=.47,rely=.60,width=300,height=35,anchor='w')

    login_btn=Button(frm,text='Login',bd=3,font=('arial',12,'bold'),
                     cursor='hand2',command=login_click)
    login_btn.place(relx=.47,rely=.74,width=110,height=35,anchor='w')

    reset_btn=Button(frm,text='Reset',command=reset,bd=3,font=('arial',12,'bold'),
                     cursor='hand2',)
    reset_btn.place(relx=.47,x=120,rely=.74,width=110,height=35,anchor='w')

    fp_btn=Button(frm,text='Forgot Password',bd=3,
                  font=('arial',12,'bold'),command=fp_click,cursor='hand2')
    fp_btn.place(relx=.47,rely=.84,width=230,height=35,anchor='w')


root=Tk()
root.state('zoomed')
root.configure(bg='black')
root.resizable(width=False,height=False)

lbl_title=Label(root,text="Banking simulation",
                font=('arial',40,'bold','underline'))
lbl_title.pack()

lbl_dt=Label(root,text=time.strftime("%A,%b %d %y ⏰%r"),
             font=('arial',20,'bold'),bg='pink',fg='blue')
lbl_dt.pack(pady=20)
update_time()

img=Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Banking image.jpeg')).resize((300,200))  
imgtk=ImageTk.PhotoImage(img,master=root)
lbl_logo=Label(root,image=imgtk,bd=0)
lbl_logo.place(relx=0,rely=0)

lbl_footer=Label(root,text="Developed BY : Shekh Aameen @ 7380864086",
                 font=('arial',10,'bold','underline'))
lbl_footer.pack(side='bottom',pady=10)

main_screen()
root.mainloop()