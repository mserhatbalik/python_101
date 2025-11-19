# Below is a more concise version of accessing keys and also associated values inside a dictionary.
favorite_languages = {"sarah": "c#", "jack": "Python", "christopher": "PHP", "elisa": "JavaScript", "richard": "Python"}
friends = ["jack", "elisa"]

for dict_key in favorite_languages:
    if dict_key in friends: # If the key is one of our friends, we access the corresponding value and print it with an additional message.
        print(f"Hi {dict_key.title()}. My friend, I see you like {favorite_languages[f"{dict_key}"]}.")
    else:
        print(f"Hi {dict_key.title()}")