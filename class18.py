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

print("----Planet Information----\n")
print("\n\nEARTH---------")
e=Earth()
print(e.get_info())
print("\n\nMARS---------")
m=Mars()
print(m.get_info())
print("\n\nJUPITER---------")
j=Jupiter()
print(j.get_info())


