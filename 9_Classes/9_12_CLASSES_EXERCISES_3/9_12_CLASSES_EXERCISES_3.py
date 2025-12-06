"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166).
Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""
# class Restaurant:
#     """A class that represents a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"Restaurant's name is {self.restaurant_name.title()}. It's cuisine type is {self.cuisine_type.title()}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is now open and accepting customers.")
#
#     def set_number_served(self, customers):
#         self.number_served = customers
#
#     def increment_number_served(self, customers):
#         self.number_served += customers
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#
#         # Adding the flavors attribute
#         self.flavors = ["Chocolate", "Vanilla", "Cherry", "Banana", "Lemon", "Caramel"]
#
#     def display_flavors(self):
#         print("We serve the following ice cream flavors!")
#         for flavor in self.flavors:
#             print(f"\t{flavor}")
#
# my_stand = IceCreamStand("Mado", "Ice Cream")
# my_stand.describe_restaurant()
# my_stand.display_flavors()


"""
9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in 
Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
"""
# class User:
#     def __init__(self, first_name, last_name, email, gender, age):
#         """Defining a new user class for regular website users"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.gender = gender
#         self.age = age
#         self.login_attempt = 0
#
#     def describe_user(self):
#         """Printing summary of user information"""
#         print("Printing the user information.")
#         print(f"\t-First Name: {self.first_name.title()}")
#         print(f"\t-Last Name: {self.last_name.title()}")
#         print(f"\t-Email: {self.email}")
#         print(f"\t-Age: {self.age}")
#         print(f"\t-Gender: {self.gender}")
#
#     def greet_user(self):
#         print(f"Hello {self.first_name.title()} {self.last_name.title()}. Welcome to our website!")
#
#     def print_login_attempts(self):
#         print(f"Login attempts: {self.login_attempt}")
#
#     def increment_login_attempts(self):
#         self.login_attempt += 1
#
#     def reset_login_attempts(self):
#         self.login_attempt = 0
#
# class Admin(User):
#     def __init__(self, first_name, last_name, email, gender, age):
#         super().__init__(first_name, last_name, email, gender, age)
#         self.privileges = ["can add post", "can delete post", "can ban user"]
#
#     def show_privileges(self):
#         print(f"This user has the following privileges")
#         while self.privileges:
#             print(f"\t{self.privileges.pop()}")
#
# new_admin = Admin("serhat", "balık", "serb@gmail.com", "m", "40")
# new_admin.show_privileges()

"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, 
that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""
# class User:
#     def __init__(self, first_name, last_name, email, gender, age):
#         """Defining a new user class for regular website users"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.gender = gender
#         self.age = age
#         self.login_attempt = 0
#
#     def describe_user(self):
#         """Printing summary of user information"""
#         print("Printing the user information.")
#         print(f"\t-First Name: {self.first_name.title()}")
#         print(f"\t-Last Name: {self.last_name.title()}")
#         print(f"\t-Email: {self.email}")
#         print(f"\t-Age: {self.age}")
#         print(f"\t-Gender: {self.gender}")
#
#     def greet_user(self):
#         print(f"Hello {self.first_name.title()} {self.last_name.title()}. Welcome to our website!")
#
#     def print_login_attempts(self):
#         print(f"Login attempts: {self.login_attempt}")
#
#     def increment_login_attempts(self):
#         self.login_attempt += 1
#
#     def reset_login_attempts(self):
#         self.login_attempt = 0
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ["can add post", "can delete post", "can ban user"]
#
#     def show_privileges(self):
#         print(f"This user has the following privileges")
#         while self.privileges:
#             print(f"\t{self.privileges.pop()}")
#
# class Admin(User):
#     def __init__(self, first_name, last_name, email, gender, age):
#         super().__init__(first_name, last_name, email, gender, age)
#         self.privileges = Privileges()
#
#
# new_admin = Admin("serhat", "balık", "serb@gmail.com", "m", "40")
# new_admin.privileges.show_privileges()


"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity to 65 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
You should see an increase in the car’s range.
"""
# class Car:
#     def __init__(self, model, make, year):
#         self.model = model
#         self.make = make
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         return f"{self.model.title()} {self.make.title()} {self.year.title()}"
#
#     def read_odometer(self):
#         return f"This car has {self.odometer_reading} kms on it."
#
#     def update_odometer(self, kms):
#         if kms > 0:
#             self.odometer_reading = kms
#
#     def increment_odometer(self, kms):
#         if kms > 0:
#             self.odometer_reading += kms
#
#     def fill_gas_tank(self):
#         print("Filling the gas tank")
#
# class Battery():
#     def __init__(self):
#         self.battery_size = 40
#
#     def describe_battery(self):
#         print(f"This car has {self.battery_size} kWh capacity battery.")
#
#     def upgrade_battery(self):
#         if self.battery_size != 65:
#             self.battery_size = 65
#
#     def get_range(self):
#         if self.battery_size == 40:
#             range = 450
#         elif self.battery_size == 65:
#             range = 650
#
#         print(f"This car can go {range} kms on a full charge.")
#
# class ElectricCar(Car):
#     def __init__(self, model, make, year):
#         super().__init__(model, make, year)
#
#         # We define a new property as usual, but we fill it with a new object from Battery() class during ElectricCar() class initialization.
#         self.battery = Battery()
#
#
#     def fill_gas_tank(self):
#         print("This is an electric car. There is no gas tank to fill up!")
#
# her_new_car = ElectricCar("BYD", "seal u dm-i", "2026")
# her_new_car.fill_gas_tank()
# print(her_new_car.read_odometer())
# her_new_car.update_odometer(50)
# her_new_car.increment_odometer(15)
# print(her_new_car.read_odometer())
#
# # We access our Battery() class methods through dot notation and chaining.
# her_new_car.battery.describe_battery()
# her_new_car.battery.get_range()
# her_new_car.battery.upgrade_battery()
# her_new_car.battery.get_range()
