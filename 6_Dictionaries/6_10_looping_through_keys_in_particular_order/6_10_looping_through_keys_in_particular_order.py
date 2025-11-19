# We can use sorted() function to sort the keys inside a dictionary to process them in an ordered fashion.

user_ages = {"tom": 34, "elena": 21, "sabrina": 56, "richard": 42}

# REMEMBER, THIS METHOD SORTS BY KEY, NOT VALUE.
# So, we get ALPHABETICALLY SORTED KEYS.
for user in sorted(user_ages):
    print(f"{user.title()} is {user_ages[user]} old.")
