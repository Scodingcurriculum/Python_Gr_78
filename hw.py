from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
def show_original_map():
    original_img.show()
def show_enhanced_map():
    enhanced_img.show()
# Load and process the treasure map
img_path=r"D:\map.png"
original_img = Image.open(img_path)  # Replace with your image file
enhanced_img = original_img.convert("L")      # Convert to grayscale
# Tkinter GUI setup
root = Tk()
root.title("Treasure Map Enhancer")
root.geometry("300x200")
# Welcome label
Label(root, text="Welcome to the Treasure Map Enhancer!", wraplength=250).pack(pady=10)
# Buttons to view the maps
Button(root, text="Show Original Map", command=show_original_map).pack(pady=10)
Button(root, text="Show Enhanced Map", command=show_enhanced_map).pack(pady=10)
# Run the application
root.mainloop()

