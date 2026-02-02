"""
15-3.	Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with ax.plot().
To simulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values and rw.y_values, and include a linewidth argument.
Use 5,000 instead of 50,000 points to keep the plot from being too busy.
"""

# from random import choice
# import matplotlib.pyplot as plt
#
#
# class RandomWalk:
#     """Class to generate random walks"""
#
#     def __init__(self, num_points=5000):
#         """Initialize attributes of a walk"""
#         self.num_points = num_points
#
#         """All walks start at (0, 0)"""
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """Calculate all the points in the walk."""
#
#         # Keep taking steps until desired length reached
#         while len(self.x_values) < self.num_points:
#             # Decide which direction to go
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # Reject moves that go nowhere
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # Calculate the new position.
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step
#
#             self.x_values.append(x)
#             self.y_values.append(y)
#
# # Make a random walk
# rw = RandomWalk(5000)
# rw.fill_walk()
#
# # Plot the walk
# plt.style.use("classic")
#
# # Change the resolution size of the figure
# fig, ax = plt.subplots(figsize=(40, 40))
#
# ax.plot(rw.x_values, rw.y_values, linewidth=1, c="red")
# ax.set_aspect("equal")
#
# # Emphasize start and end points
# ax.scatter(0, 0, c="green", s=200)  # START POINT
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c="blue", s=200)  # END POINT
#
# # Remove the x-y axes labels from the figure
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
#
# plt.show()


"""
15-4.	Modified Random Walks: In the RandomWalk class, x_step and y_step are generated from the same set of conditions. 
The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. 
Modify the values in these lists to see what happens to the overall shape of your walks. 
Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x- or y-direction list.
"""

# from random import choice
# import matplotlib.pyplot as plt
#
#
# class RandomWalk:
#     """Class to generate random walks"""
#
#     def __init__(self, num_points=5000):
#         """Initialize attributes of a walk"""
#         self.num_points = num_points
#
#         """All walks start at (0, 0)"""
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """Calculate all the points in the walk."""
#
#         # Keep taking steps until desired length reached
#         while len(self.x_values) < self.num_points:
#             # Decide which direction to go
#             x_direction = choice([1, -1])
#             x_distance = choice([30, 40, 50, 60, 70, 80, 90, 100])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([30, 40, 50, 60, 70, 80, 90, 100])
#             y_step = y_direction * y_distance
#
#             # Reject moves that go nowhere
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # Calculate the new position.
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step
#
#             self.x_values.append(x)
#             self.y_values.append(y)
#
# # Make a random walk
# rw = RandomWalk()
# rw.fill_walk()
#
# # Plot the walk
# plt.style.use("classic")
#
# # Change the resolution size of the figure
# fig, ax = plt.subplots(figsize=(40, 40))
#
# ax.scatter(rw.x_values, rw.y_values, s=15, c=range(rw.num_points), cmap=plt.cm.Blues, edgecolors="none")
# ax.set_aspect("equal")
#
# # Emphasize start and end points
# ax.scatter(0, 0, c="green", edgecolors="none", s=100)  # START POINT
# ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c="red", edgecolors="none")  # END POINT
#
# # Remove the x-y axes labels from the figure
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
#
# plt.show()

"""
15-5.	Refactoring: The fill_walk() method is lengthy. Create a new method called get_step() to determine the direction and distance for each step, 
and then calculate the step. You should end up with two calls to get_step() in fill_walk():
x_step = self.get_step()
y_step = self.get_step()
This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.
"""


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
            x_step = self._get_step()
            y_step = self._get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([30, 40, 50, 60, 70, 80, 90, 100])
        return x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([30, 40, 50, 60, 70, 80, 90, 100])
        return y_direction * y_distance

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the walk
plt.style.use("classic")

# Change the resolution size of the figure
fig, ax = plt.subplots(figsize=(40, 40))

ax.scatter(rw.x_values, rw.y_values, s=15, c=range(rw.num_points), cmap=plt.cm.Blues, edgecolors="none")
ax.set_aspect("equal")

# Emphasize start and end points
ax.scatter(0, 0, c="green", edgecolors="none", s=100)  # START POINT
ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c="red", edgecolors="none")  # END POINT

# Remove the x-y axes labels from the figure
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()