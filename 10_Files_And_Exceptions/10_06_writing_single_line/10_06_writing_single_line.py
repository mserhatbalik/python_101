# It is also possible to write a text content into a file.

from pathlib import Path

# Even if there is no file, it will create a new one with the name we've defined in the path object
path = Path("../../python_work/text_files/programming.txt")
path.write_text("I love programming!!")