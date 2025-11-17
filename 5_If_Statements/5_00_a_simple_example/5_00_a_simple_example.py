# If/Else Statements help us create and check for certain conditions in our programs to run different steps for different conditions.

cars = ["audi", "toyota", "bmw", "mazda"]

# We define our logic as "if <value> <operator> <condition-value>:"
# Then, inside the scope of if/else statements, we define the operation we want the program to run, if the condition we defined previously is met.

# In the background these comparisons either return "True" or "False" depending on the values.

for car in cars:
    if car == "bmw":        # Our special case in this example, if we detect "bmw" in our list, then we want it to be printed in UPPER CASE.
        print(car.upper())
    else:                   # ELSE statement tells the program, if our special conditions above do not trigger,
        print(car.title())  # then the core in this block should run, which is the default logic.


