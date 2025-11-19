# We can also create associate a key inside a dictionary to list a that contain multiple values
people = {"sarah": ["c#"], "jack": ["Python", "Java"], "elisa": ["JavaScript"], "richard": ["Python", "Rust", "Ruby"],
          "christopher": ["PHP"]}

for person, languages in people.items():
    message = f"{person.title()}'s favorite languages are:"
    print(message)
    for language in languages:
        print(f"\t{language.title()}")