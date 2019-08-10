import requests
import json

response = requests.get(url="https://api.publicapis.org/entries", params={"category":"animal", "https": True})

result = response.json()

#print(result)

#https://api.publicapis.org/entries?category=animals&https=true

APIS = list()

for entry in result['entries']:
    APIS.append(entry['API'])
    APIS.append(entry['API'])

APIS = list(set(APIS))

print(len(APIS))
