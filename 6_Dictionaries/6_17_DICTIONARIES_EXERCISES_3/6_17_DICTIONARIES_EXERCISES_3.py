"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

# person1 = {}
# person1["first_name"] = "Serhat"
# person1["last_name"] = "Balık"
# person1["age"] = 40
# person1["city"] = "İstanbul"
#
# person2 = {}
# person2["first_name"] = "Jane"
# person2["last_name"] = "Brown"
# person2["age"] = 26
# person2["city"] = "Boston"
#
# person3 = {}
# person3["first_name"] = "Richard"
# person3["last_name"] = "Feynman"
# person3["age"] = 69
# person3["city"] = "New York"
#
# people = [person1, person2, person3]
#
# print("List of People")
# for person in people:
#     print(f"\tFirst Name: {person["first_name"]}")
#     print(f"\tLast Name: {person["last_name"]}")
#     print(f"\tAge: {person["age"]}")
#     print(f"\tCity: {person["city"]}\n")


"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.
"""

# pet1 = {"kind": "Cat", "owner": "Feryal"}
# pet2 = {"kind": "Dog", "owner": "Yıldız"}
# pet3 = {"kind": "Bird", "owner": "Mustafa"}
# pet4 = {"kind": "Dog", "owner": "Mehmet"}
#
# pets = []
# pets.append(pet1)
# pets.append(pet2)
# pets.append(pet3)
# pets.append(pet4)
#
# print("List of Pets")
# for pet in pets:
#     print(f"\t{pet["owner"].title()} owns a {pet["kind"]}")


"""
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""

# favorite_places = {"Serhat": ["Thailand", "Amsterdam", "???"],
#                    "Peter": ["Berlin", "Jacarta", "Vatican"],
#                    "Kate": ["Los Angeles", "Paris", "Venice"]
#                    }
#
# for person, places in favorite_places.items():
#     print(f"{person}'s favorite places are")
#     for place in places:
#         print(f"\t{place}")

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""

# favorite_numbers = {"jack": [3, 35, 12], "janice": [0, 1, 2], "adam": [25, 14, 99], "ilana": [11, 0, 3],
#                     "robert": [13, 7, 49]}
#
# for name, numbers in favorite_numbers.items():
#     print(f"{name}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\t{number}")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
"""

# cities = {"istanbul": {"country": "turkey", "population": "15 million", "fact": "they love kebab!"},
#           "paris": {"country": "france", "population": "2 million", "fact": "they have the finest wine!"},
#           "amsterdam": {"country": "netherlands", "population": "1 million", "fact": "capital of ganja!"}}
#
# for city, details in cities.items():
#     print(f"Some details about the city of {city.title()}")
#     for key, value in details.items():
#         print(f"\t{key}: {value.title()}")

"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, 
or improving the formatting of the output.
"""

cities = {"istanbul": {"country": "turkey", "population": "15 million", "fact": "they love kebab!"},
          "paris": {"country": "france", "population": "2 million", "fact": "they have the finest wine!"},
          "amsterdam": {"country": "netherlands", "population": "1 million", "fact": "capital of ganja!"}}

for city, details in cities.items():
    print(f"Some details about the city of {city.title()}")
    for key, value in details.items():
        if  key == "country":
            print(f"\tThe {key.title()} this city resides in is: {value.title()}")
        elif key == "population":
            print(f"\tThe {key.title()} of this city is: {value.title()}")
        else:
            print(f"\tA {key.title()} about this city is: {value.title()}")