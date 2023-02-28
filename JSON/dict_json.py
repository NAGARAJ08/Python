import json

dict = {'name': 'Bob',
        'age': 12,
        'children': None
        }
data = json.dumps(dict,indent=4)
print(data)

