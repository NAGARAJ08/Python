import os
import pprint
import pymongo
from bson.json_util import dumps,loads

printer = pprint.PrettyPrinter()
client  = pymongo.MongoClient("mongodb://localhost:27017")

mydb = client["user_shpping_list"]

collections = mydb["items"]


curser = collections.find()

list_cusrser = list(curser)

json_info = dumps(list_cusrser,indent=2)


with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/MongoDB/Shopping_list',"Shopping_list.json"),"w") as f:

    f.write(json_info)