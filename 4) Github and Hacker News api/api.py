import requests
import json 

url = "https://api.github.com/search/repositories"
url+= "?q=language:python+sort:stars+stars:>10000" # search instruction

# Create headers this tells github what format we want our response in
# like in json
headers = {"Accpet":"application/vnd.github.v3+json"}

# Make the api call
response = requests.get(url, headers=headers)
#print(f"Status Code: {response.status_code}") # to see if the request worked

# convert the json repsonse into python dictionary 
response_dict = response.json()

# Look at the dict's keys
#print(response_dict.keys())

# How many repos matched?
matched_repos = response_dict["total_count"]
#print(f"Total Repos = {matched_repos}")

# Were the results complete?
complete_results = response_dict["incomplete_results"]
#print(f"Complete Search = {not complete_results}")

# Get the actual repos
repo_dicts = response_dict["items"]
#print(f"Repos Returned = {len(repo_dicts)}")

# Look at the 1st repo
repo1 = repo_dicts[0]
#print(f"Keys = {len(repo1)}")

#for key in sorted(repo.keys()):
#    print(key)

"""-------------------------------------------------------------"""
# Take 1 repo and get all the useful info about it 

# Get the repo name
#print("Information about each repository.")

#for repo1 in repo_dicts:

#    repo_name = repo1["name"]
#    print(f"Repo Name = {repo_name}")
#
#    # Get the owner
#    repo_owner = repo1["owner"]["login"]
#    print(f"Repo Owner = {repo_owner}")
#
#    # Get the no of stars
#    repo_stars = repo1["stargazers_count"]
#    print(f"Total stars = {repo_stars}")
#
#    # Get repos webpage
#    repos_webpage = repo1["html_url"]
#    print(f"Repos Webpage = {repos_webpage}")
#
#    # Get when repo was created 
#    created_at = repo1["created_at"]
#    print(f"Repo created at = {created_at}")
#
#    # Get when repo was last updated 
#    updated_at = repo1["updated_at"]
#    print(f"Repo last updated = {updated_at}")
#
#    # Get the repo desc
#    repo_desc = repo1["description"]
#    print(f"The repo desc = {repo_desc}")
#
#    #
#    print("\n")

"""-------------------------------------------------------------"""
# Plot the graph 
import plotly.express as px 

# repo name 
repo_name = []

for repo in repo_dicts:
    aa = repo["name"]
    repo_name.append(aa)
#print(repo_name)

# no of stars 
stars = []

for st in repo_dicts:
    aa = st["stargazers_count"]
    stars.append(aa)
#print(stars)

# hover text 

owner = []
description = []
hover_texts = []

for o in repo_dicts:
    aa = o["owner"]["login"]
    owner.append(aa)
#print(f"Owner = {owner}")

for desc in repo_dicts:
    aa = desc["description"]
    description.append(aa)
#print(f"Description = {description}")

for stuff in repo_dicts:
    owner = stuff["owner"]["login"]
    description = stuff["description"]
    
    hover_stuff = f"{owner}<br /> {description}"
    hover_texts.append(hover_stuff)

# Clickable links 
# Turn repo names into active links  
links = []

for stuff in repo_dicts:
    repo_name = stuff["name"]
    repo_url = stuff["html_url"]

    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    links.append(repo_link)

# title
title = "Most starred Python Projects on github"

# labels
labels = {"x":"Repos","y":"Stars"}

# figure 
fig = px.bar(x=links, y=stars, title=title, labels=labels,
             hover_name = hover_texts)

# modify the layout / fig object
fig.update_layout(title_font_size = 28,
                  xaxis_title_font_size=20,
                   yaxis_title_font_size=20)

# Customize Marker Colors
fig.update_traces(marker_color="steelblue",
                  marker_opacity=0.6)


# show the fig 
fig.show()