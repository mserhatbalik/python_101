"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
"""

# def make_sandwich(*ingredients):
#     print("Making you a sandwich with following ingredients.")
#     for item in ingredients:
#         print(f"\t-{item}")
#     print("")
#
# make_sandwich("tomato", "cheese", "ketchup")
# make_sandwich("pepperoni", "salami","cheese")
# make_sandwich("salami","cheese")


"""
8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you.
"""
# def build_profile(f_name, l_name, **more_info):
#     more_info["first_name"] = f_name
#     more_info["last_name"] = l_name
#     return more_info
#
# person = build_profile("serhat", "balık", age=40, city="istanbul", sex="male")
# print(person)


"""
8-14. Cars: Write a function that stores information about a car in a dictionary.
 The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments.
  Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
   Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
"""
# def make_car(p_manufacturer, p_model, **more_info):
#     more_info["manufacturer"] = p_manufacturer
#     more_info["model"] = p_model
#     return more_info
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)