# In some cases the list we are working might come up empty, and trying to run a loop through an empty list will return empty.
# In order to prevent this, we should check whether that list is empty or not before running the loop.
# If we use the list in an if statement by itself without any condition, this statement will check if the list is empty or not.
# If the list returns empty the first if block will be skipped because it will return FALSE, and the Else block will run.

pizza_toppings = []

if pizza_toppings: # This statement returns FALSE, because the list is empty. ELSE block will run in this case.
    for item in pizza_toppings:
        print(f"Adding {item} to your pizza")
else:
    print("Are you sure you want a plain pizza?")