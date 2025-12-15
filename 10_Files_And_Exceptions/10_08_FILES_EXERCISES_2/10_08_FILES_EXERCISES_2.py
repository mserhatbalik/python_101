"""
10-4.	Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
"""

# import pathlib
#
# path = pathlib.Path("../../python_work/text_files/guest.txt")
# name = input("What is your name?\n")
# path.write_text(f"{name}\n")


"""
10-5.	Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, 
and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
"""

from pathlib import Path

path = Path("../../python_work/text_files/guest_book.txt")
content = ""
while True:
    name = input("Please enter a guest name. If every guest name is entered, type 'quit' to exit the program.\n")
    if name == "quit":
        break

    content += f"{name}\n"
path.write_text(content)