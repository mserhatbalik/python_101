# Some functions might require external data to do their job.
# We pass this data to a function call through a concept called parameters/arguments

# username acts as a variable defined in the function body.
def greet_user(username):
    print(f"Hello, {username.title()}!")

# When doing a function call, the value we pass to the function matches with the "username" parameter we have defined in the function definition
greet_user("serhat")
greet_user("lisa")
greet_user("mark")