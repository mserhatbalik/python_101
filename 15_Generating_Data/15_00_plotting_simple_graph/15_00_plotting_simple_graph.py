# Import pyplot submodule of matplotlib module
import matplotlib.pyplot as plt

# Define the data. If we don't specify additional dimension, matplotlib assumes this data represent the Y-Axis of the chart.
# It will automatically plot the X-Axis as 1,2,3,4,5 which matches the total number of data points in our squares list.
squares = [1, 4, 9, 16, 25]

# Create two distinct objects at once.
# Fig is the blank canvas we want to create
# ax is the chart we want to put into this canvas.
fig, ax = plt.subplots()

# We are telling ax chart to encapsulate our squares list as data.
ax.plot(squares)

# Opens the global viewer window. If there are multiple figures and chart, it will display all at once.
# To exclude a specific chart from appearing up, we need to close it with the statement "plt.close(fig2)"
plt.show()