# We use lstrip() rstrip() strip() string methods in order to clean up whitespaces in strings.
# These methods are often used in real world applications to fix and standardize the user input in applications.

user_input = "          Serhat Balık             "
print(user_input)
print(user_input.strip())
print(user_input)

# As we can see, methods do not update the variable. In some cases it is necessary to update the variable names. Such as after user name fixing in applications.
first_name = "  serhat"
last_name = "balık      "

# Updating the variables
first_name = first_name.strip().title()
last_name = last_name.strip().title()
print(first_name)
print(last_name)