import matplotlib.pyplot as plt 

plt.style.available

input_values = [1,2,3,4,5,6] # x values 
squares = [1,4,9,16,25,36] # y values 

# Use a predefined style 
plt.style.use("seaborn-v0_8-dark")

fig, ax = plt.subplots()

# Plot numbers
ax.plot(input_values, squares, linewidth=5)

# Title 
ax.set_title("Square of a number", fontsize=24)

# x label
ax.set_xlabel("Values", fontsize=13)

# y label
ax.set_ylabel("Squares", fontsize = 13)

# ticks (the numbers)
ax.tick_params(labelsize=14)

plt.show()