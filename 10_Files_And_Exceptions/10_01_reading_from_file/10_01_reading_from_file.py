# We use "Path" class from "pathlib" module for reading writing related operations.
from pathlib import Path

# The default pathing for files is the "current" folder that the scripts run.
# Below we initialize the "Path" class with the "file" we want to work with.
path = Path("pi_digits.txt")

# We use the "read_text()" method of the Path class which returns the text content of the file we have initialized this object.
# We can also chain the strip() method to remove any whitespaces from the left and side of the content we read from the file.
contents = path.read_text().strip()

print(contents)