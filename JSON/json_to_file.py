import json

dict = {"name": "Bob",
        "languages": ["English", "French"],
        "married": True,
        "age": 32
        }

with open('person.json', 'w') as j_file:
    json.dump(dict, j_file, indent=4,sort_keys=True)
