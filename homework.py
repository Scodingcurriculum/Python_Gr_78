# Parent class: Delivery
class Delivery:
    def __init__(self, delivery_address, distance_km, rate_per_km):
        self.delivery_address = delivery_address
        self.distance_km = distance_km
        self.rate_per_km = rate_per_km

    def calculate_delivery_cost(self):
        return round(self.distance_km * self.rate_per_km, 2)  # Cost = distance * rate per km

    def process_delivery(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child class: FoodDelivery
class FoodDelivery(Delivery):
    def __init__(self, delivery_address, distance_km, food_item, restaurant_name):
        super().__init__(delivery_address, distance_km, rate_per_km=1.5)  # $1.5 per km for food
        self.food_item = food_item
        self.restaurant_name = restaurant_name

    def process_delivery(self):
        return (f"Delivering food item '{self.food_item}' from {self.restaurant_name} to {self.delivery_address}. "
                f"Distance: {self.distance_km} km. Delivery cost: ${self.calculate_delivery_cost()}.")

# Child class: GroceryDelivery
class GroceryDelivery(Delivery):
    def __init__(self, delivery_address, distance_km, grocery_list):
        super().__init__(delivery_address, distance_km, rate_per_km=1.0)  # $1 per km for groceries
        self.grocery_list = grocery_list

    def process_delivery(self):
        items = ", ".join(self.grocery_list)
        return (f"Delivering groceries: {items} to {self.delivery_address}. "
                f"Distance: {self.distance_km} km. Delivery cost: ${self.calculate_delivery_cost()}.")

# Child class: ParcelDelivery
class ParcelDelivery(Delivery):
    def __init__(self, delivery_address, distance_km, parcel_weight_kg):
        super().__init__(delivery_address, distance_km, rate_per_km=2.0)  # $2 per km for parcels
        self.parcel_weight_kg = parcel_weight_kg

    def process_delivery(self):
        return (f"Delivering a parcel weighing {self.parcel_weight_kg} kg to {self.delivery_address}. "
                f"Distance: {self.distance_km} km. Delivery cost: ${self.calculate_delivery_cost()}.")

# Function to process deliveries using polymorphism
def handle_delivery(delivery_item):
    print(delivery_item.process_delivery())

# Example usage
food_delivery = FoodDelivery("123 Elm Street", 5, "Pizza", "Mario's Pizzeria")
grocery_delivery = GroceryDelivery("456 Oak Avenue", 3, ["Milk", "Eggs", "Bread"])
parcel_delivery = ParcelDelivery("789 Pine Road", 8, 2.5)  # Parcel weighs 2.5 kg

# Handle each type of delivery
handle_delivery(food_delivery)
handle_delivery(grocery_delivery)
handle_delivery(parcel_delivery)