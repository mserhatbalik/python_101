# Changing existing values of keys is as simple as assigning them new values
# Creating empty dictionary
alien_0 = {}

# Defining its core key value pairs
alien_0["color"] = "yellow"
alien_0["points"] = 5

# Adding new key value pairs
alien_0["x-position"] = 0
alien_0["y-position"] = 0

# Determining the new position of alien depending on the condition
if alien_0["color"] == "green":
    x_increment = 1
elif alien_0["color"] == "yellow":
    x_increment = 2
elif alien_0["color"] == "red":
    x_increment = 3

# Print the new position of the alien
print(f"Alien has moved by {alien_0["x-position"] + x_increment} meters")
