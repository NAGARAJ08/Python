import pymongo

client  = pymongo.MongoClient("mongodb://localhost:27017")

mydb = client["user_shpping_list"]

collections = mydb["items"]

# dict_1 = {
#   "item_name" : "blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340
# }
document_1 = {
  "_id" : "BF00001CFOOD",
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour"
}
# x = collections.insert_one(document_1)

# print(client.list_database_names()) 

x = collections.find()

for i in x:
    print(i)
