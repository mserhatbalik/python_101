"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually and then call both methods.
"""

# class Restaurant:
#     """A class that represents a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"Restaurant's name is {self.restaurant_name.title()}. It's cuisine type is {self.cuisine_type.title()}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is now open and accepting customers.")
#
# sushico = Restaurant("sushico", "japanese food")
# baydoner = Restaurant("baydöner", "anatolian food")
# pizza_bulls = Restaurant("pizza bulls", "italian food")
#
# sushico.open_restaurant()
# sushico.describe_restaurant()
#
# baydoner.open_restaurant()
# baydoner.describe_restaurant()
#
# pizza_bulls.open_restaurant()
# pizza_bulls.describe_restaurant()



"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, 
and call describe_restaurant() for each instance.
"""


# DONE


"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

class User:
    def __init__(self, first_name, last_name, email, gender, age):
        """Defining a new user class for regular website users"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.age = age

    def describe_user(self):
        """Printing summary of user information"""
        print("Printing the user information.")
        print(f"\t-First Name: {self.first_name.title()}")
        print(f"\t-Last Name: {self.last_name.title()}")
        print(f"\t-Email: {self.email}")
        print(f"\t-Age: {self.age}")
        print(f"\t-Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. Welcome to our website!")

serhat = User("serhat", "balık", "serb@gmail.com", "m", "40")
jessica = User("jessica", "brown", "jesb@hotmail.com", "f", "24")

serhat.greet_user()
serhat.describe_user()

jessica.greet_user()
jessica.describe_user()