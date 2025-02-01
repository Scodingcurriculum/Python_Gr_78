from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Image display!")
root.geometry("500x500")
image_path = r"D:\batman.jpg"  # Replace with the path to your image file
image = Image.open(image_path)
image = image.resize((300, 300))  # Resize image if necessary
photo = ImageTk.PhotoImage(image)
# Display the image in the Tkinter window
label = Label(root, image=photo)
label.pack()
root.mainloop()



