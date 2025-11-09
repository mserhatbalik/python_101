### VARIABLES IN STRINGS  and F STRINGS###
# first_name = "Serhat"
# last_name = "Balık"
# message = f"Hello {first_name} {last_name}! Would you like to learn some Python today?"
# print(message)
from sys import prefix

### STRING FUNCTIONS ###
# first_name = "Serhat"
# last_name = "Balık"
# upper_case_message = f"{first_name.upper()} {last_name.upper()}"
# print(upper_case_message)
# lower_case_message = upper_case_message.lower()
# print(lower_case_message)
# title_case_message = lower_case_message.title()
# print(title_case_message)

### DOUBLE AND SINGLE QUOTES ###
# message = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
# print(message)

### DOUBLE AND SINGLE QUOTES WITH F STRINGS, VARS, Functions ###
# famous_person = "albert einstein"
# quote = "A person who never made a mistake never tried anything new."
# message = f'{famous_person.title()} once said, "{quote}"'
# print(message)


### WHITE SPACE ADDING AND STRIPPING ###
# first_name = "\tserhat\n"
# last_name = "\t\t\tbalık"
# print(first_name+last_name)
# stripped_first_name = first_name.lstrip()
# stripped_last_name = last_name.strip()
# print(stripped_first_name+stripped_last_name)

### REMOVE PREFIX AND SUFFIX ###
# website_name = "www.facebook.com".removeprefix("www.").removesuffix(".com")
# print(website_name)