import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# return only the addresses, not the _ids:
# you get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)