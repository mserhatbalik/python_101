class Restaurant:
    """A class that represents a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name.title()}. It's cuisine type is {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open and accepting customers.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        # Adding the flavors attribute
        self.flavors = ["Chocolate", "Vanilla", "Cherry", "Banana", "Lemon", "Caramel"]

    def display_flavors(self):
        print("We serve the following ice cream flavors!")
        for flavor in self.flavors:
            print(f"\t{flavor}")