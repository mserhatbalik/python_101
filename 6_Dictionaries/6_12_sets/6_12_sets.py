user_ages = {"tom": 34, "elena": 21, "sabrina": 56, "richard": 42, "chris": 21}

# We can also use set() function to create a set and discard the duplicate values
# sets contain only unique values, and they are arbitrarily ordered for fast access
for user in set(user_ages.values()):
    print(user)

# Defining a set is very similar to creating dictionaries with {} curly braces, but in this case there are only values, not key-value pairs.
# Also is important to remember that duplicate values will be discarded
countries = {"mexico", "turkey", "italy", "france", "turkey", "iran", "russia", "turkey"}
print(countries)