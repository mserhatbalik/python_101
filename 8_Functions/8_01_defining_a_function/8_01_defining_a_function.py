# Functions are like mini factories which do one specific job.
# They may or may not take any parameters.
# Main purpose of function is to reduce repeated code throughout your programs.
# So, if we have a complex code that needs to be executed again and again in our programs in various conditions,
# we define that code block as a function. We call that function in our main program code block whenever we need to execute it.

# We use "def" keyword to tell python that this is a function definition
def greet_user(): # greet_user() part is the name of the function
    """This function prints hello onto the console"""
    print("Hello!") # The indented part inside the function is the code block we want to run everytime the function is called.

# We call the function we have defined above 3 times in our main program.
greet_user()
greet_user()
greet_user()