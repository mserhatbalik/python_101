# When we require an external input from the user, we can achieve that by using the input() function.
# We can assign the input() function to a variable, so it can be used in the program to achieve various outcomes.

# input() function takes 1 argument, and pauses the code execution until the user enters the requested prompt.
name = input("Hello, please tell me your name.\n")
print(f"Hello {name.title()}, welcome to our hotel. I hope you have a good trip!")