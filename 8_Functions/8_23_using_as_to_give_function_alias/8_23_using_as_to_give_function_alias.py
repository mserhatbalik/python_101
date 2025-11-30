# In some cases, the function name you import from a module might conflict with the function name from your own program.
# In such cases we can use "as" keyword while importing the function to differentiate it from other functions in your program with same name.
from pizza import make_pizza as mp


# We are using the new alias we gave to make_pizza function from the pizza module we have imported
mp("medium", "pepperoni", "jambon", "cheese")
mp("small", "cheese", "mushrooms")