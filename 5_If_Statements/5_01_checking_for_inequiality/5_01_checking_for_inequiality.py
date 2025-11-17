# When we want to check if the condition is NOT what we state, we use != operator instead of ==

requested_topping = "mushrooms"
if requested_topping != "olives":
    print(f"What I want as toppings in my pizza is olives, but you've brought me {requested_topping}.")
else:
    print("Thank you for bringing olives as my pizza topping!")