import matplotlib.pyplot as plt 
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0] # start the x coordinate at 0
        self.y_values = [0] # start the y coordinate at 0

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:
            # For x 
            x_direction = choice([1,-1]) # the direction 
            x_distance = choice([0,1,2,3,4]) # how many steps should we move

            # Calculate the actual x step
            x_step = x_direction * x_distance

            # For y 
            y_direction = choice([-1,1]) 
            y_distance = choice([0,1,2,3,4])

            # The actual walk 
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calcualte the new x_position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Save the new positions 
            self.x_values.append(x)
            self.y_values.append(y)

# Plotting the random walk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Choose a plotting style 
    plt.style.use("classic")

    # figures and axes 
    fig, ax = plt.subplots(figsize=(15,9))

    # Create numbers for every point
    point_numbers = range(rw.num_points)

    # draw the actual thing
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, 
               cmap=plt.cm.Blues, 
               edgecolors = "None",
               s=15)

    # make them equally spaced 
    ax.set_aspect("equal")

    # Emphasize the 1st and last points 
    ax.scatter(0,0, c="green", edgecolors="none", s=100) # starting point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red",
               edgecolors="None", s=100) # ending point

    # Remove the axis 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Ask the user
    keep_running = input("Make another walk (y/n)?")
    if keep_running == "n":
        break
