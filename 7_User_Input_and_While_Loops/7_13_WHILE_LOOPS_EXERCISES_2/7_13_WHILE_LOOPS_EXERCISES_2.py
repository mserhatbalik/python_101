"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order,
such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

# sandwich_orders = ["tuna", "beef", "chicken", "salami", "beef", "vegan"]
# finished_sandwiches = []
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich)
#
#
# for item in finished_sandwiches:
#     print(f"Your {item.title()} sandwich has been made successfully.")


"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
# sandwich_orders = ["tuna", "beef", "pastrami", "pastrami", "chicken", "salami", "pastrami", "beef", "vegan"]
# finished_sandwiches = []
#
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
#
# print(sandwich_orders)


"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.
"""

destinations = {}

while True:
    name = input("What is your name?\n")
    destination = input("If you could visit one place in the world, where would you go?\n")
    destinations[name.title()] = destination.title()

    prompt = input("Would you like to take a new poll? (yes/no)")
    if prompt == "yes":
        continue
    elif prompt == "no":
        for name, destination in destinations.items():
            print(f"{name} would like to visit {destination}.")
        break