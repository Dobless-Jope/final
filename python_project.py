from tkinter import *
from tkinter import ttk
import os
import csv
from email.message import EmailMessage
import ssl
import smtplib

screen=Tk()
screen.geometry('360x200')
screen.title('Main page')

def d1():
    screen4.destroy()
    
def userinfo():
    u1 = log_username.get()
    c=str("C:\\Users\\lenovo\\OneDrive\\Desktop\\Accounts\\" + u1 + ".txt")
    with open (c,'r') as h:
        file_data = h.read()
        file_user = file_data.split('\n')
        a1=file_user[0]
        a2=file_user[1]
        a3=file_user[2]
        a4=file_user[3]
        global screen4
        screen4 = Toplevel(screen)
        screen4.title('Userdata')
        
        Label(screen4, text="Your username is"+":"+" "+a1).pack()
        Label(screen4, text="").pack()
        
        Label(screen4, text="Your age is"+":"+" "+a3).pack()
        Label(screen4, text="").pack()
        
        Label(screen4, text="Your gender is"+":"+" "+a4).pack()
        Label(screen4, text="").pack()
        
        Button(screen4, text="Return to account dashboard", command=d1).pack()

def send_complain():
    r = n.get("1.0", 'end-1c')
    s = p.get("1.0", 'end-1c')

    if s == "" or r == "":
        complaint_notif.config(
            text="Subject/Body cannot be empty", fg='red')
    else:
        email_sender = 'test163773@gmail.com'
        email_password = 'sunlmdmrewkhcqpp'

        email_receiver = 'adhinbinoy7@gmail.com'

        subject = r
        body = s

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            complaint_notif.config(
            text="Complaint sent successfully", fg='green')

def complain():
    global screen6,sub,bod,n,p,complaint_notif
    screen7 = Toplevel(screen)
    screen7.title('Complaint screen')
    screen7.geometry("600x450")
    sub = StringVar()
    bod = StringVar()
    
    m = Label(screen7, text='Subject:', font=(
        "times new roman", 12, "bold"))
    m.place(x=0, y=10)

    n = Text(screen7,
             width=74)
    n.place(x=1, y=40, height=30)

    o = Label(screen7, text='Body:', font=(
        "times new roman", 12, "bold"))
    o.place(x=0, y=90)

    p = Text(screen7,
             width=74)
    p.place(x=1, y=120, height=200)

    q = Button(screen7, font=("times new roman", 12, "bold"),
               text="Send complaint",command=send_complain)
    q.place(x=250, y=350)

    complaint_notif = Label(screen7, font=("times new roman", 12, "bold"))
    complaint_notif.place(x=200, y=400)

def manager_data():
    u3 = b.get()
    k = "Information on the following manager"
    if u3 == '':
        manager_inf.delete('1.0', END)
        
    if u3 == 'Spartacus Edmundo':
        with open("C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Spartacus Edmundo.txt") as h:
            m = h.read()
            manager_inf.delete('1.0', END)
            manager_inf.insert(END,m)
            
    if u3 == 'Maram Balder':
        with open("C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Maram Balder.txt") as h:
            m = h.read()
            manager_inf.delete('1.0', END)
            manager_inf.insert(END,m)

    if u3 == 'Husam Mirosław':
        with open("C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Husam Mirosław.txt") as h:
            m = h.read()
            manager_inf.delete('1.0', END)
            manager_inf.insert(END,m)

def correct(num):
    if num.isdigit() or num == "" or num == None:
        return True
    else:
        return False
    
def overview():
    a = username.get()
    b = name_of_user.get()
    c = event.get()
    d = budget.get()
    e = manager.get()
    f = date1.get()
    g = date2.get()
    h = date3.get()
    i = location.get()
    j = telephone.get()
    k = "Enter full data"
    m = "Invalid contact detail"
    o = "Invalid date entered"
    p = int(f)
    q = int(g)
    r = int(h)
    s = "Year not valid"

    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "" or j == "" or f == '0' or g == '0' or h == '0' or d == '0':
        t1.delete("1.0", END)
        t1.insert(END, k)
        return

    elif len(j) != 10:
        t1.delete("1.0", END)
        t1.insert(END, m)
        return

    elif len(f) not in range(1, 3) or len(g) not in range(1, 3) or len(h) != 4:
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 32) and (q == 1 or q == 3 or q == 5 or q == 7 or q == 8 or q == 10 or q == 12):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 31) and (q == 4 or q == 6 or q == 9 or q == 11):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 29) and (q == 2) and (r == 2022 or r == 2023 or r == 2025 or r == 2026 or r == 2027 or r == 2029 or r == 2030):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 30) and (q == 2) and (r == 2024, r == 2028):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif q < 0 or q > 12:
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif r < 2022 or r > 2030:
        t1.delete("1.0", END)
        t1.insert(END, s)
        return

    else:
        t1.delete("1.0", END)
        t1.insert(END, "Username of the person:\t\t" + a+"\n")
        t1.insert(END, "Name of the person:\t\t" + b+"\n")
        t1.insert(END, "Type of event:\t\t" + c + "\n")
        t1.insert(END, "Event budget:\t\t" + d+"\n")
        t1.insert(END, "Event Manager:\t\t" + e+"\n")
        t1.insert(END, "Date of the event:\t\t" + f+'-'+g+'-'+h+"\n")
        t1.insert(END, "Event location:\t\t" + g+"\n")
        t1.insert(END, "Contact details:\t\t" + h)
        return


def store():
    a = username.get()
    b = name_of_user.get()
    c = event.get()
    d = budget.get()
    e = manager.get()
    f = date1.get()
    g = date2.get()
    h = date3.get()
    i = location.get()
    j = telephone.get()
    k = "Enter full data"
    m = "Invalid contact detail"
    n = str(f+'-'+g+'-'+h)
    o = "Invalid date entered"
    p = int(f)
    q = int(g)
    r = int(h)
    s = "Year not valid"

    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "" or j == "" or f == '0' or g == '0' or h == '0' or d == '0':
        t1.delete("1.0", END)
        t1.insert(END, k)
        return

    elif len(j) != 10:
        t1.delete("1.0", END)
        t1.insert(END, m)
        return

    elif len(f) not in range(1, 3) or len(g) not in range(1, 3) or len(h) != 4:
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 32) and (q == 1 or q == 3 or q == 5 or q == 7 or q == 8 or q == 10 or q == 12):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 31) and (q == 4 or q == 6 or q == 9 or q == 11):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 29) and (q == 2) and (r == 2022 or r == 2023 or r == 2025 or r == 2026 or r == 2027 or r == 2029 or r == 2030):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif p not in range(1, 30) and (q == 2) and (r == 2024, r == 2028):
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif q < 0 or q > 12:
        t1.delete("1.0", END)
        t1.insert(END, o)
        return

    elif r < 2022 or r > 2030:
        t1.delete("1.0", END)
        t1.insert(END, s)
        return

    else:
        if c == 'Birthday':
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Birthday.csv', 'a+', newline="") as fh:
                writer = csv.writer(fh)
                a = [a, b, c, d, e, n, i, j]
                writer.writerow(a)
        elif c == "Marriage":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Marriage.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                b = [a, b, c, d, e, n, i, j]
                writer.writerow(b)
        elif c == "Corporate Meeting":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Corporate Meeting.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                c = [a, b, c, d, e, n, i, j]
                writer.writerow(c)
        elif c == "Informal Get Together":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Informal Get Together.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                d = [a, b, c, d, e, n, i, j]
                writer.writerow(d)
        elif c == "Conference":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Conference.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                f = [a, b, c, d, e, n, i, j]
                writer.writerow(f)
        elif c == "Seminar":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Seminar.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                g = [a, b, c, d, e, n, i, j]
                writer.writerow(g)
        elif c == "Award shows and competition":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Award shows and competition.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                h = [a, b, c, d, e, n, i, j]
                writer.writerow(h)
        elif c == "Charity event":
            with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Events\\Charity.csv', 'a+', newline="") as m:
                writer = csv.writer(m)
                i = [a, b, c, d, e, n, i, j]
                writer.writerow(i)


def delete():
    username.set("")
    name_of_user.set("")
    l5_entry.current(0)
    budget.set("")
    l7_entry.current(0)
    date1.set("")
    date2.set("")
    date3.set("")
    location.set("")
    telephone.set("")
    t1.delete("1.0", END)


def inform():
    a = username.get()
    b = name_of_user.get()
    c = event.get()
    d = budget.get()
    e = manager.get()
    f = date1.get()
    g = date2.get()
    h = date3.get()
    i = location.get()
    j = telephone.get()
    n = str(f+'-'+g+'-'+h)
    z = [a, b, c, d, e, n, i, j]

    k = str(b + " "+","+"an user of our programm has an event that is to be managed by you." + " "+"The event is that of a" + " "+c+"."+" "+"They have a budget of" +
            " "+d+"."+" "+"The following event is to be held on"+" "+n+" "+"at"+" "+i+"."+" "+"The contact details of the following user is" + " " + j+".")
    if e == 'Spartacus Edmundo':
        email_sender = 'test163773@gmail.com'
        email_password = 'sunlmdmrewkhcqpp'

        email_receiver = 'adhinbinoy7@gmail.com'

        subject = 'New event order for Spartacus Edmundo'
        body = k

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        t1.delete("1.0", END)
        t1.insert(END, "Mail has been sent")

        with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Spartacus_Edmundo.csv', 'a+') as fh:
            write = csv.writer(fh)
            write.writerow(z)

    if e == 'Maram Balder':
        email_sender = 'test163773@gmail.com'
        email_password = 'sunlmdmrewkhcqpp'

        email_receiver = 'adhin10v@gmail.com'

        subject = 'New event order for Maram Balder'
        body = k

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        t1.delete("1.0", END)
        t1.insert(END, "Mail has been sent")

        with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Maram_Balder.csv', 'a+') as fh:
            write = csv.writer(fh)
            write.writerow(z)

    if e == 'Husam Mirosław':
        email_sender = 'test163773@gmail.com'
        email_password = 'sunlmdmrewkhcqpp'

        email_receiver = 'doblessjope@gmail.com'

        subject = 'New event order for Husam Mirosław'
        body = k

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        t1.delete("1.0", END)
        t1.insert(END, "Mail has been sent")

        with open('C:\\Users\\lenovo\\OneDrive\\Desktop\\Managers\\Husam_Mirosław.csv', 'a+') as fh:
            write = csv.writer(fh)
            write.writerow(z)

def exit1():
    screen5.destroy()

def event_database():
    global screen5,username,name_of_user,event,budget,manager,date1,date2,date3,location
    global telephone,l1,f1,l2,l3,l3_entry,l4_entry,l5,l5_entry,l6,l6_entry
    global l7,l7_entry,l8,l8_entry,l9,l9_entry,l10,l10_entry,l11,t1
    screen5=Toplevel(screen)
    screen5.title('Event database')
    screen5.geometry("900x443")
    username = StringVar()
    name_of_user = StringVar()
    event = StringVar()
    budget = StringVar()
    manager = StringVar()
    date1 = StringVar()
    date2 = StringVar()
    date3 = StringVar()
    location = StringVar()
    telephone = StringVar()

    reg = screen5.register(correct)

    l1 = Label(screen5, bd=10, relief=RIDGE, text="EVENT DATABASE", font=(
    "TkDefaultFont", 30, "bold")).pack(side=TOP, fill=X)

    f1 = Frame(screen5, bd=10, relief=RIDGE)
    f1.place(x=0, y=70, width=900, height=300)

    l2 = Label(f1, text='Details about the event',
    font=("TkDefaultFont", 14, "bold"))
    l2.grid(row=0, column=1)

    l3 = Label(f1, text='Username of the user', font=(
    "TkDefaultFont", 13))
    l3.grid(row=1, column=0)

    l3_entry = Entry(f1, textvariable=username, width=25)
    l3_entry.grid(row=1, column=1)

    l4 = Label(f1, text='Full name of the user', font=(
    "TkDefaultFont", 13))
    l4.grid(row=2, column=0)

    l4_entry = Entry(f1, textvariable=name_of_user, width=25)
    l4_entry.grid(row=2, column=1)

    l5 = Label(f1, text='Event to be planned', font=(
    "TkDefaultFont", 13))
    l5.grid(row=3, column=0)

    l5_entry = ttk.Combobox(f1, textvariable=event, state='readonly', width=22)
    l5_entry["values"] = ("", "Birthday", 'Marriage', 'Corporate Meeting', 'Informal Get together',
      'Conference', 'Seminar', 'Award shows and competition', 'Charity event',)
    l5_entry.grid(row=3, column=1)

    l6 = Label(f1, text='Budget for the event', font=(
    "TkDefaultFont", 13))
    l6.grid(row=4, column=0)

    l6_entry = Entry(f1, textvariable=budget, width=25)
    l6_entry.grid(row=4, column=1)
    l6_entry.config(validate="key", validatecommand=(reg, '%P'))

    l7 = Label(f1, text='Name of the manager', font=(
    "TkDefaultFont", 13))
    l7.grid(row=5, column=0)

    l7_entry = ttk.Combobox(f1, textvariable=manager, width=22, state='readonly')
    l7_entry["values"] = ("", "Spartacus Edmundo",
      "Maram Balder", "Husam Mirosław")
    l7_entry.grid(row=5, column=1)

    l8 = Label(f1, text='Date of the event(dd/mm/yy)', font=(
    "TkDefaultFont", 13))
    l8.grid(row=6, column=0)

    l8_entry1 = Entry(screen5, textvariable=date1, width=8)
    l8_entry1.place(x=253, y=238)
    l8_entry1.config(validate="key", validatecommand=(reg, '%P'))

    l8_entry2 = Entry(screen5, textvariable=date2, width=7)
    l8_entry2.place(x=310, y=238)
    l8_entry2.config(validate="key", validatecommand=(reg, '%P'))

    l8_entry3 = Entry(screen5, textvariable=date3, width=7)
    l8_entry3.place(x=363, y=238)
    l8_entry3.config(validate="key", validatecommand=(reg, '%P'))

    l9 = Label(f1, text='Location of the event', font=(
    "TkDefaultFont", 13))
    l9.grid(row=7, column=0)

    l9_entry = Entry(f1, textvariable=location, width=25)
    l9_entry.grid(row=7, column=1)

    l10 = Label(f1, text='Mobile number', font=(
    "TkDefaultFont", 13))
    l10.grid(row=8, column=0)

    l10_entry = Entry(f1, textvariable=telephone, width=25)
    l10_entry.grid(row=8, column=1)
    l10_entry.config(validate="key", validatecommand=(reg, '%P'))

    l11 = Label(screen5, text='Details overview',
    font=("TkDefaultFont", 14, "bold"))
    l11.place(x=600, y=80)

    t1 = Text(screen5, width=45)
    t1.place(x=500, y=120, height=220)

    f2 = Frame(screen5, bd=10, relief=RIDGE)
    f2.place(x=0, y=370, width=900, height=73)

    f2_button1 = Button(f2, text="Data overview", font=(
    "TkDefaultFont", 13), width=18, height=2, command=overview)
    f2_button1.grid(row=0, column=0)

    f2_button2 = f2_button1 = Button(f2, text="Store Data", font=(
    "TkDefaultFont", 13), width=18, height=2, command=store)
    f2_button2.grid(row=0, column=1)

    f2_button3 = f2_button1 = Button(f2, text="Clear Data", font=(
    "TkDefaultFont", 13), width=18, height=2, command=delete)
    f2_button3.grid(row=0, column=2)

    f2_button4 = f2_button1 = Button(f2, text="Inform Event manager", font=(
    "TkDefaultFont", 13), width=19, height=2, command=inform)
    f2_button4.grid(row=0, column=3)


    f2_button5 = Button(f2, text="Exit", font=(
    "TkDefaultFont", 13), width=19, height=2,command=exit1)
    f2_button5.grid(row=0, column=4)
            
    

def managers():
    screen6 = Toplevel(screen)
    global b,name_of_manager,manager_inf
    screen6.geometry("660x400")
    screen6.title('Event manager data')
    name_of_manager = StringVar()
    a = Label(screen6, text="Select the manager's name",
              font=("times new roman", 12, "bold"))
    a.place(x=0, y=10)
    
    b = ttk.Combobox(screen6, font=("times new roman", 12, "bold"), width=33,
                     state='readonly', textvariable=name_of_manager)
    b["values"] = ("", "Spartacus Edmundo",
                   "Maram Balder", "Husam Mirosław")
    b.place(x=200, y=10)
    
    c = Button(screen6, text="Enter", width=20,command=manager_data)
    c.place(x=500, y=10)
    
    manager_inf = Text(screen6,width=81)
    manager_inf.place(x=1, y=40, height=355)
        
    

def registration():
    u1 = reg_username.get()
    u2 = reg_password.get()
    u3 = reg_age.get()
    u4 = reg_gender.get()
    a = os.listdir('C:\\Users\\lenovo\\OneDrive\\Desktop\\Accounts\\')
    b = str(u1+'.txt')
    c=str("C:\\Users\\lenovo\\OneDrive\\Desktop\\Accounts\\" + u1 + ".txt")
    
    if u1 == "" or u2 == "" or u3 == "" or u4 == "":
        reg_notif.config(text="All fields are necessary",fg="red")
        return

    elif len(a) == 0:
        with open(c,'w') as fh:
                fh.write(u1+'\n')
                fh.write(u2+'\n')
                fh.write(u3+'\n')
                fh.write(u4)
                reg_notif.config(fg="green", text="Account has been created")
                screen1.after(1000, lambda: screen1.destroy())
                return
        
    for i in a:
        if b in a:
            reg_notif.config(fg="red", text="Account already exists")
            return
        else:
            with open(c,'w') as fh:
                fh.write(u1+'\n')
                fh.write(u2+'\n')
                fh.write(u3+'\n')
                fh.write(u4)
                reg_notif.config(fg="green", text="Account has been created")
                screen1.after(1000, lambda: screen1.destroy())
                return
    
def register():
    global screen1,reg_username,reg_password,reg_age,reg_gender
    global username_reg,password_reg,age_reg,reg_notif
    screen1 = Toplevel(screen)
    screen1.title("Registration page")
    screen1.geometry('450x300')

    reg = screen1.register(correct)
    
    reg_username = StringVar()
    reg_password = StringVar()
    reg_age = StringVar()
    reg_gender = StringVar()
    
    Label(screen1, text="Please enter details necessary for registration below").pack()
    Label(screen1, text="Characters are not case sensitive").pack()
    Label(screen1, text="Note: No changes can be made later on to your registration details").pack()
    Label(text="").pack()
    
    Label(screen1, text="Username").pack()
    username_reg = Entry(screen1, textvariable=reg_username)
    username_reg.pack()
    
    Label(screen1, text="Password").pack()
    password_reg = Entry(screen1, textvariable=reg_password, show='*')
    password_reg.pack()
    
    Label(screen1, text="Age").pack()
    age_reg = Entry(screen1, textvariable=reg_age)
    age_reg.config(validate="key", validatecommand=(reg, '%P'))
    age_reg.pack()
    
    Label(screen1, text="Gender").pack()
    gender_reg = Entry(screen1, textvariable=reg_gender)
    gender_reg.pack()
    
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width="10",
           height="1",command=registration).pack()
    
    reg_notif = Label(screen1)
    reg_notif.pack()

def delete1():
    applicant_name.set("")
    applicant_date.set("")
    applicant_month.set("")
    applicant_year.set("")
    applicant_address.set("")
    applicant_mobile.set("")
    applicant_email.set("")
    text_1.delete("1.0", END)
    
    

def enter1():
    a1 = applicant_name.get()
    b1 = applicant_date.get()
    c1 = applicant_month.get()
    d1 = applicant_year.get()
    e1 = applicant_address.get()
    f1 = applicant_mobile.get()
    g1 = applicant_email.get()
    h1 = int(b1)
    i1 = int(c1)
    j1 = int(d1)
    k1=text_1.get("1.0", 'end-1c')

    if a1 == "" or b1 == "" or c1 == "" or d1 == "" or e1 == "" or f1 == "" or g1 == "" or k1=="":
        job_notif.config(fg="red",text="Enter the full data")
        return

    elif len(f1)!=10:
        job_notif.config(fg="red",text="Enter a valid mobile number")
        return

    elif len(b1) not in range(1,3) or len(c1) not in  range(1,3) or len(d1) != 4:
        job_notif.config(fg="red",text="Enter a valid date of birth")
        return

    elif c1 == 0 or d1 == 0 or b1 == 0 or g1 == 0:
        job_notif.config(fg="red",text="Fields cannot be zero")
        return

    elif i1 < 0 or i1 > 12:
        job_notif.config(fg="red",text="Invalid month")
        return


    elif h1 not in range(1, 32) and (i1 == 1 or i1 == 3 or i1 == 5 or i1 == 7 or i1 == 8 or i1 == 10 or i1 == 12):
        job_notif.config(fg="red",text="Invalid date")
        return

    elif h1 not in range(1, 31) and (i1  == 4 or i1  == 6 or i1 == 9 or i1 == 11):
        job_notif.config(fg="red",text="Invalid date")
        return


    elif j1 not in range (1970,2005):
        job_notif.config(fg="red",text="You are too young to apply")
        return

    else:
        m1= str(a1+" "+"would like to apply for job in your company"+"."+" "+"The date of birth of the following person is on" + " " + b1+"-"+c1+"-"+d1+"."+" "+"They live at the following address" + " "+ e1 +"."+" "+"The applicants mobile number and email address are respectively"+" "+f1+" "+"and"+" "+g1+"."+" "+"They prior knowlege and experience in this field is" +" "+k1+".")
        email_sender = 'test163773@gmail.com'
        email_password = 'sunlmdmrewkhcqpp'

        email_receiver = 'adhinbinoy7@gmail.com'

        subject = 'New job applicant details'
        body = m1

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        job_notif.config(fg="green",text="You job applicant has been received")
        

def job():
    global screen,applicant_name,job_notif,text_1,applicant_date,applicant_month,applicant_year,applicant_address,applicant_mobile,applicant_email
    screen8 = Toplevel(screen)
    screen8.geometry('900x443')
    screen8.title('job information')

    reg = screen8.register(correct)

    applicant_name=StringVar()
    applicant_date=StringVar()
    applicant_month=StringVar()
    applicant_year=StringVar()
    applicant_address=StringVar()
    applicant_mobile=StringVar()
    applicant_email=StringVar()
    job_knowledge=StringVar()

    label_1 = Label(screen8, bd=10, relief=RIDGE, text="JOB APPLICATION", font=(
    "TkDefaultFont", 30, "bold")).pack(side=TOP, fill=X)

    frame_1 = Frame(screen8, bd=10, relief=RIDGE)
    frame_1.place(x=0, y=70, width=900, height=300)

    label_2 = Label(frame_1, text='Applicant details',
    font=("TkDefaultFont", 14, "bold"))
    label_2.grid(row=0, column=0)

    label_3 = Label(frame_1, text='Name of the applicant', font=(
    "TkDefaultFont", 13))
    label_3.grid(row=1, column=0)

    label_3_entry = Entry(frame_1, textvariable=applicant_name, width=25)
    label_3_entry.grid(row=1, column=1)


    label_4 = Label(frame_1 , text = 'Date of birth of applicant(dd/mm/yy)' , font=(
    "TkDefaultFont", 13))
    label_4.grid(row=2,column=0)

    label_4_1_entry = Entry(frame_1, textvariable=applicant_date, width=8)
    label_4_1_entry.place(x=270,y=60)
    label_4_1_entry.config(validate="key", validatecommand=(reg, '%P'))

    label_4_2_entry = Entry(frame_1, textvariable=applicant_month, width=8)
    label_4_2_entry.place(x=320,y=60)
    label_4_2_entry.config(validate="key", validatecommand=(reg, '%P'))

    label_4_3_entry=Entry(frame_1, textvariable=applicant_year, width=8)
    label_4_3_entry.place(x=370,y=60)
    label_4_3_entry.config(validate="key", validatecommand=(reg, '%P'))

    label_5 = Label(frame_1 , text = 'Address' , font=(
    "TkDefaultFont", 13))
    label_5.grid(row=3,column=0)

    label_5_entry = Entry(frame_1, textvariable=applicant_address, width=25)
    label_5_entry.grid(row=3, column=1)

    label_6 = Label(frame_1 , text = 'Mobile number' , font=(
    "TkDefaultFont", 13))
    label_6.grid(row=4,column=0)

    label_6_entry = Entry(frame_1, textvariable=applicant_mobile, width=25)
    label_6_entry.grid(row=4, column=1)
    label_6_entry.config(validate="key", validatecommand=(reg, '%P'))

    label_7 = Label(frame_1 , text = 'Email address' , font=(
    "TkDefaultFont", 13))
    label_7.grid(row=5,column=0)

    label_7_entry = Entry(frame_1, textvariable=applicant_email, width=25)
    label_7_entry.grid(row=5, column=1)

    button_1 = Button(screen8,text="Enter",command=enter1,width=12)
    button_1.place(x=100,y=260)

    button_2=Button(screen8,text="Delete",command=delete1,width=12)
    button_2.place(x=320,y=260)

    label_8 = Label(screen8, text='Job Qualifications and Prior knowledge of field',
    font=("TkDefaultFont", 14, "bold"))
    label_8.place(x=450, y=80)

    text_1 = Text(screen8, width=45)
    text_1.place(x=500, y=120, height=220)

    job_notif=Label(screen8)
    job_notif.place(x=400,y=400)

    

    
    

def gologin():
    u1 = log_username.get()
    u2 = log_password.get()
    a = os.listdir('C:\\Users\\lenovo\\OneDrive\\Desktop\\Accounts\\')
    b = str(u1+'.txt')
    c=str("C:\\Users\\lenovo\\OneDrive\\Desktop\\Accounts\\" + u1 + ".txt")

    if u1 == "" or u2 == "":
        login_notif.config(text="Please enter the full data", fg="red")
        return
    
    else:
        for i in a:
            if b not in a:
                login_notif.config(text="No such account exists", fg="red")
                return
            else:
                with open(c,'r') as file:
                    file_data = file.read()
                    file_data = file_data.split('\n')
                    j = file_data[1]

                    if u2 == j:
                        screen2.destroy()
                        screen2.destroy()
                        screen3 = Toplevel(screen)
                        screen3.title('Account Dashoard')
                        screen3.geometry('600x300')
                        Label(screen3, text="Welcome to your account dashboard"+" "+u1).pack()
                        Label(screen3, text="").pack()
                    
                        Label(screen3, text="Here is a list of things you might want to check out").pack()
                        Label(screen3, text="").pack()

                        Button(screen3, text="User details", width="15",
                           height="1",command=userinfo).pack()
                        Label(screen3, text="").pack()

                        Button(screen3, text="Event database", width="15",
                           height="1",command=event_database).pack()
                        Label(screen3, text="").pack()

                        Button(screen3, text="Event Managers",
                           height="1",width=15,command=managers).pack()
                        Label(screen3, text="").pack()

                        Button(screen3, text="Issue a complaint",
                           height="1",width=15,command=complain).pack()
                        Label(screen3, text="").pack()

                        Button(screen3, text="Job at the company",
                           height="1",width=15,command=job).pack()
                        return
                    
                    else:
                        login_notif.config(
                        text="Password entered is incorrect", fg='red')
                        return
    

def login():
    global screen2,log_username,log_password,username_log,password_log,login_notif
    screen2 = Toplevel(screen)
    screen2.geometry('300x180')
    
    log_username = StringVar()
    log_password = StringVar()
    
    Label(screen2, text="Please enter details").pack()
    Label(text="").pack()
    
    Label(screen2, text="Username").pack()
    username_log = Entry(screen2, textvariable=log_username)
    username_log.pack()
    
    Label(screen2, text="Password").pack()
    password_log = Entry(screen2, textvariable=log_password, show='*')
    password_log.pack()
    
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width="10",
           height="1", command=gologin).pack()
    
    login_notif = Label(screen2)
    login_notif.pack()


Label(text="Please click one of the following options to continue",
      font='16', width='300', height='2').pack()
Label(text="").pack()

Button(text="Login", height="2", width="30",command=login).pack()
Label(text="").pack()

Button(text="Register", height="2", width="30",command=register).pack()

screen.mainloop()
