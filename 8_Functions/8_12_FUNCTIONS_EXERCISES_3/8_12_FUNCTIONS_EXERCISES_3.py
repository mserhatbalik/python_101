"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.
"""
# def city_country(city, country):
#     formatted = f"{city.title()}, {country.title()}"
#     return formatted
#
# print(city_country("istanbul", "turkey"))
# print(city_country(country="france", city="paris"))

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""
# def make_album(artist, title, songs=None):
#     album = {"artist_name": artist, "album_title": title}
#     if songs:
#         album = {"artist_name": artist, "album_title": title, "number_of_songs": songs}
#     return album
#
#
# artist1 = make_album("Sex Pistols", "Never Mind the Bollocks")
# artist2 = make_album(title="25", artist="Adele")
# artist3 = make_album("Kendrick Lamar", "DAMN", 14)
#
# print(artist1)
# print(artist2)
# print(artist3)

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""

def make_album(p_artist, p_title, p_songs=None):
    album = {"artist_name": p_artist, "album_title": p_title}
    if songs:
        album = {"artist_name": p_artist, "album_title": p_title, "number_of_songs": p_songs}
    return album

albums = []
while True:
    print("Type 'q' to quit")
    artist = input("What is the name of the artist?\n")
    if artist == "q":
        break
    title = input("What is the name of the album title?\n")
    if title == "q":
        break
    songs = input("If all the songs are ready. How many are there? If not, press ENTER\n")
    if songs == "q":
        break
    albums.append(make_album(artist, title, songs))

print(albums)