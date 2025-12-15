# We can read every single line and append stripped text to create one long line of text.
from pathlib import Path

path = Path("../../python_work/text_files/pi_digits.txt")

content = path.read_text()
lines = content.splitlines()
full_text = ""
for line in lines:
    full_text += line.strip() # This part is important to strip the white space at the start of each line, which was essentially a new line (\n) before starting the splitline() operation.

full_text = full_text
print(full_text)