import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]
mycollection = mydb["customers"]

# query = {"address": "Park Lane 38"}

# query = {"address":{"$gt":"S"}}  #the address start should be greater than S

query = {"name":{"$gt":"M"}}

doc = mycollection.find(query)

for x in doc:
    print(x)