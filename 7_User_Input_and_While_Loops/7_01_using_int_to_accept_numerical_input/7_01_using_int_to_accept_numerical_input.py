# The input() function always assumes the user input is a string.
# In order to take the numerical input, and use it in mathetmatical operations,
# we need to use the int() function to convert the numerical string into an integer.

print("Welcome to the voting program.")

# We can wrap and convert the input value immediately to integer if we know this will be true for all the cases, or do it in multiple steps.
age = int(input("What is your age?\n"))

# Check to see if conversion works.
print(type(age))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You a child. You can't vote. Go play with your toys!")