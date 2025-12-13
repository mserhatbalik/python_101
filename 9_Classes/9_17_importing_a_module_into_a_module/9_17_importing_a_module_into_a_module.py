# We import everything from the electric_car module, but because we have also imported Car module in electric_car module, we
# can also access both modules properties and methods.

import electric_car

my_car = electric_car.Car("Porsche", "911 Turbo S", "2026")
her_car = electric_car.ElectricCar("BYD", "Seal U DM-i", "2026")

print(my_car.get_descriptive_name())
print(her_car.get_descriptive_name())