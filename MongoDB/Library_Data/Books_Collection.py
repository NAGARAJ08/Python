'''
Database is made up of collections

collections are made up of the Documents


'''
import pprint
import pymongo

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Library_info"]

collections = db["Books"]

dbs = client.list_database_names()

# print(dbs)

# print(db.list_collection_names())


def insert_document():
    mycol = db["Books"]

    documnet = {
        "author":"ABC",
        "title":"Aphabets by ABC",
        "published_date":"25 Jan",
        "copies" :100
    }

    mycol.insert_one(documnet)
    # print(x.inserted_ids)



def insert_many_documents():
    
    author = ["Eric Matthes","Paul Barry","Zed A. Shaw","Brian W. Kernighan, Dennis M. Ritchie"," AI Sweigart"]

    title = [

        "Python Crash Course: A Hands-On, Project-Based Introduction to Programming",
        "Head First Python: A Brain-Friendly Guide ",
        "Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code",
        "C Programming Language",
        "Automating the Boring Stuff With Python"
    ]

    published_date = ["9 Jan","12 Aug","8 Apr","8 Jun","16 May"]

    copies = [120,100,300,40,400]

    docs = []
    for author,title,published_date,copies in zip(author,title,published_date,copies):

        doc = {"author":author,"title":title,"published_date":published_date,"copies":copies}
        # collections.insert_one(doc)
        docs.append(doc)

    collections.insert_many(docs)


def display_all_data():
    mycol = db["Books"]

    for i in mycol.find():
        printer.pprint(i)
        print()
    
    # print(list(mycol.find())) #this will print all the data in the form of List


 
def display_one_rec():

    data = collections.find_one({"author":"Paul Barry"})
    printer.pprint(data)


def count_data():

    count = collections.count_documents(filter={})
    print("No of Books Record is: ",count)


def get_books_by_id(book_id):
    from bson.objectid import ObjectId

    _id = ObjectId(book_id)
    book = collections.find_one({"_id":_id})
    printer.pprint(book)


def get_copies_range(min_copies,max_copies):
    
    query ={"$and":[
        
            {"copies":{"$gte":min_copies}},#gte - greater than equal to
            {"copies":{"$lte":max_copies}}  #lte - less than equal to
        ]}
    
    '''
    [Similar to the below Query]
    SELECT * FROM Books WHERE copies>=min_copies AND copies <= max_copies 
    '''
    copy = collections.find(query).sort("copies")

    for i in copy:
        printer.pprint(i)

def display_only_cols():
    # here 0 means do not show the ID field 
    col = {"_id":0,"author":1,"copies":1}
    x = collections.find({},col)

    for i in x:
        printer.pprint(i)


def update_record_by_id(Book_id):

    from bson.objectid import ObjectId

    _id = ObjectId(Book_id)

    all_update = {

        "$set":{"Shipping Available":False}, #just adding a boolean field
        "$inc":{"copies":20}
    }

    collections.update_one({"_id":_id},all_update)


def remove_a_field(Book_id):

    from bson.objectid import ObjectId

    _id = ObjectId(Book_id)

    collections.update_one({"_id":_id},{"$unset":{"Shipping Available":""}})


def delete_doc_by_id(book_id):

    from bson.objectid import ObjectId

    _id = ObjectId(book_id)

    collections.delete_one({"_id":_id})




def limit_query():
    
    n = int(input("Enter the No of Limited Documnets to be displayed: \t"))
    s = int(input("Enter the No of Skips to be performed before fetching the Documents: \t"))
    x = collections.find().limit(n).skip(s)
    # this displays only limited data

    for i in x:
        printer.pprint(i)




# insert_document()
# insert_many_documents()
# display_all_data()
# display_one_rec()
# count_data()
# get_books_by_id("640430c83b2f6fcbbccc9ae7")
# get_copies_range(100,350)
# display_only_cols()

# update_record_by_id("640430c83b2f6fcbbccc9ae7")
# remove_a_field("640430c83b2f6fcbbccc9ae7")

# delete_doc_by_id("640430c83b2f6fcbbccc9ae8")

# get_books_by_id("640420e1be7e3deb58ff53a2")

# limit_query()