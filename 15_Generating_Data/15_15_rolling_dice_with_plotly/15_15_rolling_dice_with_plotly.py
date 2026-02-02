from random import randint
import plotly.express as px

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides = 6):
        """Assume a six sided dice"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)

# Create D6
die = Die()

# Make some rolls and return a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# ANALYZE THE RESULTS
# Define the empty list to store total frequencies of each die roll
frequencies = []

# Define the total frequency range to loop thorugh. In this instance default num_sides is 6. range() function works through 1 to 7, but excluding 7.
poss_results = range(1,die.num_sides+1)

# Iterate through all frequencies. Start with 1.
for value in poss_results:
    # Count all the 1s in the results, then 2, then 3, etc. in each loop
    frequency = results.count(value)

    # Append the occurance of each side to the frequencies list.
    frequencies.append(frequency)

# Visualize the results using Plotly
title = "Results of Rolling one D6 1,000 Times"
labels = {"x" : "Side", "y" : "Frequency of Side"}
fig = px.line(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

# The results format is [151, 168, 167, 172, 180] as an example. 151 is how many 1s are in the results list, 168 is how many 2s are in the results list, etc.
print(frequencies)