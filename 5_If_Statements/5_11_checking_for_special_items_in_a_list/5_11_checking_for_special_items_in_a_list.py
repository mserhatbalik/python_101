# We might check if a certain item matches in a list to our cases inside a for loop

pantry = ["mushrooms", "olives", "extra cheese", "green peppers"]
requested_toppings = ["olives", "ham", "extra cheese"]

print("\nStarted preparing your pizza\n")
for item in requested_toppings:         # Loop over requested items
    if item not in pantry:              # If the "item" at the "current index of requested_toppings" is NOT inside "pantry" list we execute the operation inside this block.
        print(f"Sorry, but we don't have {item}")
    else:
        print(f"Adding {item} to your pizza")
print("Your pizza is ready!")
