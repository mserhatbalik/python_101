import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")

fig,ax = plt.subplots()

ax.scatter(x_values, y_values)

# Optional
# ax.axis([0,1100,0,1000000])

# Use original values in ticker labels instead of condensed ones.
ax.ticklabel_format(style='plain')

plt.show()