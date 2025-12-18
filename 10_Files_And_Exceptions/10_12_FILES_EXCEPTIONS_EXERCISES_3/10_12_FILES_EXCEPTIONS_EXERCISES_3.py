"""
10-6.	Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message.
Test your program by entering two numbers and then by entering some text instead of a number.
"""
# try:
#     first_number = input("Give me the first number.\n")
#     second_number = input("Give me the second number.\n")
#     sum = int(first_number) + int(second_number)
# except ValueError:
#     print("type a number")
# else:
#     print(sum)

"""
10-7.	Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, 
even if they make a mistake and enter text instead of a number.
"""

# sum = 0
# while True:
#     number = input("Give me a number to add.\n")
#     try:
#         sum += int(number)
#     except ValueError:
#         pass
#     else:
#         print(sum)

"""
10-8.	Cats and Dogs: Make two files, cats.txt and dogs.txt. 
Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to
 read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, 
 and print a friendly message if a file is missing. Move one of the files to a different location on your system, 
 and make sure the code in the except block executes properly.
"""

# from pathlib import Path
#
# dogs = "golden retriever\n"
# dogs += "german shepherd\n"
# dogs += "bulldog\n"
# cats = "siamese\n"
# cats += "persian\n"
# cats += "bengal\n"
#
# dog_path = Path("../../python_work/text_files/dogs.txt")
# dog_path.write_text(dogs)
# cat_path = Path("../../python_work/text_files/cats.txt")
# cat_path.write_text(cats)
#
# try:
#     print(dog_path.read_text())
#     print(Path("../../python_work/text_files/catss.txt").read_text())
# except FileNotFoundError:
#     print("file not found")

"""
10-9.	Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail silently if either file is missing.
"""

# from pathlib import Path
#
# dogs = "golden retriever\n"
# dogs += "german shepherd\n"
# dogs += "bulldog\n"
# cats = "siamese\n"
# cats += "persian\n"
# cats += "bengal\n"
#
# dog_path = Path("../../python_work/text_files/dogs.txt")
# dog_path.write_text(dogs)
# cat_path = Path("../../python_work/text_files/cats.txt")
# cat_path.write_text(cats)
#
# try:
#     print(dog_path.read_text())
#     print(Path("../../python_work/text_files/catss.txt").read_text())
# except FileNotFoundError:
#     pass




"""
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find a few texts you’d like to analyze. 
Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
You can use the count() method to find out how many times a word or phrase appears in a string. 
For example, the following code counts the number of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.
Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. 
This will be an approximation because it will also count words such as 'then' and 'there'. 
Try counting 'the ', with a space in the string, and see how much lower your count is.
"""

from pathlib import Path

path = Path("../../python_work/text_files/illiad.txt")

contents = path.read_text(encoding="utf-8")
count = contents.lower().count("the ")
print(count)