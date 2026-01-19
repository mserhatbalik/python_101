import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()

ax.ticklabel_format(style="plain")

# We can set the color of plots by using color property and RGB values along with it.
ax.scatter(x_values, y_values, s=10, color=(0,0.8,0))

plt.show()
