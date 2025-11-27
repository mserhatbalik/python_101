# We can also allow our function parameters to be optional.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Get fully formatted name, with optional middle name argument"""
    if middle_name != '':
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

# Because we return a value inside a function, the function call should also be assigned to a variable in the main program.
musician1 = get_formatted_name("jimmy", "hendrix")
musician2 = get_formatted_name(first_name="kirk", middle_name="lee", last_name="hammett")
musician3 = get_formatted_name("james", "hatfield")


# We print our formatted musician names
print(musician1)
print(musician2)
print(musician3)