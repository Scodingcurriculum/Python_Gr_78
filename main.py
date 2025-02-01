# Parent class: Vehicle
class Vehicle:
    def __init__(self, make, model, distance_from_user):
        self.make = make  
        self.model = model
        self.distance_from_user = distance_from_user  # New feature

    def describe(self):
        return f"This is a {self.make} {self.model} located {self.distance_from_user} km away."

# Child class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, distance_from_user, seating_capacity):
        super().__init__(make, model, distance_from_user)
        self.seating_capacity = seating_capacity

    def describe(self):
        return f"{super().describe()} It has {self.seating_capacity} seats."

# Child class: Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, make, model, distance_from_user, helmet_included):
        super().__init__(make, model, distance_from_user)
        self.helmet_included = helmet_included

    def describe(self):
        helmet_info = "comes with a helmet" if self.helmet_included else "does not include a helmet"
        return f"{super().describe()} It {helmet_info}."

# Let's create some vehicles for the ride-sharing app
car = Car("Toyota", "Camry", 2.5, 5)  # 2.5 km away
bike = Bike("Yamaha", "FZ", 1.2, True)  # 1.2 km away

# Print details about the vehicles
print(car.describe())
print(bike.describe())


