import pymongo
from pymongo import MongoClient 
  
  
class Bank_data():


    def Add_account(self, Account_no, Account_customer, Account_name, Account_age, Account_dob, Account_aadhar, Account_pan, Account_add, Account_amt, Account_type):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic_add={
            "AccountNo":Account_no,
            "CustomerId":Account_customer,
            "Name":Account_name,
            "Age":Account_age,
            "Dob":Account_dob,
            "AadharNO":Account_aadhar,
            "PanCard":Account_pan,
            "Address":Account_add,
            "Amount":Account_amt,
            "AccountType":Account_type
        }
        insert=Collection.insert_one(dic_add)


    def test(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic={
                "Username":"Guddu.py",
            "Password":"Guddu.py",
            "post":"Employee"
        }
        insert=Collection.insert_one(dic)

    def Deposit(self, accuum):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        filter = { 'Account_number': accnum }
        newvalues = { "$set": { 'Amount': 25 } }

        Collection.update_one(filter, newvalues) 
        dic={

        }
        



    def add_user(self, designation, user_name, Pasword):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        add_userdic={
            "post":designation,
            "Username":user_name,
            "Password":Pasword
        }
        add_user=Collection.insert_one(add_userdic)



    def fetch_all(self,post, u_name, pass_word):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        if post==1:
            result = Collection.find_one({"post":"Manager",
                                      "Username":u_name,
                                      "Password":pass_word})
            
        elif post==2:
            result = Collection.find_one({"post":"Employee",
                                      "Username":u_name,
                                      "Password":pass_word})
            
        else:
            pass

#obj=Bank_data()
#obj.fetch_all("Tahzeeb.py", "Tahzeeb.py")
#obj.test()