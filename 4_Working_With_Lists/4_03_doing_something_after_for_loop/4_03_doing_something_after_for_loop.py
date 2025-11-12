# We can use additional functions and methods inside a loop to automate repetitive tasks.
magicians = ["alicia", "david", "zack"]

for person in magicians:
    print(f"Congratulations {person.title()}. That was a great trick!")
    print(f"I can't wait to see your next trick {person.title()}!\n")

# The statements after the for loop which is INDENTED at the same position as the FOR LOOP statement, means the statement is outside the loop, and should not repeat.
# This is how we close a FOR LOOP.
print("Thank you all the great magicians for your performances!")