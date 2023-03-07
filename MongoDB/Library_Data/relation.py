import pprint
import pymongo

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Library_info"]

collections = db["Books"]


'''
documnet embed
'''


rental = {

    "name":"John",
    "street":"near Alphine tree",
    "city":"Alaska",
    "Country":"US",
    "rental_id":"640430c83b2f6fcbbccc9ae7" #this field will act as a Foreign key
}

def add_private_key(book_id,rental):

    from bson.objectid import ObjectId

    _id = ObjectId(book_id)

    collections.update_one({"_id":_id},{"$addToSet":{'rental':rental}})
    # The $addToSet operator adds or appends a value to an array, only if the value does not exist in the array. 


# add_private_key("640430c83b2f6fcbbccc9ae7",rental)



'''
OUTPUT:

{'_id': ObjectId('640430c83b2f6fcbbccc9ae7'),
 'author': 'Paul Barry',
 'copies': 120,
 'published_date': '12 Aug',
 'rental': [{'Country': 'US',
             'city': 'Alaska',
             'name': 'John',
             'rental_id': '640430c83b2f6fcbbccc9ae7',
             'street': 'near Alphine tree'}],
 'title': 'Head First Python: A Brain-Friendly Guide '}

'''

