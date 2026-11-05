import json 
import requests 
from pathlib import Path

from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)
print(f"Status Code = {response.status_code}")

# Convert the response into python dictionary 
submission_ids = response.json()
#print(response_dict.keys())

# now give it a output path (file)
#path = Path("C:/Users/Shivam/Desktop/Alien Invasion/top_articles.json")

#dumps = json.dumps(response_dict, indent=4)

# write it into the file 
#path.write_text(dumps)

"""----------------------------------------"""
submission_dicts = []

for ids in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{ids}.json"
    response = requests.get(url)
    #print(f"id={ids} \t Status = {response.status_code}")

    # Convert each response into python dictionary 
    response_dict = response.json()

    # Building a dictionary for each article 
    dictionary = {
                "title": response_dict["title"],
                "discuss_link": f"https://news.ycombinator.com/item?id={ids}",
                "comments": response_dict["descendants"]
    }

    # Add dictionary to our list 
    submission_dicts.append(dictionary)

# Sort the articles by comments 
sorted_dicts = sorted(submission_dicts, 
                      key = itemgetter('comments'), 
                      reverse=True)

for article in submission_dicts:
    print(f"\nTitle = {article["title"]}")
    print(f"Discussion Link = {article["discuss_link"]}")
    print(F"Comments : {article["comments"]}")