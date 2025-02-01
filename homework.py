class LuxuryCar:
    def __init__(self, make, model, fuel_type, cost, color):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.cost = cost
        self.color = color

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Cost: ${self.cost}")
        print(f"Color: {self.color}")

# Create instances of the LuxuryCar class
car1 = LuxuryCar("Mercedes-Benz", "S-Class", "Petrol", 110000, "Black")
car2 = LuxuryCar("BMW", "7 Series", "Diesel", 95000, "White")
car3 = LuxuryCar("Audi", "A8", "Electric", 120000, "Blue")

# Display information for each car
car1.display_info()
print()
car2.display_info()
print()
car3.display_info()


