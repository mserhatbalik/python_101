# In some cases, we might define a default value for a specific class object during initialization.

class Car:
    """Defining a Car class"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # We can create additional properties for the object apart from outside parameters. Also, we can set the value for it.

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name

    def read_odometer(self):
        return f"This car has {self.odometer_reading} kms on it." 

my_new_car = Car("Porsche", "911 turbo s", "2026")
her_new_car = Car("BYD", "seal u dm-i", "2026")


print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

print(her_new_car.get_descriptive_name())