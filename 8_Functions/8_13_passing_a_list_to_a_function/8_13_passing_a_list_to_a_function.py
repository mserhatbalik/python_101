# It is possible to pass a list as an argument to a function.
# This allows a function to access all the elements in the list and work with them.

def greet_users(guests):
    for guest in guests:
        print(f"Hello {guest.title()}. Welcome to our party!")

people = ["george", "jack", "selena", "mark", "yuri"]
greet_users(people)