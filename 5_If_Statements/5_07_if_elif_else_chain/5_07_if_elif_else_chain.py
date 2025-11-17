# It is possible to create additional conditional operations inside if blocks with "elif" keyword.
# This means, if the "if" statement above fails, python then goes to check the next one in line, then next one, until all of the conditions are checked.

# Below is an example to check for the age of a person in an amusement park to determine their admission price.
age = 15

if age < 12:
    print("Your are a kid")
    print("You need to pay $8")
elif age >= 12 and age < 18:
    print("You are a teenager")
    print("You need to pay $14")
elif age >= 18 and age < 65:
    print("You are a big boy")
    print("You need to pay $19")
else:
    print("You are an elderly")
    print("You don't need to pay")


# Below is also a different and concise way of creating these conditional operations.
# It allows more dynamism within the code without changing every print statement with every price or age condition change.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")