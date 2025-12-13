# We can also give modules or classes inside modules specific aliases

### ALIAS FOR MODULES ###

# import electric_car as ec
#
# my_car = ec.Car("Porsche", "911 Turbo S", "2026")
# her_car= ec.ElectricCar("BYD", "Seal U DM-i", "2026")
#
# print(my_car.get_descriptive_name())
# print(her_car.get_descriptive_name())

##############################################################

### ALIAS FOR CLASSES ###
from electric_car import ElectricCar as EC, Car as C

my_car = C("Porsche", "911 turbo s", "2026")
her_car = EC("BYD", "Seal U DM-i", "2026")

print(my_car.get_descriptive_name())
print(her_car.get_descriptive_name())