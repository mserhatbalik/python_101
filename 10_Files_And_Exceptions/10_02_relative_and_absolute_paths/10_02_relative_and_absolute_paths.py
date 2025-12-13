from pathlib import Path

# ABSOLUTE PATH
# We can specify the exact location of the folder
path = Path("C:/Users/mserh/PycharmProjects/python_crash_course/python_work/text_files/pi_digits.txt")

# RELATIVE PATH
# Or we can specify a relative path by using ".." notation to go backwards in folders how many times we want from the current folder and find our file.
path = Path("../../python_work/text_files/pi_digits.txt")
contents = path.read_text().strip()
print(contents)