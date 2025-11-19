# It is also possible to loop through a dictionary using the VALUES as basis.

user_ages = {"tom": 34, "elena": 21, "sabrina": 56, "richard": 42, "chris": 21}

# for user in sorted(user_ages.values()):
#     print(user)

# We can also use set() function to create a set and discard the duplicate values
# sets contain only unique values, and they are arbitrarily ordered for fast access
for user in set(user_ages.values()):
    print(user)