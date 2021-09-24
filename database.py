import pymongo
from pymongo import MongoClient 
  
  


myclient = MongoClient("mongodb://localhost:27017/") #making connection 
db = myclient["bank_management_system_2021"]#database name
Collection = db["Login_post"]#collection name
dic={
    "Username":"Tahzeeb.py",
    "Password":"Tahzeeb.py"
}
insert=Collection.insert_one(dic)