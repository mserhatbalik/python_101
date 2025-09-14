# In python, it is possible to use specific mechanisms to manipulate data we are referring to.
# The mechanism we talk about are called "methods" in programming.
# print() method was the first we used, which helps us print certain text on to screen.
# title() method is used to manipulate the data it is used on to change the first letters of text to uppercase.
# In this case, title() method is used by chaining it to the data we want to manipulate.
# By doing this we tell the python interpreter to make title() method to act on the name variable.
# Every method uses parantheses, which usually accepts additional data or parameters for the method to work
# In this case title() method doesn't require any additional information, so we leave the parantehes empty.

# title()
name = "serhat balık"
print(name.title())

# upper()
print(name.upper())

# lower()
print(name.lower())
