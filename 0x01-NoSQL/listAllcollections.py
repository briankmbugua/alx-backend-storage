import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print(mydb.list_collection_names()) 


def list_all():
    """List all docucments in a collection"""
    mydoc = mycol.find()
    for x in mydoc:
        print(x)