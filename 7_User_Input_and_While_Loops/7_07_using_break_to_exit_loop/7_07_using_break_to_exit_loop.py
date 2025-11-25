# We also use "break" statement to stop and get out of the loop immediately.
# break statement allows us to control the flow of our while loops

prompt = "Tell me you favorite country.\n"
prompt += "(You can write 'quit' in order to stop the program)\n"


# In some cases we don't even need to use variable. Just using True in a while statement will suffice.
while True:
    country = input(prompt)

    if country == 'quit':
        break
    else:
        print(f"I love {country.title()}\n")