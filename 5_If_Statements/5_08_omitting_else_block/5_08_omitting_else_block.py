# It is not always needed to use "else" keyword inside if statements.
# Else keyword is usually used in cases if something has to happen no matter what.
# In the case below, this is not the case. We only want to check for 3 conditions, and that's all.

name = "Serhat"
if name == "serhat":
    print("Your name is lowercased")
elif name == "Serhat":
    print("Your name is titlecased")
elif name == "SERHAT":
    print("Your name is uppercased")
# else:
#     print("Your name is not what we are looking for")