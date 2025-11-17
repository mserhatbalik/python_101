# There is one caveat with if statements. If one of the statements evaluates to TRUE, then the next elif and else statements are skipped entirely.
# This is useful in most situations, but in some cases we would like to create multiple independed if statements.

# In this example, following statements after the second one are skipped because the second one returns TRUE

pizza_toppings = ["mushrooms", "extra cheese", "pepperoni"]
if "cream" in pizza_toppings:  # Cream is not in our list, so this if statement returns FALSE and skipped
    print("Adding cream to your pizza")
elif "extra cheese" in pizza_toppings: # Extra cheese is in our list, so this statement returns TRUE and executes the operations inside the statement
    print("Adding extra cheese to your pizza")
elif "mushrooms" in pizza_toppings: # Mushrooms is in our list, BUT just because the statement above returned TRUE, additional if statements are skipped entirely in this block.
    print("Adding mushrooms to your pizza")
print("Finished making your pizza\n")

if "cream" in pizza_toppings: # This statement returns FALSE same as the if block above.
    print("Adding cream to you pizza")
if "extra cheese" in pizza_toppings:
    print("Adding extra cheese to your pizza") # This statement returns TRUE and the operation executes.
if "mushrooms" in pizza_toppings:
    print("Adding mushrooms to your pizza") # This statement also returns TRUE and the operation executes because it is an INDEPENDENT IF block. So the the if statements above do not affect this one.
print("Finished making your pizza")