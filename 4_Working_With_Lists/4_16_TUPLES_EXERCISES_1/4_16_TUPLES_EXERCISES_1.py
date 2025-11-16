"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods.
Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
"""

old_menu = ("pilav", "kuru fasülye", "türlü", "çorba", "salata")
print("\nOur food menu is:")
for food in old_menu:
    print(food.title())

# basic_foods[3] = "orman kebabı"

new_menu = ("pilav", "kuru fasülye", "orman kebabı", "pide", "salata")
print("\nOur new food menu is:")
for food in new_menu:
    print(food.title())