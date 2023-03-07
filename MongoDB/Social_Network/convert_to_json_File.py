import pymongo
from bson.json_util import dumps,loads
import os
import pprint

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.social_network

my_collections = db.user_list


cursor = my_collections.find()

# conver the curor to the list of dictionaries

list_curser = list(cursor)

json_data = dumps(list_curser,indent=3)



with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/MongoDB/Social_Network','Social_network.json'),'w') as data:
    data.write(json_data)