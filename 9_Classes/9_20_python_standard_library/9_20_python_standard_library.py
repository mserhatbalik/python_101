# We can also use standard functions and methods that come with python which are written by other programmers.
# It is also possible to download additional libraries to use other people's classes and methods which excel at specific kind of task.

# We imported the "random" module from Python Standard Library. Normally we cannot use randint() method without importing this module.
from random import randint

print(randint(1, 6))

# We import the choice() method from random module. This method takes a list or tuple and returns a random element from them.
from random import choice

my_tuple =("apple", "orange", "banana", "watermelon", "cherry", "lemon", "fig",)
print(choice(my_tuple))