# We can simplfy our hello world program by using variables.
# Variables are "labels" that we can give assign to values, so we can refer to them easily in the future.
# The critical distinction is they are not storage for values, but referring mechanism to the values that are already stored in the memory.
message = "Hello Python!"
print(message)

# When we refer to the same variable again and assing it a different value, we overwrite the first assigned value.
# This is why the print(message) output is different in the second print prompt.
message = "Hello Python Crash Course world"
print(message)