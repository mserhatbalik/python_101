# In more complicated scenarios we may need to define multiple conditions to keep the program running.
# But this will create hard to manage "while conditions", in order to overcome that problem, we use boolean variables.
#

prompt = "Tell me something, and I will spit it back to you.\n"
prompt += "Also, you can write 'quit' in order to stop the program.\n"

# We set a custom boolean variable named as "active", then set it to True
active = True

# As long as active is set to True, while loop will keep repeating.
# Also we don't need to define the statement below as "while active == True:"
# Because while and if statements checks for True by default.
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(f"{message}\n")