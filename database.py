import pymongo
from pymongo import MongoClient 
  
  
class Bank_data():


    def test(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic={
                "Username":"Tahzeeb.py",
            "Password":"Tahzeeb.py"
        }
        insert=Collection.insert_one(dic)
    
    def fetch_all(self, u_name, pass_word):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        result = Collection.find_one({"Username":u_name,
                                        "Password":pass_word})
        print(result)
#obj=Bank_data()
#obj.fetch_all("Tahzeeb.py", "Tahzeeb.py")