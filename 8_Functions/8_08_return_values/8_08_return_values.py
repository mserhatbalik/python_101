# It is also possible to do some calculations inside a function call and return the result back to the main program,
# and use that result value for some other operation. To achieve this, we use "return" arguments.

# In the function below, we execute 2 specific operations before returning the value back.
# First, we neatly stitch the first_name and last_name values together and assign it to a local function variable called "full_name"
# Second, in the same line as the "return" statement, we also change the "full_name" string into "title()" case.
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Because we return a value inside a function, the function call should also be assigned to a variable in the main program.
musician1 = get_formatted_name("jimmy", "hendrix")
musician2 = get_formatted_name(first_name="kirk", last_name="hammett")
musician3 = get_formatted_name("james", "hatfield")

# We print our formatted musician names
print(musician1)
print(musician2)
print(musician3)