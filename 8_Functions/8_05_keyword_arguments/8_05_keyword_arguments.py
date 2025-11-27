# Keyword arguments free us from worrying about the position of the arguments
# They act like key/value pairs, which are especially useful in cases where we pass values to functions from dictionaries

def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# In the example below we intentionally mix the ordering of parameters
# Because we explicitly tell python to match the parameters with = assignment operator to the values, everything works as intended with no issues
describe_pet(pet_name="cici", animal_type="bird")
describe_pet(animal_type="cat", pet_name="garfield")