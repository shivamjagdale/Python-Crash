import json
from pathlib import Path 

# Give the location of the file 
path = Path("C:/Users/Shivam/Desktop/Practise/eq_data_30day.geojson")

# read the file 
file = path.read_text(encoding="utf-8")

# now turn it into python object 
earthquake_data = json.loads(file)

# give the output path 
# 
path = Path("C:/Users/Shivam/Desktop/Practise/geo_data_30day.json")

# dump it 
dump = json.dumps(earthquake_data, indent=4)

# write it 
path.write_text(dump)

"""-------------------------------------------------"""
# counting how many earth quakes we have 

eq_dict = []

earthquakes = earthquake_data["features"]

for quake in earthquakes:
    aa = quake
    eq_dict.append(aa)
print(len(eq_dict))

"""-------------------------------------------------"""

# Extract magnitudes 
mags = []

for magnitude in earthquakes:
    aa = magnitude["properties"]["mag"]
    mags.append(aa)
#print(mags[:10])

# Extract location
long = []
lati = []

for longitude in earthquakes:
    aa = longitude["geometry"]["coordinates"][0]
    long.append(aa)
#print(long[:5])

for latitude in earthquakes:
    aa = latitude["geometry"]["coordinates"][1]
    lati.append(aa)
#print(lati[:5])

# eq title
eq_title = []

for title in earthquakes:
    aa = title["properties"]["title"]
    eq_title.append(aa)

"""-------------------------------------------------"""
# Creating world map

import plotly.express as px 

title = "World map of Earthquakes"

# figure
fig = px.scatter_geo(lon=long, lat=lati, title=title,
                     color=mags, size=mags,
                     color_continuous_scale="Viridis",
                     labels={"color":"Magnitude"},
                     projection="natural earth",
                     hover_name= eq_title)

# show the figure 
fig.show()