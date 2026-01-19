import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Reds)
ax.ticklabel_format(style="plain")

# We can save the chart to specified path.
plt.savefig("myplot.svg")
plt.show()
