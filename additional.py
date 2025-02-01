# Parent class: Waste
class Waste:
    def __init__(self, weight_kg, rate_per_kg):
        self.weight_kg = weight_kg
        self.rate_per_kg = rate_per_kg

    def process_waste(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_cost(self):
        return round(self.weight_kg * self.rate_per_kg, 2)  # Cost = weight * rate per kg

# Child class: PlasticWaste
class PlasticWaste(Waste):
    def __init__(self, weight_kg):
        super().__init__(weight_kg, rate_per_kg=2.0)  # $2 per kg for plastic waste

    def process_waste(self):
        return (f"Processing {self.weight_kg} kg of plastic waste. "
                f"It will be recycled into reusable products. "
                f"Cost: ${self.calculate_cost()}.")

# Child class: OrganicWaste
class OrganicWaste(Waste):
    def __init__(self, weight_kg):
        super().__init__(weight_kg, rate_per_kg=1.0)  # $1 per kg for organic waste

    def process_waste(self):
        return (f"Processing {self.weight_kg} kg of organic waste. "
                f"It will be converted into compost. "
                f"Cost: ${self.calculate_cost()}.")

# Child class: EWaste
class EWaste(Waste):
    def __init__(self, weight_kg):
        super().__init__(weight_kg, rate_per_kg=5.0)  # $5 per kg for e-waste

    def process_waste(self):
        return (f"Processing {self.weight_kg} kg of e-waste. "
                f"Recovering precious metals and disposing of hazardous materials. "
                f"Cost: ${self.calculate_cost()}.")

# Function to handle waste using polymorphism
def handle_waste(waste_item, quantity):
    total_cost = waste_item.calculate_cost() * quantity
    print(f"{waste_item.process_waste()} Total cost for {quantity} items: ${total_cost}.\n")

# User Input System
def main():
    print("Welcome to the Smart Waste Management System!")
    print("Waste types: 1. Plastic  2. Organic  3. E-Waste")
    
    waste_type = int(input("Enter the waste type (1/2/3): "))
    weight_kg = float(input("Enter the weight of waste (in kg): "))
    quantity = int(input("Enter the number of units: "))

    # Create the appropriate waste object based on user input
    if waste_type == 1:
        waste = PlasticWaste(weight_kg)
    elif waste_type == 2:
        waste = OrganicWaste(weight_kg)
    elif waste_type == 3:
        waste = EWaste(weight_kg)
    else:
        print("Invalid waste type! Exiting...")
        return

    # Handle the waste and calculate the cost
    handle_waste(waste, quantity)

# Run the program
if __name__ == "__main__":
    main()
