# In cases, where the number of arguments are not clear, it is possible to define arbitrary parameters with "*" asterix sign.
# This will indicate to python interpreter that, this function MIGHT multiple arguments

def cook_pizza(*toppings):
    print("Preparing a pizza with following toppings..")
    for topping in toppings:
        print(f"\t-{topping}")


cook_pizza("pepperoni", "cheese", "mushrooms", "tomato", )
