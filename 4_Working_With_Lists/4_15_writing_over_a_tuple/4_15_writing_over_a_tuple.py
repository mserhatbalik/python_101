# We can't change the existing tuples, BUT we can change the variable name to point to a new tuple in the memory.

dimensions = (400, 200)
print(dimensions)

# Assignment below will throw an error, because we're trying to change the (400, 200) tuple. This is not possible.
# dimensions[1] = 500

# What is possible is, we can create a new tuple and assign this tuple to our previous tuple variable name "dimensions"
dimensions = (1200, 500)
print(dimensions)

# (400, 200) tuple is still in the memory, but the "dimensions" variable name now points to a new block in the memory where the (1200, 500) tuple resides
# (400, 200) tuple will eventually be erased by the Python garbage collector.

# The important lesson in here is, VARIABLES ARE NOT THE VALUES. They are just used as labels to represent the VALUES in the memory.
# We can change what the label represents.