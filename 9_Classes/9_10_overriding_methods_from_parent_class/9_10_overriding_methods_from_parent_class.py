class Car:
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

    def update_odometer(self, kms):
        if self.odometer_reading < kms:
            self.odometer_reading = kms

    def increase_odometer(self, kms):
        self.odometer_reading += kms

    # The method for filling the gas tank of a Car object.
    def fill_gas_tank(self):
        print(f"Filling the gas tank of {self.get_descriptive_name()}")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        return f"This car has {self.battery_size}-kWh battery."

    def fill_gas_tank(self):
        """Overriding the method of the parent class"""
        print("This is an electric car. It does not have a tank!")


my_car = ElectricCar("tesla", "model t", "2025")
print(my_car.get_descriptive_name())
print(my_car.describe_battery())
my_car.fill_gas_tank()
