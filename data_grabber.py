#This file should only be run once to download the data from the api
from villagers_class import Villager
import requests
import json

# get villager name and ID
response = requests.get('http://acnhapi.com/v1/villagers/').json()
villagers = {}

for key, value in response.items():
    villager_id = value.get('id')
    villager_name = value.get('name').get('name-USen')
    villagers[villager_id]=villager_name
with open('data/villagers_data.json', 'w') as file:
    file.write(json.dumps(villagers))

# # to get the images
# for item in villagers:
#     image_response = requests.get(f'http://acnhapi.com/v1/images/villagers/{item.id}')
#     with open(f'images/{item.name}.png', 'wb') as file:
#         file.write(image_response.content)

