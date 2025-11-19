"""
6-4. Glossary 2: Now that you know how to loop through a dictionary,
clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.
"""
# programming_words = {"integer": "A numerical representation of a value",
#                      "slice": "A function to copy a part of a list",
#                      "list": "A container which stores arbitrary amount of data",
#                      "for-loop": "A programming concept that allows us run X amounts of iterations for particular code blocks",
#                      "if block": "A programming concept that allows us check for particular condition before executing specific code blocks",
#                      "dictionary": "A Python data structure that allows storage of information in key-value pairs.",
#                      "set": "A Python data structure that allows storage of arbitrarily ordered unique values",
#                      "float": "A data type similar to integer that allows decimal point operations.",
#                      "list comprehension": "Quick way of populating lists with particular kind of logic",
#                      "tuple": "A data type similar to lists, but immutable. We can assign a new tuple to a variable, but we cannot assign new values to an existing tuple."}
# for item in programming_words:
#     print(f"{item}: {programming_words[item]}")


"""
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
"""

# rivers = {"nile": "egypt", "euphrates": "turkey", "niagara": "united states"}
# for item in rivers:
#     print(f"{item} river runs through {rivers[item]}")
# for river in rivers.keys():
#     print(river)
# for country in rivers.values():
#     print(country)

"""
6-6. Polling: Use the code in favorite_languages.py (page 96).

Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. 
If they have not yet taken the poll, print a message inviting them to take the poll.
"""

people = ["osman", "patrick", "jack", "elisa", "nick"]
favorite_languages = {"sarah": "c#", "jack": "Python", "christopher": "PHP", "elisa": "JavaScript", "richard": "Python"}

for person in people:
    if person in favorite_languages:
        print(f"Hey {person}. Thank you for taking the poll.")
    else:
        print(f"Hey {person}. I invite you to take the poll.")