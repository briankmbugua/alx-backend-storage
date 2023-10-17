import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
# find the first document in the customers collection
x = mycol.find_one()
# find all documents in the customers collection
x = mycol.find()
for x in x:
    print(x)

# find only some fields in the result
# the second parameter of the find() method is an object describing which fields to include in the result

for x in mycol.find({}, {"_id": 0}):
    print(x)
