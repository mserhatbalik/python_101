"""
7-1. Rental Car: Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as “Let me see if I can find you a Subaru.”
"""
# car = input("Please enter your requested car.\n")
# print(f"Let me check if I can find a {car.title()}.")

"""
7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
# seats = int(input("Hello. How many people are in your dinner group?"))
#
# if seats > 8:
#     print("Currently our big tables are full, please wait.")
# else:
#     print("Your table is ready!")


"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""

multiples = int(input("Give me a number\n"))

if multiples % 10 == 0:
    print("Your number is a multiples of 10")
else:
    print("Give me another number to check if it is multiples of 10")
