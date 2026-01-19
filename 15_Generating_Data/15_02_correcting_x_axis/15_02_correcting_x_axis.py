import matplotlib.pyplot as plt

# Defined X-Axis values
input_values = [1, 2, 3, 4, 5]

# Defined Y-Axis values
squares = [1, 4, 9, 16, 25]

# Created fig & ax objects
fig, ax = plt.subplots()

# Filled the X-Axis and Y-Axis data of ax chart. Also set the linewidth property
ax.plot(input_values, squares, linewidth=3)

# Draw the chart
plt.show()
