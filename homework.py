# Parent class: Vehicle
class Vehicle:
    def __init__(self, make, model, distance_from_user, speed_kmh, base_fare):
        self.make = make
        self.model = model
        self.distance_from_user = distance_from_user  # Distance in kilometers
        self.speed_kmh = speed_kmh  # Speed in kilometers per hour
        self.base_fare = base_fare  # Base fare for the ride (per km)

    def time_to_reach(self):
        # Time = Distance / Speed
        time_in_hours = self.distance_from_user / self.speed_kmh
        time_in_minutes = time_in_hours * 60  # Convert to minutes
        return round(time_in_minutes, 2)  # Return time rounded to 2 decimal places

    def calculate_cost(self, distance_to_destination):
        # Total cost = base fare * total distance (to pick up + to destination)
        total_distance = self.distance_from_user + distance_to_destination
        return round(self.base_fare * total_distance, 2)

    def describe(self):
        time = self.time_to_reach()
        return (f"This is a {self.make} {self.model} located {self.distance_from_user} km away. "
                f"It will take approximately {time} minutes to reach you.")

# Child class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, distance_from_user, speed_kmh, base_fare, seating_capacity, driver_name):
        super().__init__(make, model, distance_from_user, speed_kmh, base_fare)
        self.seating_capacity = seating_capacity
        self.driver_name = driver_name

    def describe(self):
        return (f"{super().describe()} It has {self.seating_capacity} seats. "
                f"Your driver is {self.driver_name}.")

# Child class: Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, make, model, distance_from_user, speed_kmh, base_fare, helmet_included, driver_name):
        super().__init__(make, model, distance_from_user, speed_kmh, base_fare)
        self.helmet_included = helmet_included
        self.driver_name = driver_name

    def describe(self):
        helmet_info = "comes with a helmet" if self.helmet_included else "does not include a helmet"
        return (f"{super().describe()} It {helmet_info}. "
                f"Your driver is {self.driver_name}.")

# Let's create some vehicles for the ride-sharing app
car = Car("Toyota", "Camry", 2.5, 60, 10, 5, "Alice")  # Base fare 10 per km
bike = Bike("Yamaha", "FZ", 1.2, 40, 5, True, "Bob")  # Base fare 5 per km

# Distance to the destination
distance_to_destination = 8  # in kilometers

# Print details about the vehicles, including cost
print(car.describe())
print(f"The ride cost for the car will be ${car.calculate_cost(distance_to_destination)}.\n")

print(bike.describe())
print(f"The ride cost for the bike will be ${bike.calculate_cost(distance_to_destination)}.\n")

