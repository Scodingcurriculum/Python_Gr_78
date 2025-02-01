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

class Vihaan(Profile):
    def __init__(self):
        super().__init__("Vihaan",12,"Black,Purple","Soccer")

class Virti(Profile):
    def __init__(self):
        super().__init__("Virti",10,"Red, Pink, Lemon","Painting")

print("\n\n----------Student Details---------")
student1=Vihaan()
print(student1.get_info())
print("\n\n----------------------------------")
student2=Virti()
print(student2.get_info())


