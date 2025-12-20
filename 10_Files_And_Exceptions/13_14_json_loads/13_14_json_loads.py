# We use json.loads() function in order to deserialize upcoming data.

from pathlib import Path
import json

path = Path("../../python_work/json_files/numbers.json")
content = path.read_text(encoding="utf-8")

# Without the following step, python will just read the text. However, it will not create a python object,
# so we cannot access individual list items just using content[0] or content[2],
# because python can't decide if the [2, 5, 9, 1, 19, 23, 4] data is a list or just a series of characters starting with "[" bracket.
#  To make this text a workable python object, we need to change its format to JSON, by using json.loads() function
numbers = json.loads(content)
print(content)