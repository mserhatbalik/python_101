# There is special keyword "in" we use to check if a value is present or not in a list

banned_users = ["bob", "marie", "jack", "robert", "juliana"]
registering_user = "serhat"
if registering_user in banned_users:
    print("You are banned previously. Registration is not possible at this time.")
else:
    print(f"Welcome {registering_user.title()}. You are now a registered member.")