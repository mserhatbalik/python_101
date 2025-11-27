# It is possible to create fixed positional arguments alongside arbitrary arguments
# Key point is, the POSITIONAL argument definition has to be done AFTER the arbitrary argument definitions.

def cook_pizza(*toppings, size):
    print(f"Preparing you {size} sized pizza with the following toppings..")
    for topping in toppings:
        print(f"\t-{topping.title()}")

cook_pizza("medium", "pepperoni", "cheese", "mushrooms", size="medium")