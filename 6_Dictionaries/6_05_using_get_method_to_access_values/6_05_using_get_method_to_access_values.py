# There is another way to access values of keys in dictionaries, which is helpful in some cases.
# When we use dictonary["key"] format in order to access a value,
# If there is no key with that name, Python will throw an error and crash your program

car = {"brand": "porsche", "model":"911 turbo s", "topspeed": 412, "color": "", "year": 2020}

# Python throws an error, because there is not "key" named "horsepower" in car dictionary
# print(car["horsepower"])

# To overcome this problem we can use the get() method
# print(car.get("horsepower"))

# If we specify a second parameter, the second parameter will return as a "default value" instead of "None"
print(car.get("horsepower", "There is no key named 'horsepower' in this dictionary"))