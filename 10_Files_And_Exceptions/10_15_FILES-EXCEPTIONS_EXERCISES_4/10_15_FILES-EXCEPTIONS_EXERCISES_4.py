"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file.
Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”
"""
# from pathlib import Path
# import json
#
# # PROGRAM 1
# path = Path("favorite_number.json")
# favorite_number = input("What is your favorite number?\n")
# content = json.dumps(favorite_number)
# path.write_text(content)
#
# # PROGRAM 2
# path = Path("favorite_number.json")
# content = path.read_text()
# favorite_number = json.loads(content)
# converted_number = int(favorite_number)
# print(f"“I know your favorite number! It’s {converted_number}.”")


"""
10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. 
If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. 
Run the program twice to see that it works.
"""

# from pathlib import Path
# import json
#
# path = Path("favorite_number.json")
#
# def ask_number(path):
#
#     favorite_number = input("What is your favorite number?\n")
#     content = json.dumps(favorite_number)
#     path.write_text(content)
#
#
# def read_number(path):
#     content = path.read_text()
#     favorite_number = json.loads(content)
#     print(f"I know your favorite number! It’s {favorite_number}.")
#
# def favorite(path):
#     if path.exists():
#         read_number(path)
#     else:
#         ask_number(path)
#
# favorite(path)

"""
10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. 
Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. 
Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). 
Print a summary showing exactly what your program remembers about the user.
"""
# from pathlib import Path
# import json
#
# def create_user(path):
#     user_name = input("What is your name?\n")
#     email = input("What is your email?\n")
#     country = input("Which country you reside in?\n")
#     user_info = {"user_name": user_name, "email": email, "country": country}
#     content = json.dumps(user_info)
#     path.write_text(content)
#
#
# def initialize_user(path):
#     if path.exists():
#         content = path.read_text(encoding="utf-8")
#         user_info = json.loads(content)
#         for key, value in user_info.items():
#             print(f"\t-{key} = {value}")
#     else:
#         create_user(path)
#
# path = Path("user_info.json")
# initialize_user(path)

"""
10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username,
 or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
If it’s not, call get_new_username() to get the correct username.
"""

from pathlib import Path
import json

def create_user(path):
    print("You information is not saved in our systems.")
    user_name = input("What is your name?\n")
    email = input("What is your email?\n")
    country = input("Which country you reside in?\n")
    user_info = {"user_name": user_name, "email": email, "country": country}
    content = json.dumps(user_info)
    path.write_text(content)


def initialize_user(username, path):
    if path.exists():
        content = path.read_text(encoding="utf-8")
        user_info = json.loads(content)
        if user_info["user_name"] == username:
            for key, value in user_info.items():
                print(f"\t-{key} = {value}")
        else:
            create_user(path)
    else:
        create_user(path)


def greet_user(path):
    username = input("What is your username?\n")
    initialize_user(username, path)

path = Path("user_info.json")
greet_user(path)
