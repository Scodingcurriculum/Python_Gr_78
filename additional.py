# Parent class: Vehicle
class Vehicle:
    def __init__(self, make, model, distance_from_user, speed_kmh):
        self.make = make
        self.model = model
        self.distance_from_user = distance_from_user  # Distance in kilometers
        self.speed_kmh = speed_kmh  # Speed in kilometers per hour

    def time_to_reach(self):
        # Time = Distance / Speed
        time_in_hours = self.distance_from_user / self.speed_kmh
        time_in_minutes = time_in_hours * 60  # Convert to minutes
        return round(time_in_minutes, 2)  # Return time rounded to 2 decimal places

    def describe(self):
        time = self.time_to_reach()
        return (f"This is a {self.make} {self.model} located {self.distance_from_user} km away. "
                f"It will take approximately {time} minutes to reach you.")

# Child class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, distance_from_user, speed_kmh, seating_capacity):
        super().__init__(make, model, distance_from_user, speed_kmh)
        self.seating_capacity = seating_capacity

    def describe(self):
        return (f"{super().describe()} It has {self.seating_capacity} seats.")

# Child class: Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, make, model, distance_from_user, speed_kmh, helmet_included):
        super().__init__(make, model, distance_from_user, speed_kmh)
        self.helmet_included = helmet_included

    def describe(self):
        helmet_info = "comes with a helmet" if self.helmet_included else "does not include a helmet"
        return f"{super().describe()} It {helmet_info}."

# Let's create some vehicles for the ride-sharing app
car = Car("Toyota", "Camry", 2.5, 60, 5)  # 2.5 km away, speed 60 km/h
bike = Bike("Yamaha", "FZ", 1.2, 40, True)  # 1.2 km away, speed 40 km/h

# Print details about the vehicles
print(car.describe())
print(bike.describe())

