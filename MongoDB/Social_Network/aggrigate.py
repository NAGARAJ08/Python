import pymongo
import pprint
# this is a aggrigate method impl

printer = pprint.PrettyPrinter()

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.social_network

my_collections = db.user_list


def group_by_users():

    agg_Res = my_collections.aggregate(
        [{
            "$group":
            {
                "_id":"$user",
                "num_Tutorial":{"$sum":1}  
              }  }
        ])
    
    for i in agg_Res:
        printer.pprint(i)


def group_by_title():

    agg_Res = my_collections.aggregate(
        [
            {
                "$group":
                {
                    "_id":"$title",
                    "total_enrolled":{"$sum":1}
                }
            }
        ]
    )

    for i in agg_Res:
        printer.pprint(i)



def group_by_popularity():

    agg_res = my_collections.aggregate(

        [
            {
                "$group":
                {
                    "_id":"$Popularity",
                    "count":{"$sum":1}
                }
            }
        ]
    )

    for i in agg_res:
        print(i)



def set_popularity():

    my_collections.update_many(

        {"comments":{"$gte":30}}, #for High Popularity
        # {"comments":{"$and" :[{"$gte":10},{"lte":30}]}},

        # {"comments":{"$gt":10}},
        # {"comments":{"$lt":10}},
        {"$set":{"Popularity":"High"}}
    )



def get_distinct():

    print(my_collections.distinct("title"))
    print(my_collections.distinct("comments"))

def display():

    x = my_collections.find()

    for i in x:
        printer.pprint(i)


# group_by_users()
# group_by_title()
# set_popularity()
# group_by_popularity()
# display()
get_distinct()