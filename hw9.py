from tkinter import *
root=Tk()
root.geometry("350x350")
root.title("Addition Window")

e1=Entry(root)
e1.pack()

e2=Entry(root)
e2.pack()

label=Label(root, text="Result Appears here")
label.pack()

def addition():
    n1=float(e1.get())
    n2=float(e2.get())
    ans=n1+n2
    label['text']= str(ans)
    
btn=Button(root,text="Add",command=addition)
btn.pack()
root.mainloop()