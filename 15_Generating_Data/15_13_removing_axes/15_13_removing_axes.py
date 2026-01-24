from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        """All walks start at (0, 0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until desired length reached
        while len(self.x_values) < self.num_points:
            # Decide which direction to go
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

while True:
    # Make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the walk
    plt.style.use("classic")

    # Change the resolution size of the figure
    fig, ax = plt.subplots(figsize=(40,40))

    ax.scatter(rw.x_values, rw.y_values, s=15, c=range(rw.num_points), cmap=plt.cm.Blues, edgecolors="none")
    ax.set_aspect("equal")

    # Emphasize start and end points
    ax.scatter(0, 0, c="green", edgecolors="none", s=100) # START POINT
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c="red", edgecolors="none") # END POINT

    # Remove the x-y axes labels from the figure
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig("myplot.png")
    plt.show()
    prompt = input("Would you like to continue? Type 'n' top stop")
    if prompt == 'n':
        break

