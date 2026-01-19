import matplotlib.pyplot as plt

squares = [1,4,9,16,25]

fig, ax = plt.subplots()

# We can set the line thickness with the "linewidth" property
ax.plot(squares, linewidth=3)

# Define the title of ax chart and fontsize
ax.set_title("Square Numbers", fontsize=24)

# Define the label and fontsize of X-Axis
ax.set_xlabel("Value", fontsize=14)

# Define the label and fontsize of Y-Axis
ax.set_ylabel("Square of value", fontsize=14)

# Define the label size of tick value delimiters of both X and Y Axis
ax.tick_params(labelsize=14)

# Show the fig
plt.show()