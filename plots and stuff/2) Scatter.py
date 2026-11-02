import matplotlib.pyplot as plt 

# Use a predefined style 
plt.style.use("seaborn-v0_8")

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

# Plot numbers
ax.scatter(x_values, y_values, c = x_values , cmap=plt.cm.Blues, s=50)
#ax.scatter(2,4, s=100, color="red")

# Title 
ax.set_title("Square of a number", fontsize=24)

# x label
ax.set_xlabel("Values", fontsize=13)

# y label
ax.set_ylabel("Squares", fontsize = 13)

# ticks (the numbers)
ax.tick_params(labelsize=14)

# set the range for each axis 
ax.axis([0,1000, 0,1_000_000])

# want normal numbers 
ax.ticklabel_format(style="plain")

# save the graph 
plt.savefig("squareee.png")

plt.show()