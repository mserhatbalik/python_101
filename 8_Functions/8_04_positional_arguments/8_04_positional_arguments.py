# We can pass arguments to functions in two ways
# The first way to pass an argument/parameter is positional
# Arguments are passed to a function in the way they are defined in the function definition

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# The order of parameters defined in function definition is also corresponds to the order of parameters passed during a function call
# The first parameter we pass during a function call corresponds to "animal_type"
# The second parameter we pass during a function call corresponds to "pet_name"
describe_pet("hamster", "harry")
describe_pet("dog", "poo")