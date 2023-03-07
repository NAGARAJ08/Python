import pymongo
from bson.json_util import dumps,loads
import os

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Student_data"]

colletions = db["student_info"]


curser = colletions.find()

list_curser = list(curser)

json_data = dumps(list_curser,indent=4)

with open(os.path.join('/home/nagaraj/pythonLearn/pyproject/python/MongoDB/StudentDB','studentDB.json'),'w') as data:
    data.write(json_data)