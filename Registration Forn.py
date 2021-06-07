import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tm
from tkinter import colorchooser
from tkinter import messagebox
from tkinter.ttk import *
import pandas as pd

app= tk.Tk()
app.geometry("500x400")
app.configure(bg='light blue')

f_name=tk.StringVar()
u_name=tk.StringVar()
age=tk.StringVar()
email=tk.StringVar()
mobile=tk.StringVar()
pwd=tk.StringVar()


tk.Label(app,text="FULL NAME",bg='light blue').place(x=20,y=30)
tk.Label(app,text="USER NAME",bg='light blue').place(x=20,y=60)
tk.Label(app,text="AGE",bg='light blue').place(x=20,y=90)
tk.Label(app,text="EMAIL ID",bg='light blue').place(x=20,y=120)
tk.Label(app,text="MOBILE NO.",bg='light blue').place(x=20,y=150)
tk.Label(app,text="PASSWORD",bg='light blue').place(x=20,y=180)

tk.Entry(app,width=30,bg="#ffffff",textvariable=f_name).place(x=120,y=30)
tk.Entry(app,width=30,bg="#ffffff",textvariable=u_name).place(x=120,y=60)
tk.Entry(app,width=30,bg="#ffffff",textvariable=age).place(x=120,y=90)
tk.Entry(app,width=30,bg="#ffffff",textvariable=email).place(x=120,y=120)
tk.Entry(app,width=30,bg="#ffffff",textvariable=mobile).place(x=120,y=150)
tk.Entry(app,width=30,bg="#ffffff",textvariable=pwd,show='*').place(x=120,y=180)

def mobile_limit(mobile):
    if len(mobile.get())>10:
        messagebox.showerror("Error", "Error message")
        mobile.set(mobile.get()[:10])
mobile.trace('w',lambda *args: mobile_limit(mobile))

def age_limit(age):
    if len(age.get())>2:
        messagebox.showerror("Error", "Error message")
        age.set(age.get()[:2])
age.trace('w',lambda *args: age_limit(age))


def pwd_limit(pwd):
    if len(pwd.get())>8:
        messagebox.showerror("Error", "Error message")
        pwd.set(pwd.get()[:8])
pwd.trace('w',lambda *args: pwd_limit(pwd))



def register():

    f=open("data.csv",'a')
    data=[f_name.get(),u_name.get(),age.get(),email.get(),mobile.get(),pwd.get()]
    f.write(','.join(data)+'\n')
    f.close()
    f_name.set('')
    u_name.set('')
    age.set('')
    email.set('')
    mobile.set('')
    pwd.set('')
    
    corr=('full name','user name','AGE','email id','mobile number','password')
    df=pd.read_csv('data.csv',names=corr)
    new_df = df.dropna()
   
    #open a new window use a Toplevel function
    new_Window = tk.Toplevel(app)
    new_Window.title("RESULTS")
    new_Window.configure(bg='light goldenrod')
    # sets the geometry of toplevel
    new_Window.geometry('500x300')
  
    # A Label widget to show in toplevel
    Summary=tk.Label(new_Window,text ="SUMMARY",font=('Arial Black', 16, 'bold'),bg='light goldenrod').place(x=200,y=10)
    
    total_var=tk.Variable(app)
    Average_age_var=tk.Variable(app)
    mail_domain_var=tk.Variable(app)
    google_var=tk.Variable(app)
    yahoo_var=tk.Variable(app)
    
    total_var.set(new_df['full name'].count())
    Average_age_var.set(df['AGE'].mean())
    mail_domain_var.set(new_df['email id'].count())
    
    mail=new_df['email id']
    
    google_var.set(new_df['email id'][mail.str.endswith('@google.com')].count())
    yahoo_var.set(new_df['email id'][mail.str.endswith('@yahoo.com')].count())

    Total_user=tk.Label(new_Window,text ="Total User:",bg='light goldenrod').place(x=20,y=60)
    Average_age=tk.Label(new_Window,text ="Average Age:",bg='light goldenrod').place(x=20,y=100)
    mail_domain=tk.Label(new_Window,text ="Commonly Mail Domain:",font=('Bahnschrift SemiBold', 10, 'bold'),bg='light goldenrod').place(x=20,y=140)
    Google=tk.Label(new_Window,text ="google.com",bg='light goldenrod').place(x=50,y=180)
    yahoo=tk.Label(new_Window,text ="yahoo.com",bg='light goldenrod').place(x=50,y=220)
    
    Total_user=tk.Label(new_Window,text ="Total User:",textvariable=total_var,bg='light goldenrod').place(x=90,y=60)
    Average_age=tk.Label(new_Window,text ="Average Age:",textvariable=Average_age_var,bg='light goldenrod').place(x=120,y=100)
    mail_domain=tk.Label(new_Window,text ="Commonly Mail Domain:",textvariable=mail_domain_var,bg='light goldenrod').place(x=200,y=140)
    Google=tk.Label(new_Window,text ="google.com",textvariable=google_var,bg='light goldenrod').place(x=120,y=180)
    yahoo=tk.Label(new_Window,text ="yahoo.com",textvariable=yahoo_var,bg='light goldenrod').place(x=120,y=220)
   
    

tk.Button(app,text='SUBMIT',command=register).place(x=150,y=210)



app.mainloop()
    
