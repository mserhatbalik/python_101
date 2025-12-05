# In some cases, we might define a default value for a specific class object during initialization.

class Car:
    """Defining a Car class"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name

    def read_odometer(self):
        return f"This car has {self.odometer_reading} kms on it."

    def update_odometer(self, kms):  # We create a method to change the odometer INDIRECTLY. This allows us additional operations before assignment.
        """Set the odometer reading to the given value"""
        if self.odometer_reading < kms:
            self.odometer_reading = kms

    def increase_odometer(self, kms):
        self.odometer_reading += kms


my_new_car = Car("Porsche", "911 turbo s", "2026")
her_new_car = Car("BYD", "seal u dm-i", "2026")
moms_new_car = Car("audi", "q6 suv e-tron", "2026")

### MY CAR ###
print(my_new_car.get_descriptive_name())
# We can change an object's properties DIRECTLY
my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())


### HER CAR ###
print(her_new_car.get_descriptive_name())
# We can change an object's properties through METHODS
her_new_car.update_odometer(10)
her_new_car.update_odometer(12)
her_new_car.update_odometer(5) # We can't roll back the odometer because of the if/else check we did in the method.
print(her_new_car.read_odometer())


### MOM's CAR ###
print(moms_new_car.get_descriptive_name())
print(moms_new_car.read_odometer())
moms_new_car.increase_odometer(15) # Increment the odometer
moms_new_car.increase_odometer(845) # Increment the odometer
print(moms_new_car.read_odometer())