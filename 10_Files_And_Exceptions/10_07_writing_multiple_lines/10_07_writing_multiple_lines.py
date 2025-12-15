# Writing multiple lines is similar to writing a single line.
# The main difference is that we add attach new line to our main content for every single line

from pathlib import Path

path = Path("../../python_work/text_files/learning_python_multi_line.txt")

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

# write_text() method always overwrites previous content.
path.write_text(contents)