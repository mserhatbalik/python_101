# To work with parts of a list we can use slice() function.
# Important thing to remember is; INDEXES start from 0

players = ["alice", "eli", "samantha", "john", "jake", "richard", "penelope", "christopher"]

# Below we specify to cut from 2nd index number up to 5th index number. Excluding 5th.
# In this case; 0, 1, 2 (samantha), 3 (john), 4 (jake), 5 (EXCLUDING)
print(players[2:5])

# If we omit the first number, that means "start from the beginning"
# In this case; 0 (alice), 1 (eli), 2 (EXCLUDING), 3, 4, 5, 6, 7
print(players[:2])

# We can also define the beggining index and go thorugh to the end of list
# In this case; 0, 1, 2, 3, 4 (jake), 5 (richard), 6 (penelope), 7 (christopher)
print(players[4:])

# It is also possible to define the starting index as negative values to determine the starting index from the end of the list
# In this case; 0, 1, 2, 3, 4, 5 (richard), 6 (penelope), 7 (christopher)
print(players[-3:])
