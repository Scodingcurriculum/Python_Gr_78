#Actual LOC = 50
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Identify the Words from Emojis!")
root.geometry("500x500")
# List of image paths
image_paths = ["D:/moonKey.PNG","D:/B@.PNG","D:/chorse.PNG"]
answers=["monkey","bat","sea horse"]
index = 0
def load_image(image_path):
    image = Image.open(image_path)
    image = image.resize((200, 200))
    return ImageTk.PhotoImage(image)
def update_image():
    global index
    image_path = image_paths[index]
    photo = load_image(image_path)
    image_label.config(image=photo)
    image_label.image = photo
    reset()
def show_prev_image():
    global index
    index = (index - 1) % len(image_paths)
    update_image()
def show_next_image():
    global index
    index = (index + 1) % len(image_paths)
    update_image()
def reset():
    e.delete(0, END)
    lstat.config(text="")
# Add image label
image_label = Label(root)
image_label.pack()
#Add entry to write the image name
e=Entry(root)
e.pack()
#Add label to display the status 
lstat=Label(root)
lstat.pack()
def check():
    img_name=e.get().lower()
    if img_name==answers[index]:
        lstat["text"]="Correct"
    else:
        lstat["text"]="Wrong!\n"+"Correct answer is "+answers[index]
 #Add button to chek the image name
btn_check=Button(root,text="CHECK",comman=check)
btn_check.pack()
# Add buttons to navigate through images
prev_button = Button(root, text="<<", command=show_prev_image)
prev_button.pack(side=LEFT)

next_button = Button(root, text=">>", command=show_next_image)
next_button.pack(side=RIGHT)
# Load the first image
update_image()
# Start the Tkinter main loop
root.mainloop()
