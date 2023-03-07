import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Student_data"]

colletions = db["student_info"]

# print(client.list_database_names())

# info = {"name": "ABC","USN":"1DS1232D"}

# x = colletions.insert_one(info)

# print(x.inserted_ids)

'''
Let's add more student data 
'''

info = [

    {"name": "AAB","USN":"1DS323H"},
    {"name": "AAC","USN":"1DS343H"},
    {"name": "WWA","USN":"1DS231H"},
    {"name": "PER","USN":"1DS333H"},
    {"name": "OEW","USN":"1DS392H"},
    {"name": "CCA","USN":"1DS383H"},
    {"name": "DDQ","USN":"1DS353H"},
    {"name": "BBQ","USN":"1DS373H"},
    {"name": "MMQ","USN":"1DS303H"}
]

x = colletions.insert_many(info)
print(x.inserted_ids)





# query = {"name":"ABC"}
# colletions.delete_one(query)
# # here we deleted a student named ABC 


# lets update the data here say we want to rename the studet name of WWA to WWA-B
query = {"name":"MMQ"}
updata = {"$set":{"name":"MMA-B"}}

# $set operator replaces the value of a field with the specified value. 
colletions.update_one(query,updata)



x = colletions.find().sort("USN")  # this sorts the students data in the ascending order

# looping to print the data in the collection
for i in x:
    print(i)
