"""
8-9. Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
"""
# def show_messages(p_messages):
#     for message in p_messages:
#         print(f"{message}")
#
# messages = ["hey man give me a call.", "what the hell?", "hello mr. call me back.", "hahaha thats funny"]
# show_messages(messages)


"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""
# def send_messages(p_messages):
#     while p_messages:
#         current_message = p_messages.pop()
#         sent_messages.append(current_message)
#
# messages = ["hey man give me a call.", "what the hell?", "hello mr. call me back.", "hahaha thats funny"]
# sent_messages = []
#
# send_messages(messages)
#
# print(messages)
# print(sent_messages)

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
# def send_messages(p_messages):
#     p_messages.reverse()
#     while p_messages:
#         current_message = p_messages.pop()
#         sent_messages.append(current_message)
#
# messages = ["hey man give me a call.", "what the hell?", "hello mr. call me back.", "hahaha thats funny"]
# sent_messages = []
#
# send_messages(messages[:])
#
# print(messages)
# print(sent_messages)
