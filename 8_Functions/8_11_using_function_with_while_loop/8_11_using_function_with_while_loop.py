# We can also call functions in a loop, stop it with a break statement when necessary

def greet_user(f_name, l_name):
    full_name = f"Hello {f_name} {l_name}"
    return full_name.title()

while True:
    print("Type 'q' anytime you want to stop the program")
    first_name = input("What is your first name?\n")
    if first_name == "q":
        break
    last_name = input("What is your last name?\n")
    if last_name == "q":
        break
    message = greet_user(first_name, last_name)
    print(message)