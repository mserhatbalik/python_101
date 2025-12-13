# In some cases the incoming data might be structured in a way where each line represents a section of information.
# We can store each line in a list and loop over them to work with them individually using the "splitlines()" method of Path class.

from pathlib import Path

file = Path("../../python_work/text_files/pi_digits.txt")
content = file.read_text().strip()
content_lines_list = content.splitlines()
print(content_lines_list)