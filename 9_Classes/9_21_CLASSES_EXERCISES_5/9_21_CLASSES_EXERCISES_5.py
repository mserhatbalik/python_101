"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
# import dice
#
# six_sided_dice = dice.Dice()
# print("*********************")
# for _ in range(0, 10):
#     print(six_sided_dice.roll_die())
#
# ten_sided_dice = dice.Dice()
# print("*********************")
# for _ in range(0, 10):
#     ten_sided_dice.set_sides(10)
#     print(ten_sided_dice.roll_die())
#
# twenty_sided_dice = dice.Dice()
# print("*********************")
# for _ in range(0, 10):
#     twenty_sided_dice.set_sides(20)
#     print(twenty_sided_dice.roll_die())

"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
"""

# from lottery import Lottery as LT
#
# lottery_characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]
# my_lottery = LT(lottery_characters)
# print(my_lottery.hitbig())


"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

# from lottery import Lottery as LT
#
# my_ticket = [3, 5, "a", "d"]
# won_lottery = LT().hitbig()
# counter = 1
#
# while won_lottery != my_ticket:
#     won_lottery = LT().hitbig()
#     counter += 1
#
# print(f"In order to hit lottery, we had to pull numbers {counter} times")

"""
9-16. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. 
Go to https://pymotw.com and look at the table of contents. Find a module that looks interesting to you and read about it, 
perhaps starting with the random module.
"""