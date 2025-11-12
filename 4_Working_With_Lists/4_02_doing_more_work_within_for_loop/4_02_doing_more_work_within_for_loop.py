# We can use additional functions and methods inside a loop to automate repetitive tasks.
magicians = ["alicia", "david", "zack"]

for person in magicians:
    print(f"Congratulations {person.title()}. That was a great trick!")
    print(f"I can't wait to see your next trick {person.title()}!\n")