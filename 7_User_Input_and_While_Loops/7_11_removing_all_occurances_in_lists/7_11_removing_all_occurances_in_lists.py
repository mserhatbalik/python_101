# Previously we have used remove() method to remove a specific occurrence of a value in a particular list.
# But this method removes only one occurrence of a specified value.
# To remove all the occurrences of a specific value, we can loop through a list until there is none.

animals = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while "cat" in animals:
    animals.remove("cat")

print(animals)

