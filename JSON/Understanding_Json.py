import json

with open('info.json', 'r') as f:
    data = json.load(f)

print(data)
