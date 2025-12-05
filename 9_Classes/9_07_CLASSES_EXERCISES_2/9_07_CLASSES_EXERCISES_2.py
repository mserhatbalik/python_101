"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
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
# sushico = Restaurant("sushico", "japanese food")
# baydoner = Restaurant("baydöner", "anatolian food")
# pizza_bulls = Restaurant("pizza bulls", "italian food")
#
# sushico.describe_restaurant()
# sushico.open_restaurant()
# sushico.number_served = 25
# print(f"{sushico.restaurant_name.title()} has now served {sushico.number_served} customers.\n")
#
#
# baydoner.describe_restaurant()
# baydoner.open_restaurant()
# baydoner.set_number_served(89)
# print(f"{baydoner.restaurant_name.title()} has now served {baydoner.number_served} customers.\n")
#
#
# pizza_bulls.describe_restaurant()
# pizza_bulls.open_restaurant()
# pizza_bulls.increment_number_served(10)
# pizza_bulls.increment_number_served(11)
# pizza_bulls.increment_number_served(42)
# print(f"{pizza_bulls.restaurant_name.title()} has now served {pizza_bulls.number_served} customers.\n")




"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
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
# serhat = User("serhat", "balık", "serb@gmail.com", "m", "40")
# jessica = User("jessica", "brown", "jesb@hotmail.com", "f", "24")
#
# serhat.greet_user()
# serhat.describe_user()
# serhat.increment_login_attempts()
# serhat.increment_login_attempts()
# serhat.print_login_attempts()
#
# jessica.greet_user()
# jessica.describe_user()
# jessica.increment_login_attempts()
# jessica.print_login_attempts()
# jessica.increment_login_attempts()
# jessica.print_login_attempts()
# jessica.reset_login_attempts()
# jessica.print_login_attempts()

