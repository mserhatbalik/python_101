import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")

fig,ax = plt.subplots()

# We can set gradient coloring based on value. We pass the y_values as the lookup table. The higher the value the more intense the color.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

plt.show()