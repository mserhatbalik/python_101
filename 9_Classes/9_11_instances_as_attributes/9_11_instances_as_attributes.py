class Car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.model.title()} {self.make.title()} {self.year.title()}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} kms on it."

    def update_odometer(self, kms):
        if kms > 0:
            self.odometer_reading = kms

    def increment_odometer(self, kms):
        if kms > 0:
            self.odometer_reading += kms

    def fill_gas_tank(self):
        print("Filling the gas tank")

# It is important to write the classes to the top of the classes they will be used in.
# In this case Battery() class will be used to create new attributes and methods for an ElectricCar class.
# Because the Python interpreter reads the code from Top to Bottom, ordering of the classes is important.
class Battery():
    def __init__(self):
        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has {self.battery_size} kWh capacity battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 450
        elif self.battery_size == 65:
            range = 650

        print(f"This car can go {range} kms on a full charge.")

class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)

        # We define a new property as usual, but we fill it with a new object from Battery() class during ElectricCar() class initialization.
        self.battery = Battery()


    def fill_gas_tank(self):
        print("This is an electric car. There is no gas tank to fill up!")

her_new_car = ElectricCar("BYD", "seal u dm-i", "2026")
her_new_car.fill_gas_tank()
print(her_new_car.read_odometer())
her_new_car.update_odometer(50)
her_new_car.increment_odometer(15)
print(her_new_car.read_odometer())

# We access our Battery() class methods through dot notation and chaining.
her_new_car.battery.describe_battery()
her_new_car.battery.get_range()
