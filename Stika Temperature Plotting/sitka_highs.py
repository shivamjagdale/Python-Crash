from pathlib import Path
import csv

path = Path("C:/Users/Shivam/Desktop/Alien Invasion/death_valley_2021_simple.csv")

# read the file
lines = path.read_text().splitlines()

# Give those lines to csv reader 
reader = csv.reader(lines)

# Get the 1st row 
header_row = next(reader)
#print(header_row)

# Go thru the headers 
for index, header in enumerate(header_row):
    print(index, header)

# Extract high temps from csv
# tell me why this works but 
"""------------------------------------------------------"""

from datetime import datetime
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%d-%m-%Y')

    try:
        low = int(row[4])
        high = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
"""------------------------------------------------------"""

# Now plot a char usint matplotlib 
import matplotlib.pyplot as plt 

# Choose a plotting style
plt.style.use("seaborn-v0_8")

# Create the figure and axes 
fig,ax = plt.subplots()

# plot the temperatures 
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)

# fill between
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)

# add title 
ax.set_title("Daily high and low temps in 2021 \nDeath Valley CA.", fontsize=24)

# x and y axis labels
ax.set_xlabel("", fontsize=15)
ax.set_ylabel("Temperatures (F)", fontsize=15)

# write the dates correctly on x-axis
fig.autofmt_xdate()

# ticks 
ax.tick_params(labelsize=16)

# show the fig
plt.show()