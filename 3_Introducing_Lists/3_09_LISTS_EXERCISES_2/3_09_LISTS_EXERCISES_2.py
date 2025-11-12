# # 3-4. Guest List: If you could invite anyone, living or deceased, to dinner,
# # who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
# # Then use your list to print a message to each person, inviting them to dinner.
#
people = ["sun tzu", "al pacino", "bill gates"]
# print(f"Hi {people[0].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[1].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[2].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")


# # Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# print(f"Oh, it seems like {people[2].title()} will not be able to make it")
# people.pop()
# people.append("steve jobs")
# print(f"Hi {people[2].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")

#  You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
people.insert(0, "buddha")
people.insert(2, "mustafa kemal")
people.append("jesus")

# print(f"Hi {people[0].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[1].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[2].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[3].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[4].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")
# print(f"Hi {people[5].title()}, I hope you are doing well. I would like to invite you to my dinner and have a pleasant evening with us.")

#  You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

denied_person = people.pop()
print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
denied_person = people.pop()
print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
denied_person = people.pop()
print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
denied_person = people.pop()
print(f"I am sorry {denied_person.title()} but dinner table won't arrive in time, I have to cancel my invitation.")
print(f"Hi {people[0].title()} you are still invited to dinner. I hope to see you here.")
print(f"Hi {people[1].title()} you are still invited to dinner. I hope to see you here.")