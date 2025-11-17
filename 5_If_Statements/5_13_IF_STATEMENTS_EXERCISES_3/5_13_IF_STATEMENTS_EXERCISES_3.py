"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user.

If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""
# users = ["blake", "jennifer", "admin", "carmella", "tony"]
# for user in users:
#     if user == "admin":
#         print(f"Hello {user}. Would you like to see a status report?")
#     else:
#         print(f"Hello {user}. Thank you for logging in.")



"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.

If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.
"""

# users = []
# if users:
#     for user in users:
#         if user == "admin":
#             print(f"Hi {user}. Would you like to check status report?")
#         else:
#             print(f"Hi {user}. Thank you for logging in.")
# else:
#     print("We need some users to run the program!")


"""
5-10. Checking Usernames: Do the following to create a program that simulates how
 websites ensure that everyone has a unique username.

Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already been used. 
If it has, print a message that the person will need to enter a new username. 
If a username has not been used, print a message saying that the username is available.
Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""

# current_users = ["blake", "Jennifer", "admin", "carmella", "tony"]
# new_users = ["Jake", "Tony", "molly", "blake", "Patrick", "richard", "CARMELLA", "penelope"]
#
# lower_case_new_users = [name.lower() for name in new_users] # Using LIST COMPREHENSION
#
# for user in lower_case_new_users:
#     if user in current_users:
#         print(f"The user name {user} is not available")
#     else:
#         print(f"New user {user} is created")


"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
Most ordinal numbers end in th, except 1, 2, and 3.

Store the numbers 1 through 9 in a list.
Loop through the list.
Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""

# for number in range(1,10):
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     elif number == 4:
#         print("4th")
#     elif number == 5:
#         print("5th")
#     elif number == 6:
#         print("6th")
#     elif number == 7:
#         print("7th")
#     elif number == 8:
#         print("8th")
#     else:
#         print("9th")
