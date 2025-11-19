# .keys() method can be used in cases where we just need to access the key parameters of a particular dicitonary.

favorite_languages = {"sarah": "c#", "jack": "Python", "christopher": "PHP", "elisa": "JavaScript", "richard": "Python"}

# This for loop goes through all the keys inside the favorite_languages dictionary, and assign each key name to "dict_key" variable.
# dict_key variable can be named to anything
for dict_key in favorite_languages.keys():
    print(dict_key)

# .keys() method is used to make your code more explicit and readable. In the end though, it is not necessary.
# The code below achieves the same goal.
for key in favorite_languages:
    print(key.title())