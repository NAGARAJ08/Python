import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

doc = mycol.find().sort("name",-1)

# for ascending order we can just sya .sort("name") or .sort("name",1)
# for descending order we write as .sort("name",-1)

for i in doc:
    print(i)