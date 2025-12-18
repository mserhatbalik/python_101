# We use try/except/else blocks to encapsulate our code blocks to handle possible errors proactively.

print("Give me two numbers")
while True:
    first_number = input("First number. Type 'q' to quit\n")
    if first_number == "q":
        break
    second_number = input("Give me second number. Type 'q' to quit\n")
    if second_number == "q":
         break

    # try block is the operation we want to check for. We should not have any other code in this block other than the one we want to check for errors.
    try:
        division = int(first_number)/int(second_number)

    # "except" block can have or not have a specific error type to check for. It depends on us to check for what specifically.
    # In this case we check if the operation above causes the specified error type in this block.
    except ZeroDivisionError:
        print("You can't divide a number with zero!")

    # If everything working as expected, python will skip the "except" block and run the "else" block, which is usually the case.
    else:
        print(f"Division is {division}")