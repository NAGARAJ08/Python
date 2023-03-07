import pprint
import pymongo

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Library_info"]

collections = db["rental"]


rental = {

    "name":"Bob",
    "street":"Mountain View",
    "city":"Sunnyvale",
    "Country":"US",
    "rental_id":"640420e1be7e3deb58ff53a2" #this field will act as a Foreign key
}

def add_relation(book_id,rental):
    
    from bson.objectid import ObjectId
    _id = ObjectId(book_id)

    rental = rental.copy()

    rental["rental_id"] = book_id

    collections.insert_one(rental)

def display():
    x = collections.find()

    for i in x:
        printer.pprint(i)


# add_relation("640420e1be7e3deb58ff53a2",rental)
display()