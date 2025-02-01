from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Identify the Super Heroes!")
root.geometry("500x500")

# Add image label
image_label = Label(root)
image_label.pack()

#Add entry to write the image name
e=Entry(root)
e.pack()

#Add label to display the status 

lstat=Label(root)
lstat.pack()


#Add button to chek the image name
btn_check=Button(root,text="CHECK",command=check)
btn_check.place(relx=0.5,rely=0.3,anchor=CENTER)
# Add buttons to navigate through images
prev_button = Button(root, text="<<", command=show_prev_image)
prev_button.place(relx=0.2,rely=0.5,anchor=CENTER)

next_button = Button(root, text=">>", command=show_next_image)
next_button.place(relx=0.5,rely=0.5,anchor=CENTER)


# Start the Tkinter main loop
root.mainloop()
