# Below we create 30 individual alien dictionaries in a for loop, and put all these dictionaries inside a list
aliens = []

# _ can be used while creating a for loop when that variable will not be used in the upcoming code block to simplify the syntax.
for _ in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# The reason for the variable reassignment takes effect, is the aliens[:3] points to the exact memory address of the list.
# So, when we loop through that part of the list, the value assignments change the exact part of that list.
# Change the FIRST 3 aliens to YELLOW
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

# Change the LAST 3 aliens to RED
for alien in aliens[-3:]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

for alien in aliens:
    print(alien)
print(len(aliens))