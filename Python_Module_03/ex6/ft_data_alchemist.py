import random

names =  ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

all_cap = [name.capitalize() for name in names]
o_cap = [name for name in names if name == name.capitalize()]
print("=== Game Data Alchemist ===")
print()
print(f"Initial list of players: {names}")
print(f"New list with all names capitalized: {all_cap}")
print(f"New list of capitalized names only: {o_cap}")
print()
dic = {name: random.randint(0,1000) for name in all_cap}
print(f"Score dict: {dic}")
avg = round(sum(dic.values()) / len(dic), 2)
print(f"Score average is {avg}")
high = {name: score for name, score in dic.items() if score > avg}
print(f"High scores: {high}")