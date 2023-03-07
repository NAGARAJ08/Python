# update and insert (update + insert = upsert).

from pymongo import InsertOne , DeleteOne,ReplaceOne
import pymongo


import pprint

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Student_data"]

colletions = db["student_info"]


res  = [InsertOne({"name":"ZZZ","USN":"1DS231L"}),
        InsertOne({"name":"RRR","USN":"1DS231R"}),
        DeleteOne({"name":"ABB"}),
        ReplaceOne({"name":"AAC"},{"name":"ABB"},upsert=True)        
        ]

colletions.bulk_write(res)

x = colletions.find()

for i in x:
    printer.pprint(i)

    
