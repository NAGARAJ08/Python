import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
myD = myclient["mydatabase"]
mycollection = myD["customers"]

q = {"address":{"$regex":"^S"}}  #start with S

doc = mycollection.find(q)

for i in doc:
    print(i)