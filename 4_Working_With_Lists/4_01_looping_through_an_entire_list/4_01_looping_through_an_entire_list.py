# Looping throughout an entire list
countries = ["turkey", "united states", "peru", "brazil", "india"]

# For loops work in a closed system. Loops start from index 0 unless otherwise specified.
# The "item" is the current element in the loop. We can name this to whatever we want.
# "countries" is the list we want to iterate through.
# Make a note of the extra TAB we used for the print(item) function. This means that, this statement is inside the for loop statement.
# So after the first loop completes, the iterator go back to the beginning and starts again, but this time iteration goes +1
for item in countries:
    print(item)