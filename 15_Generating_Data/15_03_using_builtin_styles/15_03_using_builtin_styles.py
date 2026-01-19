import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Define the style before creating the fig and ax
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

plt.show()