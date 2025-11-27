# It is also possible to define default values for parameters in cases when no value is passed to the function to be used as the default value

def describe_car(person, car_model, color="white"):
    print(f"{person.title()} has a {color} {car_model.title()}!")


# We intentionally skip the color argument in the first function call below, and it equates to "white"
describe_car(car_model="porsche 911 turbo s", person="serhat")

# If we explicitly pass an argument, it will overwrite the default value.
describe_car(person="jack", color="black", car_model="Audi q5")

# Using positional arguments. When defining a function, default parameters should be defined last.
describe_car("kate", "volkswagen polo")