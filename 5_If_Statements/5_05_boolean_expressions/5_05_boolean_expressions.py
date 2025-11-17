# Boolean expressions are conditional tests by themselves. We can use these data types to create special rules for certain users, for example.
# Let's say we have users in a database, and we also have a rule if they can only read content on the website, or also can write new content.

user = "john"
can_read = True
can_write = True

if can_read == True and can_write == True:
    print(f"The user: {user} is an Admin. It can both read and write content on the website.")
else:
    print(f"The user: {user} does not have all the permissions.")