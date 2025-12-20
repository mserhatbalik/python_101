# We use json.dumps() function to serialize any data into a JSON format.
# The operation after the serialization step is the same as before. We write the "serialized JSON data" onto the path we provided.

from pathlib import Path
import json

path = Path("../../python_work/json_files/numbers.json")
content = json.dumps([2, 5, 9, 1, 19, 23, 4])
path.write_text(content)