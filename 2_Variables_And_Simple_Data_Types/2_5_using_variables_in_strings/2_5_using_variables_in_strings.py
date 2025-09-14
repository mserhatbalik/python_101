# In some cases you will require to use variable names together with a string.
# We use name and lastname variable together in the example below to print welcome message to the user.

# In order to do that, we use the concept called "f-strings"
# Using f"<string>" lets us use curly braces {<variable>} inside that string, which in turn helps us refer to a variable inside that string.

name = "Serhat"
last_name = "Balık"
print(f"Welcome to my world {name} {last_name}!")