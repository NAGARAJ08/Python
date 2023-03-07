import pymongo
import pprint

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.social_network

my_collections = db.user_list

profiles = [
    {"_id":1, "user":"Amit", "title":"Python", "comments":5},
    {"_id":2, "user":"Drew",  "title":"JavaScript", "comments":15},
    {"_id":3, "user":"Amit",  "title":"C++", "comments":6},
    {"_id":4, "user":"Drew",  "title":"MongoDB", "comments":2},
    {"_id":5, "user":"Cody",  "title":"Perl", "comments":9}
]


data = [

    {"_id":6, "user":"Shiva", "title":"Python", "comments":15},
    {"_id":7, "user":"Raj", "title":"Python", "comments":25},
    {"_id":8, "user":"Alex", "title":"Java", "comments":1},
    {"_id":9, "user":"Avir", "title":"MongoDB", "comments":45},
    {"_id":10, "user":"NK", "title":"C++", "comments":9},
]

# my_collections.insert_many(data)

x = my_collections.find()

for i in x:
    printer.pprint(i)

    
 