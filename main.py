#Actual LOC = 50
from tkinter import *
from PIL import Image, ImageTk
import time 

root=Tk()
root.title("Identify the Super Heroes!")
root.geometry("500x500")
# List of image paths
image_paths = ["D:/cap_am.jpg","D:/fantastic.jpg","D:/batman.jpg"]
image_list=[ "captain america", "fantastic","batman"]
index = 0
score =0
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
#Add Score label
score_label=Label(root,text="Score: 0", font=("Arial", 24))
score_label.place(relx=0.5,rely=0.9,anchor=CENTER)
score =0
def check():
    global score
    img_name=e.get().lower()
    if img_name==image_list[index]:
        lstat["text"]="Correct"
        score=score+1
        score_label["text"]= "Score "+ str(score)
        time.sleep(2)
        show_next_image()
    else:
        lstat["text"]="Wrong!\n"+"Correct answer is "+image_list[index]
        time.sleep(2)
        show_next_image()
          
#Add button to chek the image name
btn_check=Button(root,text="CHECK",command=check)
btn_check.place(relx=0.5,rely=0.6,anchor=CENTER)
# Add buttons to navigate through images
prev_button = Button(root, text="<<", command=show_prev_image)
prev_button.place(relx=0.2,rely=0.5,anchor=CENTER)
next_button = Button(root, text=">>", command=show_next_image)
next_button.place(relx=0.8,rely=0.5,anchor=CENTER)
# Load the first image
update_image()
# Start the Tkinter main loop
root.mainloop()

