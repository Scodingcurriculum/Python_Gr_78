import tkinter as tk
from tkinter import messagebox

class Profile:
    def __init__(self, name="", age=0, favorite_color="", hobby=""):
        self.__name = name
        self.__age = age
        self.__favorite_color = favorite_color
        self.__hobby = hobby

    def update_profile(self, name, age, favorite_color, hobby):
        self.__name = name
        self.__age = age
        self.__favorite_color = favorite_color
        self.__hobby = hobby

    def get_info(self):
        return (f"Name: {self.__name}\n"
                f"Age: {self.__age}\n"
                f"Favorite Color: {self.__favorite_color}\n"
                f"Hobby: {self.__hobby}")

class ProfileApp:
    def __init__(self, root):
        self.profile = Profile()
        self.root = root
        self.root.title("Kids Profile App")
        self.root.geometry("500x300")
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.age_label = tk.Label(root, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()
        self.color_label = tk.Label(root, text="Favorite Color:")
        self.color_label.pack()
        self.color_entry = tk.Entry(root)
        self.color_entry.pack()
        self.hobby_label = tk.Label(root, text="Hobby:")
        self.hobby_label.pack()
        self.hobby_entry = tk.Entry(root)
        self.hobby_entry.pack()
        self.save_button = tk.Button(root, text="Save Profile", command=self.save_profile)
        self.save_button.pack()
        self.show_button = tk.Button(root, text="Show Profile", command=self.show_profile)
        self.show_button.pack()
        self.info_label = tk.Label(root, text="", justify=tk.LEFT)
        self.info_label.pack()

    def save_profile(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        favorite_color = self.color_entry.get()
        hobby = self.hobby_entry.get()

        if name and age.isdigit() and favorite_color and hobby:
            self.profile.update_profile(name, int(age), favorite_color, hobby)
            messagebox.showinfo("Success", "Profile saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields with valid information.")

    def show_profile(self):
        info = self.profile.get_info()
        self.info_label.config(text=info)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
