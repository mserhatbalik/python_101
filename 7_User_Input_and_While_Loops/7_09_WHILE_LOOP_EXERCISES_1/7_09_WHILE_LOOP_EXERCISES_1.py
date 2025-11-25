"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""
# prompt = "Please enter your pizza topping.\n"
# prompt += "(Prompt 'quit' in order to top the program)\n"
#
# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"I will add {topping} on to your pizza!")
#     else:
#         break


"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
"""

# prompt = "What is your age? Type 'quit' to end the program.\n"
#
# while True:
#     age = input(prompt)
#     if age == "quit":
#         break
#     elif int(age) < 3:
#         print("You are a baby. Movie ticket is free for you.\n")
#     elif 3 <= int(age) < 12:
#         print("You are a child and your ticket fee is $10.\n")
#     else:
#         print("Your ticket fee is $15.\n")

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""

# prompt = "What is your age? Type 'quit' to end the program.\n"
#
# age = ""
# while age != 'quit':
#     age = input(prompt)
#
#     if age != 'quit':
#         if int(age) < 3:
#             print("You are a baby. Movie ticket is free for you.\n")
#         elif 3 <= int(age) < 12:
#             print("You are a child and your ticket fee is $10.\n")
#         else:
#             print("Your ticket fee is $15.\n")


# prompt = "What is your age? Type 'quit' to end the program.\n"
#
# active = True
#
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     elif int(age) < 3:
#         print("You are a baby. Movie ticket is free for you.\n")
#     elif 3 <= int(age) < 12:
#         print("You are a child and your ticket fee is $10.\n")
#     elif int(age) > 12:
#         print("Your ticket fee is $15.\n")


"""
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)
"""

while True:
    print("infinity...")