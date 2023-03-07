import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["mydatabase"]

coll = db["customers"]

query = {"address":"Mountain 21"}


# coll.delete_one(query)


for i in coll.find():
    print(i)
