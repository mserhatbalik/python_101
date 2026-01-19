"""
15-1.	Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5,000 cubic numbers.
"""

# import matplotlib.pyplot as plt
#
# x_values = list(range(1,5001))
# y_values = [x**3 for x in x_values]
#
# plt.style.use("seaborn-v0_8")
# fig,ax = plt.subplots()
# ax.plot(x_values, y_values)
# ax.ticklabel_format(style="plain")
#
# plt.show()


"""
15-2.	Colored Cubes: Apply a colormap to your cubes plot.
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds)
ax.ticklabel_format(style="plain")

plt.savefig("myscatter.svg")
plt.show()
