# Be careful when using "double quotes" with 'single quotes'
# In order to properly let Python interpreter to determine your string, you should use single quotes inside double quotes or visa-versa.

# This is the wrong way of doing it.
# welcome_message = 'Hello Mr. 'George', welcome to our house.'

# This is the proper way of using double quotes with single quotes
welcome_message = "Hello Mr. 'George', welcome to our house."
print(welcome_message)
