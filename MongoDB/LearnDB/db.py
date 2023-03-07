''''
MongoDB is a NoSql database that stores data in the BSON format i.e (Binary JSON)

MongoDB is document-oriented. 

Table in RDBMS is called a Collection in MongoDB.
'''

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  #27017 is the default port

mydb = myclient["mydatabase"]



mycollection = mydb["customers"]

# these collections have the data as in the form of dictionary know as postss

# _id is used to access the posts

# mydict = {"name": "John", "address": "Highway 37" }

# x = mycollection.insert_one(mydict)

# print(myclient.list_database_names())

# print(x.inserted_id)

# print(myclient.list_database_names())
# print(mydb.list_collection_names())


mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]


# so _id above basically acts as a primary key

x = mycollection.insert_many(mylist)

print(x.inserted_ids)
