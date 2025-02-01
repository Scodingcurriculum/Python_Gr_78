from tkinter import *
root=Tk()
root.geometry("350x350")
root.title("Welcome window")

e=Entry(root)
e.pack()

label=Label(root, text="Enter your name and Press the button")
label.pack()

def display():
    label['text']="Welcome to Tkinter "+e.get()

btn=Button(root,text="Click Me",command=display)
btn.pack()
root.mainloop()

