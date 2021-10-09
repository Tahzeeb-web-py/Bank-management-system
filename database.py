import pymongo
from pymongo import MongoClient 
  
  
class Bank_data():





    def delete_account(self, del_Accountno,del_aadharno):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        dic_delete={'Account No':del_Accountno,
        'Aadhar No':del_aadharno
        }
        Collection.delete_one(dic_delete)
        ##print(del_Accountno)


    def Add_account(self,Accountno,FirstName, LastName, FatherName, MotherName, ContactNo, AadharNo, PanCard, Dob,Address, City, Zip, Gender, AlternativeNo, Amount):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        dic_add={
            'Account No':Accountno,
            'First Name':FirstName,
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
        ##print(dic_add)


    def Add_Newuser(self, username, user_name, password, post, no_mobile):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic={"Name":username,
                "Username":user_name,
            "Password":password,
            "post":post,
            "Contact No":no_mobile
        }
        insert=Collection.insert_one(dic)

    def delete_user(self, del_username, del_pass, del_mobile_no):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic={
            "Username":del_username,
            "Password":del_pass,
            "Contact No":del_mobile_no
        }
        Collection.delete_one(dic)
        #print(dic)

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

    def get_data_emp(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        dic=Collection.find({},
            {
            "_id":0
            }
            )
        #print(dic)
        return dic
    

    def get_data_customer(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        dic=Collection.find({},
            {
            "_id":0,
            "Alternative No":0,
            "Address":0,
            "Address code":0,
            "City":0,
            
            "Last Name":0
            }
            )
        #print(dic)
        return dic



    def account_no_declaration(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["account_no"]#collection name

        for dic in Collection.find({},{
            "_id":0
        }):
         v=dic["Accnum"]
         ##print(v)
         return v
    def alter_acc(self, num, transnum):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["account_no"]#collection name
        myquery = { "Accnum":num }
        newvalues = { "$set": { "Accnum": transnum } }

        Collection.update_one(myquery, newvalues)


    def deposit_amt(self, accno, amount1):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        
        search={
            "Account No":accno
        }
        for found in Collection.find(search,{"_id":0, "Amount":1}):
            a=found['Amount']
            
            b=int(a)+int(amount1)
            
        result = Collection.update_one({"Account No":accno},{"$set":{"Amount":b}}
        )

    def withdrawal_amt(self, accno, amount1):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]#collection name
        search={
        "Account No":accno
        }
        for found in Collection.find(search,{"_id":0, "Amount":1}):
            a=found['Amount']
            
            if int(a)>int(amount1):
                b=int(a)-int(amount1)
                result = Collection.update_one({"Account No":accno},{"$set":{"Amount":b}})
                return 1
            else:
                return 0
    def manager_info(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        myq={'post':'Manager'}
        for dic in Collection.find(myq):
            name=dic['Name']
            return name
    def transfer_db(self,transferacc,depoacc, amt):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]
        trans={'Account No':transferacc}
        for dic in Collection.find(trans):
            tra=dic['Amount']
            print(tra)
        depo={'Account No':depoacc}
        for pic in Collection.find(depo):
            dep=pic['Amount']
            print(dep)
        if int(transferacc)>int(amt):
                b=int(tra)-int(amt)
                result = Collection.update_one({"Account No":transferacc},{"$set":{"Amount":b}})
                return 1
        else:
            print('sorry')
            
        b=int(dep)+int(amt)
        result = Collection.update_one({"Account No":depoacc},{"$set":{"Amount":b}})
    def balance_valid(self, accnumber):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Accounts"]
        myquery={
            'Account No':accnumber
        }
        for x in Collection.find(myquery):
            #print(x['Amount'])
            return x['Amount']




#obj=Bank_data()
#obj.manager_info()         




