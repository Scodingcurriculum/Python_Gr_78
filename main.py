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
def handle_waste(waste_item):
    print(waste_item.process_waste())

# Example usage
plastic = PlasticWaste(10)  # 10 kg of plastic waste
organic = OrganicWaste(5)   # 5 kg of organic waste
ewaste = EWaste(2)          # 2 kg of e-waste
# Handle each type of waste
handle_waste(plastic)
handle_waste(organic)
handle_waste(ewaste)


