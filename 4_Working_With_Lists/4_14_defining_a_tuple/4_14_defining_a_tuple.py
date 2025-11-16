# TUPLES are similar to lists in structure, but with one defining different charactristic.
# We cannot change the value of items inside a tuple after it is defined. There is an exception in the next section about this, which will be clarified.

# We use () when defining a tuple instead of [] which is used while defining a list.
dimensions = (200, 40)
print(dimensions)

# Accessing an item inside a tuple is similar to accessing an item inside a list
print(dimensions[0])
print(dimensions[1])

# Getting an error when we try to change a value inside a tuple
# dimensions[1] = 60

# Defining a tuple with a single element REQUIRES a "," COMMA in order to work.
# This happens when we are creating a tuple from scratch during program run time, and in order to prevent getting an error we must use "," while defining the first element.
coordinates = (5738128,)
print(coordinates[0])
