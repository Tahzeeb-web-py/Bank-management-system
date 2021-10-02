import pymongo
from pymongo import MongoClient 
  
  
class Bank_data():


    def Add_account(self,Accountno,FirstName, LastName, FatherName, MotherName, ContactNo, AadharNo, PanCard, Dob,Address, City, Zip, Gender, AlternativeNo, Amount):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        dic_add={
            'Account No':Accountno,'First Name':FirstName,
        'Last Name':LastName,
        "Father's Name":FatherName,
        "Mother's Name":MotherName,
        'Contact No':ContactNo, 
        'Alternative No':AlternativeNo,
        'Aadhar No':AadharNo, 
        'Pan No':PanCard, 
        'Date of Birth':Dob,
        'Address':Address, 
        'City':City, 
        'Address code':Zip, 
        'Sex':Gender, 
        'Amount':Amount

            
        }
        insert=Collection.insert_one(dic_add)
        #print(dic_add)


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

    def Deposit(self, accuum,amt):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        filter = { 'Account_number': accnum }
        newvalues = { "$set": { 'Amount': amt} }

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