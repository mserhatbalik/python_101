def make_pizza(size, *toppings):
    """Making pizza with specified size and various numbers of toppings"""
    print(f"Making {size} size pizza with the following toppings...")
    for topping in toppings:
        print(f"\t-{topping}")