# Most of the times, we should leave the original list as it is, and create a new copy and work with that copy instead.
# We can use slice [:] function to achieve that outcome.

my_favorite_foods = ["pizza", "kebab", "hamburger", "sushi"]
my_friends_favorite_foods = my_favorite_foods[:]

my_favorite_foods.append("doner")
my_friends_favorite_foods.append("lasagna")

print(my_favorite_foods)
print(my_friends_favorite_foods)
