from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Base class
class Planet:
    def __init__(self, name, distance_from_sun, diameter, moons):
        self.__name = name
        self.__distance_from_sun = distance_from_sun
        self.__diameter = diameter
        self.__moons = moons

    def get_info(self):
        return (f"Planet: {self.__name}\n"
                f"Distance from Sun: {self.__distance_from_sun} million km\n"
                f"Diameter: {self.__diameter} km\n"
                f"Moons: {self.__moons}")

# Derived classes for specific planets (if needed)
class Earth(Planet):
    def __init__(self):
        super().__init__("Earth", 149.6, 12742, 1)

class Mars(Planet):
    def __init__(self):
        super().__init__("Mars", 227.9, 6779, 2)

class Jupiter(Planet):
    def __init__(self):
        super().__init__("Jupiter", 778.3, 139820, 79)

# Create a Tkinter application
class PlanetApp:
    def __init__(self, root):
        self.planets = {
            "Earth": Earth(),
            "Mars": Mars(),
            "Jupiter": Jupiter()
        }
        global index
        self.img_name=["Earth","Jupiter","Mars"]
        self.img_list=["D:\earth.png","D:\jupiter.png","D:\mars.png"]
        self.root = root
        self.root.title("Planet Info App")
        self.root.geometry("400x500")
        
        # Create a dropdown menu for selecting a planet
        self.planet_var = StringVar(value="Select a Planet")
        self.planet_menu = OptionMenu(root, self.planet_var, *self.planets.keys())
        self.planet_menu.place(relx=0.5,rely=0.2,anchor=CENTER)

        # Create a button to show planet info
        self.show_info_button = Button(root, text="Show Info", command=self.show_info)
        self.show_info_button.place(relx=0.5,rely=0.3,anchor=CENTER)

        # Label to display planet info
        self.image_label = Label(root)
        self.image_label.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.info_label = Label(root, text="", justify=LEFT)
        self.info_label.place(relx=0.5,rely=0.7,anchor=CENTER)

         
    def show_info(self):
        planet_name = self.planet_var.get()
        if planet_name in self.planets and planet_name in self.img_name:
            planet = self.planets[planet_name]
            info = planet.get_info()
            self.info_label.config(text=info)
            self.index=self.img_name.index(planet_name)
            image = Image.open(self.img_list[self.index])
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            messagebox.showerror("Error", "Please select a valid planet.")
if __name__ == "__main__":
    root = Tk()
    app = PlanetApp(root)
    root.mainloop()

