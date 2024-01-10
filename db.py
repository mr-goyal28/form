import pymongo

myclient = pymongo.MongoClient("mongodb+srv://goyalsaab1312:9991166591K@cluster0.dyl0bl2.mongodb.net/")

mydb = myclient["formdata"]
print(mydb)
mycol = mydb["forms"]
print(mycol)

