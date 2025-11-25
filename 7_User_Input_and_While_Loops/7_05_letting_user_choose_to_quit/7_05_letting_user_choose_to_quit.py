# Unless designed specifically, console programs stop running after the first execution.
# While loops let us run the program indefinately unless user specify otherwise.

prompt = "Tell me something, and I will spit it back to you!\n"
prompt += "You can type 'quit' whenever you wish to stop the program.\n"

message = ""
while message != "quit":
    message = input(prompt)
    print(message)