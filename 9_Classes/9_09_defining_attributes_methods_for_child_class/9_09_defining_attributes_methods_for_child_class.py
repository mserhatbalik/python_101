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

    def update_odometer(self,
                        kms):  # We create a method to change the odometer INDIRECTLY. This allows us additional operations before assignment.
        """Set the odometer reading to the given value"""
        if self.odometer_reading < kms:
            self.odometer_reading = kms

    def increase_odometer(self, kms):
        self.odometer_reading += kms

# Defining an ElectricCar class inherited from Car class
class ElectricCar(Car):
    # Initialize the attributes of the ElectricCar class
    def __init__(self, make, model, year):
        # Initialize the attributes inherited from the parent class using the arguments passed in ElectricCar initialization method.
        super().__init__(make, model, year)

        # We are creating a new property specific to the child class.
        # ElectricCar class has this property, but Car class do not.
        self.battery_size = 40

    def describe_battery(self):
        """Returns a result describing the battery_size property"""
        return f"This car has {self.battery_size}-kWh battery."


my_car = ElectricCar("tesla", "model t", "2025")
print(my_car.get_descriptive_name())
print(my_car.describe_battery())


















