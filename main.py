class PizzaHut:
    def __init__(self):
        self.type_of_pizza = ""
        self.toppings = []
        self.base_price = 10.0  # base price for a pizza

    def set_pizza_type(self, pizza_type):
        self.type_of_pizza = pizza_type

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_bill(self):
        topping_price = 1.5  # price per topping
        total_price = self.base_price + len(self.toppings) * topping_price
        return total_price

    def display_order(self):
        print(f"Pizza Hut Order: {self.type_of_pizza} Pizza")
        if self.toppings:
              self.toppings=', '.join(self.toppings)
        else:
            print("No Toppings") 
        print(f"Total Bill: ${self.calculate_bill():.2f}")
        print()

# Create an order for Pizza Hut
p1 = PizzaHut()
print("----------------------------")
p1.set_pizza_type("Margherita")
p1.add_topping("cheese")
p1.display_order()
print("----------------------------")

p2 = PizzaHut()
print("----------------------------")
p2.set_pizza_type("veg")
p2.add_topping("olives")
p2.add_topping("mushrooms")
p2.display_order()
print("----------------------------")

