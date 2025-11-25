# We can ask for multiple inputs a fill a dictionary member with each iteration using the while loop

responses = {}
active = True

while active:
    name = input("What is your name?\n")
    response = input("Where would you like to visit?\n")
    responses[name.title()] = response.title()

    repeat = input("Would you like to let another person respond? (yes/no)\n")
    if repeat == "no":
        active = False

for key, value in responses.items():
    print(f"The person {key} likes to visit {value}")