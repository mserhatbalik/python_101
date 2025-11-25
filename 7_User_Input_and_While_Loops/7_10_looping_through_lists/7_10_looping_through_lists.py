# When we give a list as a condition a while loop, the loop will keep running until the end of the list.
# In the example below we run through the list of unconfirmed users, and put them to confirmed users list.

unconfirmed_users = ["alice", "mark", "john", "leila"]
confirmed_users = ["kate", "jonathan"]

while unconfirmed_users:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)

print(confirmed_users)