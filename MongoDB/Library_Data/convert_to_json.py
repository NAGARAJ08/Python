import os
import pprint
import pymongo
from bson.json_util import dumps,loads
printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Library_info"]

collections = db["Books"]

curser = collections.find()

list_cusrser = list(curser)

json_info = dumps(list_cusrser,indent=2)


with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/MongoDB/Library_Data/',"Library_data.json"),"w") as f:

    f.write(json_info)