import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Instead of a line, scatter just marks key data points. s=200 argument defines the size of marks.
ax.scatter(input_values, squares, s=200)

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

ax.tick_params(labelsize=14)


plt.show()
