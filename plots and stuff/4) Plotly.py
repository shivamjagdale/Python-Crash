from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Rolling our dice"""
        return randint(1, self.num_sides)


# We roll the 6 sided slide 100 times and store the result.
# Making a histogram

import plotly.express as px

die_1 = Die()
die_2 = Die(10)

# Create an empty list to store the values 
results = []

# rolling the dice 1000 times
for roll in range(50_000):
    a = die_1.roll() + die_2.roll()
    results.append(a)

max_poss_result = die_1.num_sides + die_2.num_sides # 12

frequencies = [] # stores how many times each number appeared.

poss_results = range(2, max_poss_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Create a bar chart
# title
title = "Results of rolling 2 dice D6 and D10 50,000 Times"

# axis labels 
labels = {"x":"Numbers", "y":"No of times they appear"}

fig = px.bar(x=poss_results, y=frequencies,
              title=title, 
              labels=labels)

# show every number on x-axis
fig.update_layout(xaxis_dtick=1)

# save graph               
fig.write_html("dice.html")

# show the graph
fig.show()