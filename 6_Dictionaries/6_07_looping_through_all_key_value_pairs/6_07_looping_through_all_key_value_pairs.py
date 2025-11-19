# It is also possible to loop through a dictionary and access to key defitions of the data in addition to values

favorite_languages = {"sarah": "c#", "jack": "Python", "christopher": "PHP", "elisa": "JavaScript", "richard": "Python"}

# We can give any name as parameters in the for loop.
# .items() function is important. This allows us to take each item and divide it into its parts as key-value pairs,
# and assign them to their corresponding values. In this case "name" -> KEY and "language" -> VALUE
for person, language in favorite_languages.items():
    print(f"{person.title()}'s favorite programming language is {language}.\n")