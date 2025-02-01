from tkinter import *
root=Tk()
root.geometry("350x350")
root.title("Login window")

lbl_un=Label(root,text="Enter Username: ")
lbl_pswd=Label(root,text="Enter Password: ")
lbl_status=Label(root)

ip_un=Entry(root)
ip_pswd=Entry(root,show="*")

database = {"Smiley":"Smiley@123","Rockstar":"rockY#2012", "funTym":"Enjoy345!"}
def login():
    username = ip_un.get()
    password = ip_pswd.get()
    for key in database.keys():
        if username == key and password==database.get(username):
            lbl_status["text"]="User Verified"
            break
        else:
            lbl_status["text"]="User Not Verified"
    clear_ip()   

#Additional Activity
def signup():
    username = ip_un.get()
    password = ip_pswd.get()
    flag=0
    for key in database.keys():
        if username == key:
            lbl_status["text"]="User Already Exists"
            break
        else:
            flag=1
    if flag==1:
        database[username]=password
        lbl_status["text"]="User Added"  
        print(database)    
    clear_ip()
        
def clear_ip():
    ip_un.delete(0, END)
    ip_pswd.delete(0, END)
    
      
lbl_un.place(relx=0.5,rely=0.2,anchor=CENTER)
ip_un.place(relx=0.5,rely=0.3,anchor=CENTER)

lbl_pswd.place(relx=0.5,rely=0.4,anchor=CENTER)
ip_pswd.place(relx=0.5,rely=0.5,anchor=CENTER)

lbl_status.place(relx=0.5,rely=0.6,anchor=CENTER)
btn_Login=Button(root,text="Login",command=login)
btn_Login.place(relx=0.6,rely=0.7,anchor=CENTER)

btn_SignUp=Button(root,text="Sign Up",command=signup)
btn_SignUp.place(relx=0.4,rely=0.7,anchor=CENTER)

root.mainloop()