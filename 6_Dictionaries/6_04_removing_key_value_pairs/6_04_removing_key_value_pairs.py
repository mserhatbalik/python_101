# Removing keys from dicitonaries are similar to the technique we used for the lists
# "del" keyword lets us remove any key and it's associated value in a dictionary PERMANENTLY

car = {"brand": "BMW", "model": "420", "color": "Red", "topspeed": 365}
print(car)

# Removing the "color" key and it's associated value
del car["color"]

# Printing last state of the car dictionary
print(car)
