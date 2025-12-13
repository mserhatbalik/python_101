"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
"""
# from restaurant import Restaurant, IceCreamStand
#
# my_restaurant = IceCreamStand("Baklavagiller", "Dessert")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()


"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
"""

# import user as us
# user_1 = us.Admin("serhat", "balık", "serb@hotmail.com", "m", "40")
# user_1.describe_user()
# user_1.privileges.show_privileges()



"""
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
"""

# import admin
#
# user_1 = admin.Admin("serhat", "balık", "serb@hotmail.com", "m", "40")
# user_1.greet_user()
# user_1.privileges.show_privileges()