import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]


q = {"address":"Valley 345"}

nd = {"$set":{"address":"valley 340"}}

mycol.update_one(q,nd)

x = mycol.find()

for i in x:
    print(i)