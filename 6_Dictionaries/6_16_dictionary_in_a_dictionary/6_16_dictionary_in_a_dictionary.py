# We can use dictionaries inside dictionaries to represent complex data, but it can also get complicated.
# In the example below, "username" acts like an identifier; this can also be a numerical identification number to reflect a more realistic scenario.
# The secondary dictionary defined inside the first one contains the details of that particular user.

users = {"serhatbalik": {
    "first_name": "serhat", "last_name": "balık", "email": "sbalik@gmail.com"},
    "yasarkurt": {
        "first_name": "yaşar", "last_name": "kurt", "email": "ykurt@gmail.com"
    }}

for username, details in users.items():
    print(f"Username: {username}")
    print(f"\tFirst Name: {details["first_name"].title()}")
    print(f"\tLast Name: {details["last_name"].title()}")
    print(f"\tEmail: {details["email"]}")
