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


# We can use INHERITANCE to create parent/child relationship between classes.
class ElectricCar(Car): # This line tells the Python to create an "ElectricCar" class which inherits all properties of the "Car" class
    def __init__(self, make, model, year): # This is the initialization method of the "ElectricCar" class.
        # The idea below is to use super() with .__init__(args) to tell parent class to create a new instance of the "Car" class with the
        # specified arguments, so that instance of the "Car" class can be used as a child object in the "ElectricCar" class and be expanded upon.
        super().__init__(make, model, year)

# Because we have inherited all the methods and properties of the Car class, we can use all of those methods and properties in ElectricCar class.
my_car = ElectricCar("tesla", "t", "2025")
print(my_car.get_descriptive_name())