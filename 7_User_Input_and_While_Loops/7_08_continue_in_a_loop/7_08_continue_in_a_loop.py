# continue statement works similar to break statement, but it does not stop the while loop,
# it just goes back to the beginning of the loop without executing the rest of the code after the continue statement.
#

number = 0
while number < 10:
    number += 1

    if number % 2 == 0:
        continue # if the number is EVEN, then go back to the beginning of the loop, and SKIP the print(number) statement
    print(number)
