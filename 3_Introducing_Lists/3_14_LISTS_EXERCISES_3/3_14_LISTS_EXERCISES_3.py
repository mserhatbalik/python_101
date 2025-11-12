"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its order has changed.
Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
"""

# places = ["peru", "america", "china", "russia", "india"]
# print(places)
# print(sorted(places))
# print(places)
# print(sorted(places,reverse=True))
# print(places)
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)


"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), 
use len() to print a message indicating the number of people you’re inviting to dinner.
"""
# people = ["sun tzu", "al pacino", "bill gates"]
# people.insert(0, "buddha")
# people.insert(2, "mustafa kemal")
# people.append("jesus")
# denied_person = people.pop()
# print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
# denied_person = people.pop()
# print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
# denied_person = people.pop()
# print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
# denied_person = people.pop()
# print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
# print(f"Hi {people[0].title()} you are still invited to dinner. I hope to see you here.")
# print(f"Hi {people[1].title()} you are still invited to dinner. I hope to see you here.")
# print(f"Number of guests that are invited to dinner are {len(people)}")

"""
3-10. Every Function: Think of things you could store in a list. 
For example, you could make  a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

# classes = ["wizard", "rogue", "archer", "mage", "warrior", "paladin", "priest", "warlock", "death knight", "shaman", "druid"]

# # Accessing elements in a list
# print(classes[-3].title())
#
# # Modifying elements in a list
# classes[2] = "ranger"
# print(classes)
#
# # Adding elements to a list
# classes.append("demon hunter")
# print(classes)
# classes.insert(2, "monk")
# print(classes)
#
# # Removing elements from a list
# classes.pop()
# classes.pop()
# print(classes)
# classes.remove("ranger")
# print(classes)
# del classes[3]
# print(classes)
#
# # Sorting a list CHRONOGICALLY
# classes.reverse()
# print(classes)
# classes.reverse()
# print(classes)
#
#
#
# # Sorting a list alphabetically TEMPORARILY
# print(sorted(classes))
# print(sorted(classes, reverse=True))
# print(classes)
#
# # Sorting a list alphabetically PERMANENTLY
# classes.sort()
# print(classes)
# classes.sort(reverse=True)
# print(classes)
# print(len(classes))