from random import randint
import plotly.express as px
from plotly.graph_objs.layout.scene import xaxis


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six sided dice"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)


# Create D6
die_1 = Die()
die_2 = Die(10)

# Make some rolls and return a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# ANALYZE THE RESULTS
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


# Making a histogram
title = "Results of Rolling two D6 1,000 Times"
labels = {"x" : "Result", "y" : "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

# Customize chart
fig.update_layout(xaxis_dtick=1)

# Print results
print(frequencies)
