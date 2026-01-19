import matplotlib.pyplot as plt

# Creating the list of x values between 1 and 1000
x_values = list(range(1, 1001))

# Using list comprehension to generate the squares of x values
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)

# Set range for each axis
ax.axis([0, 1100, 0, 1000000])

plt.show()
