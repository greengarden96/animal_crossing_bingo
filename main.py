import json

from villagers_class import Villager
import random

grid = 5
items = grid * grid
villagers_number = 391
with open('data/villagers_data.json', 'r') as file:
    villagers = json.load(file)

card=[]
for i in range(items-1):
    number=random.randint(1,391)
    card.append(villagers[str(number)])
print(card)
