# We can also return more complex data structures from functions.
# In the example below, we return a dictionary with appropriate keys/values.
# We also check if the optional parameter called "age" is also passed during function call and return appropriate data

# Using "None" keyword is considered best practice when defining default values for function arguments.
def build_person(first_name, last_name, age=None):
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person = {"first_name": first_name, "last_name": last_name, "age": age}
    return person

who = build_person("serhat", "balık")
print(who)