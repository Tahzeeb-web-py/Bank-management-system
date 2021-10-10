import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import OptionMenu, messagebox
from tkcalendar import Calendar
from database import Bank_data
import pymongo
from pymongo import MongoClient
import random
from random import randrange
from tkinter.scrolledtext import ScrolledText



obj=Bank_data()#database.py object Created..........



#..................................Class Account....................................................................................................
class Account():



        def reset_note(self):
                self.notice_entry.delete(0, END)
        def delete_treeview(self):
                curItem = self.tree_note.focus()
                temp=self.tree_note.item(curItem, 'values')
                #print(temp[0])
                dd=int(temp[0])
                obj.delete_notice(dd)
                #print(type(dd))
                


                selected_item = self.tree_note.selection()[0]
                self.tree_note.delete(selected_item)
                
        def send_data_to(self):
                id=randrange(1,99999)
                v=obj.add_notice(id, self.notice_entry.get())

  
        def notice(self):
                self.npew=StringVar()
                self.notice_page=tk.Tk()
                self.notice_page.geometry('1400x750+10+10')
                self.notice_page.title('Notice')
                self.notice_page['bg']='cyan'
                note=StringVar()
                heading_frame=Frame(self.notice_page, width=1300, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame( self.notice_page,width=1300, height=570, bg='peachpuff4', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame( self.notice_page,width=1300, height=70, bg='White', relief=RIDGE).place(x=50, y=670)
                self.entry_frame=Frame(self.notice_page, width=800, height=550, bg='white', relief=GROOVE).place(x=78, y=100)
                self.entry_frame=Frame(self.notice_page, width=500, height=40, bg='BLACK', relief=RIDGE).place(x=300, y=150)
                lbs=Label(self.notice_page, text='Notice:',font=('arail', 20, 'bold'), bg='white').place(x=110, y=150)
                self.notice_entry=Entry(self.notice_page, textvariable=note,font=35, width=43)
                self.notice_entry.place(x=310, y=155)
                entry_note = ttk.Scrollbar(self.notice_page, orient="horizontal", command=self.notice_entry.xview)
                entry_note.place(x=300, y=200)
                self.notice_entry.configure(xscrollcommand=entry_note.set)
                self.reset_button=Button(self.notice_page, text='Clear', bg='Red', fg='white', width=15,font=('arail', 8, 'bold'), command=self.reset_note)
                self.reset_button.place(x=688, y=200)






















                Label(self.notice_page, text='Notice', font=('helvetica', 35, 'bold'),bg='White').place(x=550, y=15)
                column_notice=('#1','#2')
                self.tree_note=ttk.Treeview(self.notice_page, columns=column_notice, show='headings', height=26)
                self.tree_note.column('#1',anchor=CENTER, width=50)
                self.tree_note.column('#2',anchor=CENTER, width=350)
                self.tree_note.heading('#1', text='Id no')
                self.tree_note.heading('#2', text='Notice')
                self.tree_note.bind('<<TreeviewSelect>>')
                self.tree_note.place(x=910, y=100)

                for x in obj.fetch_notice():
                        print(x)
                        z=x['no']
                        z1=x['notices']
                       

                        self.tree_note.insert("",tk.END, value=[z, z1])
                vsb = ttk.Scrollbar(self.notice_page, orient="vertical", command=self.tree_note.yview)
                vsb.place(x=1320, y=90)
                self.tree_note.configure(yscrollcommand=vsb.set)
                
                exit_button_cust_list=Button(self.notice_page, text='Exit', bg='red', fg='Black', width=15,command=self.notice_page.destroy,font=('arail', 12, 'bold'))
                exit_button_cust_list.place(x=1150, y=690)
                refresh_button=Button(self.notice_page, text='Refresh', bg='yellow', fg='Black', width=15,font=('arail', 12, 'bold'))
                refresh_button.place(x=910, y=690)
                save_button=Button(self.notice_page, text='Save', bg='Green', fg='white', width=15,font=('arail', 12, 'bold'),command=self.send_data_to)
                save_button.place(x=78, y=690)
                delete_button=Button(self.notice_page, text='Delete', bg='red', fg='White', width=15,font=('arail', 12, 'bold'),command=self.delete_treeview)
                delete_button.place(x=350, y=690)



                self.notice_page.mainloop()
        
        
                

        def customer_list(self):
                cust_list=tk.Tk()
                cust_list.geometry('1400x750+10+10')
                cust_list.title('Customer list')
                cust_list['bg']='grey'
                heading_frame=Frame( cust_list, width=1300, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(cust_list,width=1300, height=570, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(cust_list,width=1300, height=70, bg='White', relief=RIDGE).place(x=50, y=670)

                Label(cust_list, text='Customer List', font=('helvetica', 35, 'bold'),bg='White').place(x=550, y=15)


                column_cust=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10')

                tree_cust=ttk.Treeview(cust_list, columns=column_cust, show='headings', height=26)

                #tree_emp.column('#0',anchor=CENTER, width=1)
                tree_cust.column('#1',anchor=CENTER, width=100)
                tree_cust.column('#2',anchor=CENTER, width=160)
                tree_cust.column('#3',anchor=CENTER, width=160)
                tree_cust.column('#4',anchor=CENTER, width=160)
                tree_cust.column('#5',anchor=CENTER, width=120)
                tree_cust.column('#6',anchor=CENTER, width=80)
                tree_cust.column('#7',anchor=CENTER, width=160)
                tree_cust.column('#8',anchor=CENTER, width=120)
                tree_cust.column('#9',anchor=CENTER, width=100)
                tree_cust.column('#10',anchor=CENTER, width=120)
               
                
                
                tree_cust.heading('#1', text='Account No')
                tree_cust.heading('#2', text='Name')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                tree_cust.heading('#3', text="Father's Name")
                tree_cust.heading('#4', text="Mother's Name")
                tree_cust.heading('#5', text='Contact No')
                tree_cust.heading('#6', text='sex')
                tree_cust.heading('#7', text='Aadhar No')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                tree_cust.heading('#8', text='Pan No')
                tree_cust.heading('#9', text='Date of Birth')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                tree_cust.heading('#10', text='Account Balance')
               

                tree_cust.bind('<<TreeviewSelect>>')
                tree_cust.place(x=60, y=100)
                vsb = ttk.Scrollbar(cust_list, orient="vertical", command=tree_cust.yview)
                vsb.place(x=1250, y=70)
                tree_cust.configure(yscrollcommand=vsb.set)

                for x in obj.get_data_customer():
                        f1=x["Account No"]
                        f2=x["First Name"]
                        f3=x["Father's Name"]
                        f4=x["Mother's Name"]
                        f5=x["Contact No"]
                        f6=x["Sex"]
                        f7=x["Aadhar No"]
                        f8=x["Pan No"]
                        f9=x["Date of Birth"]
                        f10=x["Amount"]

                        tree_cust.insert("",tk.END, value=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10])
                


                exit_button_cust_list=Button(cust_list, text='Exit', bg='red', fg='Black', width=15,command=cust_list.destroy,font=('arail', 12, 'bold'))
                exit_button_cust_list.place(x=1150, y=690)
                cust_list.mainloop()






        def Employee_list(self):
                obj.get_data_emp()
                emp_list=tk.Tk()
                emp_list.geometry("950x700")
                emp_list.title('Employee list')
                emp_list['bg']='grey'


                search_var=StringVar()

                heading_frame=Frame(emp_list, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(emp_list,width=850, height=510, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(emp_list,width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=610)
                label_firstname=Label(emp_list, text='Employee List',bg="White",font=('arail', 20, 'bold')).place(x=370, y=30)

                column_emp=('#1','#2','#3','#4','#5')

                tree_emp=ttk.Treeview(emp_list, columns=column_emp, show='headings', height=23)

                #tree_emp.column('#0',anchor=CENTER, width=1)
                tree_emp.column('#1',anchor=CENTER, width=160)
                tree_emp.column('#2',anchor=CENTER, width=160)
                tree_emp.column('#3',anchor=CENTER, width=160)
                tree_emp.column('#4',anchor=CENTER, width=160)
                tree_emp.column('#5',anchor=CENTER, width=160)

                
                tree_emp.heading('#1', text='Post')
                tree_emp.heading('#2', text='Name')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                tree_emp.heading('#3', text='Username')
                tree_emp.heading('#4', text='Password')
                tree_emp.heading('#5', text='Mobile No')

                tree_emp.bind('<<TreeviewSelect>>')
                tree_emp.place(x=70, y=100)

                #contacts={}
                for x in obj.get_data_emp():
                       
                        v=x['post']
                        v1=x['Name']
                        v2=x['Username']
                        v3=x['Password']
                        v4=x['Contact No']
                       
                        tree_emp.insert("",tk.END, value=[v,v1, v2, v3, v4])
                        



                




                self.search_entry=Entry(emp_list, textvariable=search_var, width=30)
                self.search_entry.place(x=150, y=630)

                exit_button_addcustomer=Button(emp_list, text='Exit', bg='red', fg='Black', width=15,command=emp_list.destroy,font=('arail', 12, 'bold'))
                exit_button_addcustomer.place(x=700, y=630)
                
                self.Save_button_addcustomer=Button(emp_list, text='Search', bg='Green', fg='White', width=7,font=('arail', 8, 'bold'))
                self.Save_button_addcustomer.place(x=70, y=630)

                emp_list.resizable(False, False)


                emp_list.mainloop()
        
        def senddata(self):
                accnuum=obj.account_no_declaration()
                self.int_transfer=int(accnuum)
                self.randam=randrange(1,78)
                self.no=self.int_transfer+self.randam
                self.gen1=self.gen.get()
                self.Accountno=str(self.no)
                self.messtring=f"Account of this customer is {self.Accountno}."
                send_data=obj.Add_account(self.Accountno,self.FirstName.get(),self.LastName.get(),self.FatherName.get(), self.MotherName.get(), self.Contactnum.get(), self.Aadharnum.get(), self.Pan.get(),self.cal.get_date(), self.Address.get(),self.City.get(), self.Zipcode.get(), self.gen1, self.Alternativenum.get(),self.Depo_amount.get())
                #print(send_data)
                messagebox.showinfo('showinfo',self.messtring)
                obj.alter_acc(accnuum, self.no)

        def reset(self):
                self.FirstName.delete(0,END)
                self.LastName.delete(0,END)
                self.FatherName.delete(0,END)
                self.MotherName.delete(0,END)
                self.Contactnum.delete(0,END)
                self.Aadharnum.delete(0,END)
                self.Pan.delete(0,END)
                self.Address.delete(0,END)
                self.City.delete(0,END)
                self.Zipcode.delete(0,END)
                self.Alternativenum.delete(0,END)
                self.Depo_amount.delete(0,END)
        def add(self):
               
                ##print(Accountno)
                global addNew_customer
                addNew_customer=tk.Tk()
                addNew_customer.geometry("950x700+100+100")
                addNew_customer.title("Add Customer Window")
                addNew_customer['bg']='grey'
                
              
                Var_first_name=StringVar()
                var_last_name=StringVar()
                var_father_name=StringVar()
                var_mother_name=StringVar()
                var_contact_num=StringVar()
                var_aadhar_num=StringVar()
                var_pan_num=StringVar()
                var_dob=StringVar()
                self.D=tk.StringVar(addNew_customer)
                self.M=tk.StringVar(addNew_customer)
                self.Y=tk.StringVar(addNew_customer)
                var_alternative_num=StringVar()
                var_gender=StringVar()
                var_address=StringVar()
                var_city=StringVar()
                var_zip_code=StringVar()
                var_Deposit=StringVar()
                self.gen=StringVar(addNew_customer)
                dob=StringVar()
                
                heading_frame=Frame(addNew_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(addNew_customer, width=850, height=510, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(addNew_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=610)

                label_firstname=Label(addNew_customer, text='New Account Opening',bg="White",font=('arail', 20, 'bold')).place(x=330, y=30)
                label_firstname=Label(addNew_customer, text='First Name',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                self.FirstName=Entry(addNew_customer, textvariable=Var_first_name, width=35)
                self.FirstName.place(x=220, y=130)
                label_firstname=Label(addNew_customer, text='Last Name',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                self.LastName=Entry(addNew_customer, textvariable=var_last_name, width=35)
                self.LastName.place(x=220, y=170)
                label_firstname=Label(addNew_customer, text="Father's Name",font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                self.FatherName=Entry(addNew_customer, textvariable=var_father_name, width=35)
                self.FatherName.place(x=220, y=210)
                label_firstname=Label(addNew_customer, text="Mothet's Name",font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                self.MotherName=Entry(addNew_customer, textvariable=var_mother_name, width=35)
                self.MotherName.place(x=220, y=250)
                label_firstname=Label(addNew_customer, text='Contact No.',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                self.Contactnum=Entry(addNew_customer, textvariable=var_contact_num, width=35)
                self.Contactnum.place(x=220, y=290)
                label_firstname=Label(addNew_customer, text='Aadhar Card No',font=('arail', 12, 'bold'), bg='White').place(x=70, y=330)
                self.Aadharnum=Entry(addNew_customer, textvariable=var_aadhar_num, width=35)
                self.Aadharnum.place(x=220, y=330)
                label_firstname=Label(addNew_customer, text='Pan Card',font=('arail', 12, 'bold'), bg='White').place(x=70, y=370)
                self.Pan=Entry(addNew_customer, textvariable=var_pan_num, width=35)
                self.Pan.place(x=220, y=370)
                label_firstname=Label(addNew_customer, text='Date of Birth',font=('arail', 12, 'bold'), bg='White').place(x=70, y=410)
                  
                self.cal=Calendar(addNew_customer, selectmode='day', year=2000, month=1, days=22)
                self.cal.place(x=220, y=410)

                label_firstname=Label(addNew_customer, text='Alternative No',font=('arail', 12, 'bold'), bg='White').place(x=500, y=330)
                self.Alternativenum=Entry(addNew_customer, textvariable=var_alternative_num, width=35)
                self.Alternativenum.place(x=650, y=330)
                label_firstname=Label(addNew_customer, text='Gender',font=('arail', 12, 'bold'), bg='White').place(x=500, y=250)
                self.degisnation_radio1=Radiobutton(addNew_customer, text='Male', variable= self.gen, value='Male',font=('arial', 13, 'bold'), bg='white')
                self.degisnation_radio1.place(x=650, y=250)
                self.degisnation_radio=Radiobutton(addNew_customer, text='Female', variable=self.gen, value='Female',font=('arial', 13, 'bold'), bg='white')
                self.degisnation_radio.place(x=790, y=250)
                self.degisnation_radio1=Radiobutton(addNew_customer, text='Trans', variable=self.gen, value='Trans',font=('arial', 13, 'bold'), bg='white')
                self.degisnation_radio1.place(x=650, y=290)
                self.degisnation_radio=Radiobutton(addNew_customer, text='Other', variable= self.gen, value='Other',font=('arial', 13, 'bold'), bg='white')
                self.degisnation_radio.place(x=790, y=290)
                label_firstname=Label(addNew_customer, text='Address',font=('arail', 12, 'bold'), bg='White').place(x=500, y=130)
                self.Address=Entry(addNew_customer, textvariable=var_address, width=35)
                self.Address.place(x=650, y=130)
                label_firstname=Label(addNew_customer, text='City',font=('arail', 12, 'bold'), bg='White').place(x=500, y=170)
                self.City=Entry(addNew_customer, textvariable=var_city, width=35)
                self.City.place(x=650, y=170)
                label_firstname=Label(addNew_customer, text='Zip Code',font=('arail', 12, 'bold'), bg='White').place(x=500, y=210)
                self.Zipcode=Entry(addNew_customer, textvariable=var_zip_code, width=35)
                self.Zipcode.place(x=650, y=210)
                Amount_depo=Label(addNew_customer, text='Opening Deposit',font=('arail', 12, 'bold'), bg='White').place(x=500, y=370)
                self.Depo_amount=Entry(addNew_customer, textvariable=var_Deposit, width=35)
                self.Depo_amount.place(x=650, y=370)

               
                
                exit_button_addcustomer=Button(addNew_customer, text='Exit', bg='red', fg='Black', width=15,command=addNew_customer.destroy,font=('arail', 12, 'bold'))
                exit_button_addcustomer.place(x=380, y=630)
                reset_button_addcustomer=Button(addNew_customer, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'), command=self.reset)
                reset_button_addcustomer.place(x=100, y=630)
                self.Save_button_addcustomer=Button(addNew_customer, text='Add', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'), command=lambda:[self.senddata(),addNew_customer.destroy()])
                self.Save_button_addcustomer.place(x=680, y=630)
                addNew_customer.resizable(False, False)


                addNew_customer.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------              
        def send_data_delete_customer(self):
                obj.delete_account(self.Account_num.get(), self.Aadhar_num.get())
                #print(self.Account_num.get())
        def delete(self):
                dele_customer=tk.Tk()
                dele_customer.geometry("950x530+100+100")
                dele_customer.title("Delete Customer Window")
                dele_customer['bg']='grey'

                var_del_accno=StringVar()
                var_del_aadharno=StringVar()
                var_remark=StringVar()
                var_acc_name=StringVar()
                var_date=StringVar()
                self.var_verify=StringVar(dele_customer)
                heading_frame=Frame(dele_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(dele_customer, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(dele_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(dele_customer, text='Close Account',bg="White",font=('arail', 20, 'bold')).place(x=350, y=30)
                label_firstname=Label(dele_customer, text='Name of Account Holder:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                FirstName=Entry(dele_customer,textvariable=var_acc_name, width=35)
                FirstName.place(x=300, y=130)
                label_firstname=Label(dele_customer, text='Account Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                self.Account_num=Entry(dele_customer,textvariable=var_del_accno, width=35)
                self.Account_num.place(x=300, y=170)
                label_firstname=Label(dele_customer, text='Aadhar No:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                self.Aadhar_num=Entry(dele_customer,textvariable=var_del_aadharno, width=35)
                self.Aadhar_num.place(x=300, y=210)
                label_firstname=Label(dele_customer, text='Date of closing:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                

                label_firstname=Label(dele_customer, text='Remark:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                FirstName=Entry(dele_customer,textvariable=var_remark, width=35)
                FirstName.place(x=300, y=290)

                label_firstname=Label(dele_customer, text='Verify by:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=340)
                dateofcloseing=Radiobutton(dele_customer, variable=self.var_verify, value='Manager', text='Manager')
                dateofcloseing.place(x=300, y=340)
                dateofcloseing=Radiobutton(dele_customer, variable=self.var_verify, value='Employee', text='Employee')
                dateofcloseing.place(x=400,y=340)

                
                exit_button_delecustomer=Button(dele_customer, text='Exit', bg='red', fg='Black', width=15,command=dele_customer.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=380, y=470)
                reset_button_delecustomer=Button(dele_customer, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_delecustomer.place(x=100, y=470)
                Delete_button_delecustomer=Button(dele_customer, text='Close Account', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'), command=lambda:[self.send_data_delete_customer(), dele_customer.destroy()])
                Delete_button_delecustomer.place(x=680, y=470)
                dele_customer.resizable(False, False)
                dele_customer.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def send_data_add_user(self):
                obj.Add_Newuser(self.EmpName.get(), self.addusername.get(), self.addpassword.get(), self.add_post.get(), self.no_mobile.get())


        def Add_user_bank(self):
                add_user=tk.Tk()
                add_user.geometry("950x530+100+100")
                add_user.title("Add Employee Window")
                add_user['bg']='grey'
                add_Empname=StringVar()
                add_username=StringVar()
                add_mobile=StringVar()
                add_password=StringVar()
                self.add_post=StringVar(add_user)
                self.add_varify=StringVar(add_user)

                heading_frame=Frame(add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame( add_user, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame( add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(add_user, text='Add Bank Employee',bg="White",font=('arail', 20, 'bold')).place(x=350, y=30)
                label_firstname=Label(add_user, text='Name of Employee:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                self.EmpName=Entry(add_user,textvariable=add_Empname, width=35)
                self.EmpName.place(x=300, y=130)
                label_firstname=Label(add_user, text='Username:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                self.addusername=Entry(add_user,textvariable=add_username, width=35)
                self.addusername.place(x=300, y=170)
                label_firstname=Label(add_user, text='Mobile Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                self.no_mobile=Entry(add_user,textvariable=add_mobile, width=35)
                self.no_mobile.place(x=300, y=250)
                label_firstname=Label(add_user, text='Password:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                self.addpassword=Entry(add_user,textvariable=add_password, width=35)
                self.addpassword.place(x=300, y=210)

                label_firstname=Label(add_user, text='Post:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                self.select_post=Radiobutton(add_user, text='Manager', variable=self.add_post, bg='White',value='Manager')
                self.select_post.place(x=300, y=290)
                self.select_post=Radiobutton(add_user, text='Employee', variable=self.add_post,bg='White', value='Employee')
                self.select_post.place(x=420, y=290)
                self.select_post=Radiobutton(add_user, text='Staff', variable=self.add_post,bg='White', value='Staff')
                self.select_post.place(x=540, y=290)

                label_firstname=Label(add_user, text='Verify by:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=340)
                self.select_varification=Radiobutton(add_user, text='Manager', variable=self.add_varify, bg='White',value='Manager')
                self.select_varification.place(x=300, y=340)
                

                
                exit_button_delecustomer=Button(add_user, text='Exit', bg='red', fg='Black', width=15,command=add_user.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=380, y=470)
                reset_button_delecustomer=Button(add_user, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_delecustomer.place(x=100, y=470)
                Delete_button_delecustomer=Button(add_user, text='Add Account', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'),command=lambda:[self.send_data_add_user(), add_user.destroy()])
                Delete_button_delecustomer.place(x=680, y=470)
                add_user.resizable(False, False)
                add_user.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def reset_delete_user_bank(self):
                self.delusername.delete(0,END)
                self.Delmobile.delete(0, END)
                self.delpassword.delete(0, END)
        def send_delete_data(self):
                obj.delete_user(self.delusername.get(), self.delpassword.get(), self.Delmobile.get())
                #print(self.delusername.get(), self.delpassword.get(), self.Delmobile.get())
        def delete_user_bank(self):
                dele_user=tk.Tk()
                dele_user.geometry("500x530+100+100")
                dele_user.title("Delete Employee Window")
                dele_user['bg']='grey'
                del_username=StringVar()
                del_password=StringVar()
                del_mobile=StringVar()
                heading_frame=Frame(dele_user, width=450, height=70, bg='White', relief=RIDGE).place(x=25, y=10)
                middle_frame=Frame( dele_user, width=450, height=350, bg='White', relief=RIDGE).place(x=25, y=90)
                futter_frame=Frame( dele_user, width=450, height=70, bg='White', relief=RIDGE).place(x=25, y=450)
                label_firstname=Label(dele_user, text='Delete Bank Employee',bg="White",font=('arail', 20, 'bold')).place(x=100, y=30)
                label_firstname=Label(dele_user, text='Username:',font=('arail', 12, 'bold'), bg='White').place(x=50, y=170)
                self.delusername=Entry(dele_user, textvariable=del_username,width=35)
                self.delusername.place(x=200, y=170)
                label_firstname=Label(dele_user, text='Mobile Number:',font=('arail', 12, 'bold'), bg='White').place(x=50, y=250)
                self.Delmobile=Entry(dele_user,textvariable=del_mobile, width=35)
                self.Delmobile.place(x=200, y=250)
                label_firstname=Label(dele_user, text='Password:',font=('arail', 12, 'bold'), bg='White').place(x=50, y=210)
                self.delpassword=Entry(dele_user,textvariable=del_password,width=35)
                self.delpassword.place(x=200, y=210)
                exit_button_delecustomer=Button(dele_user, text='Exit', bg='red', fg='Black', width=15,command=dele_user.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=50, y=470)
                reset_button_delecustomer=Button(dele_user, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'),command=self.reset_delete_user_bank)
                reset_button_delecustomer.place(x=150, y=350)
                Delete_button_delecustomer=Button(dele_user, text='Delete Employee', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'), command=lambda:[self.send_delete_data(), dele_user.destroy()])
                Delete_button_delecustomer.place(x=280, y=470)
                dele_user.resizable(False, False)
                dele_user.mainloop()
        expression = ""
        def press(self,num):
	
	        global expression
	        self.expression = self.expression + str(num)
	        self.equation.set(self.expression)

        def equalpress(self):
	
	        try:

		        global expression
		        total = str(eval(expression))
		        self.equation.set(total)
		        self.expression = ""

	
	        except:

		        self.equation.set(" error ")
		        self.expression = ""

        def clear(self):
	        self.expression_field.delete(0, END)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def Calculator_bank(self):
                bank_cal=tk.Tk()
                bank_cal.geometry("950x530+100+100")
                bank_cal.title("Calcultor Window")
                bank_cal['bg']='grey'
                heading_frame=Frame(bank_cal, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame( bank_cal, width=850, height=350, bg='yellow', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame( bank_cal, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(bank_cal, text='Calculate',bg="White",font=('arail', 20, 'bold')).place(x=400 , y=30)
                self.equation=StringVar()
                self.expression_field = Entry(bank_cal, width=35,font=('arail', 15, 'bold') ,textvariable=self.equation)
                self.expression_field.place(x=75, y=120)
                button1 = Button(bank_cal, text=' 1 ', fg='black', bg='White',command=lambda: self.press(1), height=2, width=10)
                button1.place(x=75, y=250)
                button2 = Button(bank_cal, text=' 2 ', fg='black', bg='White',command=lambda: self.press(2), height=2, width=10)
                button2.place(x=75, y=300)
                button3 = Button(bank_cal, text=' 3 ', fg='black', bg='white',command=lambda: self.press(3), height=2, width=10)
                button3.place(x=75, y=350)
                button4 = Button(bank_cal, text=' 4 ', fg='black', bg='white',command=lambda: self.press(4), height=2, width=10)
                button4.place(x=170, y=250)
                button5=Button(bank_cal, text=' 5 ', fg='black', bg='white',command=lambda: self.press(5), height=2, width=10)
                button5.place(x=170, y=300)
                button6 = Button(bank_cal, text=' 6 ', fg='black', bg='white',command=lambda: self.press(6), height=2, width=10)
                button6.place(x=170, y=350)
                button7 = Button(bank_cal, text=' 7 ', fg='black', bg='white',command=lambda: self.press(7), height=2, width=10)
                button7.place(x=265, y=250)
                button8 = Button(bank_cal, text=' 8 ', fg='black', bg='white',command=lambda: self.press(8), height=2, width=10)
                button8.place(x=265, y=300)
                button9 = Button(bank_cal, text=' 9 ', fg='black', bg='white',command=lambda: self.press(9), height=2, width=10)
                button9.place(x=265, y=350)
                button0 = Button(bank_cal, text=' 0 ', fg='black', bg='white',command=lambda: self.press(0), height=2, width=10)
                button0.place(x=360, y=250)
                plus = Button(bank_cal, text=' + ', fg='black', bg='white',command=lambda: self.press("+"), height=2, width=10)
                plus.place(x=360, y=300)
                minus = Button(bank_cal, text=' - ', fg='black', bg='white',command=lambda: self.press("-"), height=2, width=10)
                minus.place(x=360, y=350)
                multiply = Button(bank_cal, text=' * ', fg='black', bg='white',command=lambda:self.press("*"), height=2, width=10)
                multiply.place(x=455, y=250)
                divide = Button(bank_cal, text=' / ', fg='black', bg='white',command=lambda: self.press("/"), height=2, width=10)
                divide.place(x=455, y=300)
                equal = Button(bank_cal, text=' = ', fg='black', bg='white',command= self.equalpress(), height=2, width=10)
                equal.place(x=455, y=350)
                Decimal= Button(bank_cal, text='.', fg='black', bg='white',command=lambda: self.press('.'), height=2, width=10)
                Decimal.place(x=555, y=350)


                exit_button_cal=Button(bank_cal, text='Exit', bg='red', fg='Black', width=15,command=bank_cal.destroy,font=('arail', 12, 'bold'))
                exit_button_cal.place(x=380, y=470)
                reset_button_cal=Button(bank_cal, text='Reset', bg='yellow', fg='Black',width=15,command=self.clear(), font=('arail', 12, 'bold'))
                reset_button_cal.place(x=100, y=470)
                
                bank_cal.resizable(False, False)


                bank_cal.mainloop()



objAdd_customer= Account()

class Manager():
    


    def reset_deposit(self):
        self.acc_name.delete(0, END)
        self.amonut.delete(0, END)
        self.acc_no.delete(0, END)
        return
    def reset_withdrawal(self):
        self.acc_no_withdrawal.delete(0, END)
        self.acc_name_withdrawal.delete(0, END)
        self.amonut_withdrwal.delete(0, END)
        return
    def reset_transfer(self):
        self.acc_no_withdrawal_tranfer.delete(0, END)
        self.acc_no_deposit_transfer.delete(0, END)
        self.amonut_transfer.delete(0, END)
        return

    def send_deposit(self):
        self.send=obj.deposit_amt(self.acc_no.get(), self.amonut.get())
        self.reset_deposit()
        
        #print(self.acc_no.get())
    def send_withdrawal_amt(self):
            self.send=obj.withdrawal_amt(self.acc_no_withdrawal.get(), self.amonut_withdrwal.get())
            if self.send==1:
                    self.reset_withdrawal()
            else:
                    self.messege='Insufficient Amount in Account'
                    messagebox.showinfo('showinfo',self.messege)
                    self.reset_withdrawal()

    def transfer_amt(self):
        obj.transfer_db(self.acc_no_withdrawal_tranfer.get(),self.acc_no_deposit_transfer.get(),self.amonut_transfer.get())
        self.reset_transfer()
    def check_balance(self):
            balance=obj.balance_valid(self.balance_account_no.get())
            #print(balance)
            #return balance
            ff=f'Total Amount in the bank account No:   {self.balance_account_no.get()} is:     {balance}'
            self.messege='Balance in Account'
            messagebox.showinfo('showinfo',ff)

    



    

        


    def Gui(self):
        self.M_name=obj.manager_info()
        manager_window=tk.Tk()
        manager_window.geometry("1920x1080")
        manager_window.title("Manager Window")
        manager_window['bg']='peach puff'
        





#datatype declaration for deposit part---------------------------------------------------
        self.depositmoney=StringVar()
        self.accnum=StringVar()
        self.accname=StringVar()
        self.acc_amount=IntVar()
#End.......................................................................................
# 
# datatype declaration for withdrawal part------------------------------------------------
        self.Account_No_withdrawal=IntVar()
        self.Account_withdrawal_name=StringVar()
        self.Accoount_withdrawal=IntVar()
        self.Account_withdrawal_type=StringVar()
#End........................................................................................
#
#datatype declaraton for tranfer Amount part-----------------------------------------------

        self.Account_num_withdrawal_transfer=IntVar()
        self.Account_num_diposit_transfer=IntVar()
        self.Account_amount_transfer=IntVar()
#End.........................................................................................

#datatype declaration for account balance part..............................................
        self.account_balance=IntVar()
        self.balance=IntVar()





        tk.Frame(manager_window, width=1450, height= 100, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(manager_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        tk.Label(manager_window, text='Manager:', bg='cyan', fg='black', font=('arial', 12, 'bold')).place(x=175, y=75)
        tk.Label(manager_window, text=self.M_name, bg='cyan', fg='black', font=('arial', 12, 'bold')).place(x=250, y=75)
        #tk.Frame(manager_window, width=880, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=8)
        tk.Frame(manager_window, width=1450, height=700, bg="gainsboro", borderwidth=10, relief=SUNKEN).place(x=45, y=120)
        tk.Button(manager_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.add).place(x= 505, y=10)
        tk.Button(manager_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold"), command=objAdd_customer.delete).place(x= 505, y=57)
        tk.Button(manager_window, height=2, text="New Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.Add_user_bank).place(x= 725, y=10)
        tk.Button(manager_window, height=2, text="Delete Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.delete_user_bank).place(x= 725, y=57)
        tk.Button(manager_window, height=2, text="Calculator", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.Calculator_bank).place(x= 945, y=10)
        tk.Button(manager_window, height=2, text="Employee List", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.Employee_list).place(x= 945, y=57)
        tk.Button(manager_window, height=2, text="Login Out", bg="red", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=manager_window.destroy).place(x= 1165, y=57)
        tk.Button(manager_window, height=2, text="Customer Profile", bg="White", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=objAdd_customer.customer_list).place(x= 1165, y=10)
        tk.Button(manager_window, height=5, text="Notice", bg="White", width=11, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=objAdd_customer.notice).place(x= 1380, y=10)

        tk.Frame(manager_window, height=300, width=500, bg="White", borderwidth=3, relief='ridge').place(x=60,y=140)
        tk.Frame(manager_window, height=350, width=500, bg="White", borderwidth=3, relief='ridge').place(x=60,y=450)
        tk.Frame(manager_window, height=300, width=500, bg="White", borderwidth=3, relief='ridge').place(x=580,y=140)
        tk.Frame(manager_window, height=350, width=500, bg="White", borderwidth=3, relief='ridge').place(x=580,y=450)
        tk.Frame(manager_window, height=660, width=390, bg="White", borderwidth=3, relief='sunken').place(x=1090,y=140)
        
        lbs=tk.Label(manager_window, text='Amount Deposit', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=220,y=150)
        lbs=tk.Label(manager_window, text="Account No:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=210)
        self.acc_no=Entry(manager_window, textvariable=self.accnum, width=40)
        self.acc_no.place(x=220,y=210)
        lbs=tk.Label(manager_window, text="Name of holder:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=250)
        self.acc_name=Entry(manager_window, textvariable=self.accname, width=40)
        self.acc_name.place(x=220,y=250)
        lbs=tk.Label(manager_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=290)
        self.amonut=Entry(manager_window, textvariable=self.acc_amount, width=40)
        self.amonut.place(x=220,y=290)
        lbs=tk.Label(manager_window, text="Type:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=340)
        self.degisnation_radio1=Radiobutton(manager_window, text='Cash', variable=self.depositmoney, value="Cash",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=200, y=340)
        self.degisnation_radio1=Radiobutton(manager_window, text='Cheque', variable=self.depositmoney, value="Cheque",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=290, y=340)
        self.degisnation_radio1=Radiobutton(manager_window, text='DD', variable=self.depositmoney, value="DD",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=390, y=340)
        self.reset=tk.Button(manager_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_deposit).place(x=100,y=390)
        self.reset=tk.Button(manager_window, text='Deposit', width=20, bg='Green', fg='white',font=('arail', 10,'bold'), command=self.send_deposit).place(x=300,y=390)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbs=tk.Label(manager_window, text='Amount Withdrawal', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=750,y=150)
        lbs=tk.Label(manager_window, text="Account No:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=210)
        self.acc_no_withdrawal=Entry(manager_window, textvariable=self.Account_No_withdrawal, width=40)
        self.acc_no_withdrawal.place(x=750,y=210)
        lbs=tk.Label(manager_window, text="Name of holder:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=250)
        self.acc_name_withdrawal=Entry(manager_window, textvariable=self.Account_withdrawal_name, width=40)
        self.acc_name_withdrawal.place(x=750,y=250)
        lbs=tk.Label(manager_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=290)
        self.amonut_withdrwal=Entry(manager_window, textvariable=self.Accoount_withdrawal, width=40)
        self.amonut_withdrwal.place(x=750,y=290)
        lbs=tk.Label(manager_window, text="Type:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=340)
        self.With_type_radio1=Radiobutton(manager_window, text='Recipt', variable=self.Account_withdrawal_type, value="Recipt",font=('arial', 12, 'bold'), bg='white')
        self.With_type_radio1.place(x=750, y=340)
        self.With_type_radio1=Radiobutton(manager_window, text='Cheque', variable=self.Account_withdrawal_type, value="Cheque",font=('arial', 12, 'bold'), bg='white')
        self.With_type_radio1.place(x=900, y=340)
        
        self.reset=tk.Button(manager_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_withdrawal).place(x=650,y=390)
        self.reset=tk.Button(manager_window, text='Withdraw', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.send_withdrawal_amt).place(x=850,y=390)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbs=tk.Label(manager_window, text='Transfer Amount', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=220,y=460)
        lbs=tk.Label(manager_window, text="Account No(Tranfer From):", bg='white', font=('arail', 12, 'bold')).place(x=70, y=520)
        self.acc_no_withdrawal_tranfer=Entry(manager_window, textvariable=self.Account_num_withdrawal_transfer, width=40)
        self.acc_no_withdrawal_tranfer.place(x=290,y=520)
        lbs=tk.Label(manager_window, text="Account No(Deposit):", bg='white', font=('arail', 12, 'bold')).place(x=70, y=560)
        self.acc_no_deposit_transfer=Entry(manager_window, textvariable=self.Account_num_diposit_transfer, width=40)
        self.acc_no_deposit_transfer.place(x=290,y=560)
        lbs=tk.Label(manager_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=620)
        self.amonut_transfer=Entry(manager_window, textvariable=self.Account_amount_transfer, width=40)
        self.amonut_transfer.place(x=290,y=620)
        self.reset=tk.Button(manager_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_transfer).place(x=100,y=680)
        self.reset=tk.Button(manager_window, text='Transfer', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.transfer_amt).place(x=300,y=680)
#.........................................................................................................................................................................
        lbs=tk.Label(manager_window, text='Account Balance', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=750,y=460)
        lbs=tk.Label(manager_window, text="Account No:", bg='white', font=('arail', 15, 'bold')).place(x=600, y=520)
        self.balance_account_no=Entry(manager_window, textvariable=self.account_balance,font=('arial', 15, 'bold'),width=20)
        self.balance_account_no.place(x=750,y=520)

        #bal=self.check_balance()
        
        #self.reset=tk.Button(manager_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold')).place(x=100,y=680)
        self.reset=tk.Button(manager_window, text='Check', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.check_balance).place(x=750,y=680)
        
        manager_window.mainloop()


class Employee():
    def reset_deposit(self):

        self.acc_name.delete(0, END)
        self.amonut.delete(0, END)
        self.acc_no.delete(0, END)
        return
    def reset_withdrawal(self):
        self.acc_no_withdrawal.delete(0, END)
        self.acc_name_withdrawal.delete(0, END)
        self.amonut_withdrwal.delete(0, END)
        return
    def reset_transfer(self):
        self.acc_no_withdrawal_tranfer.delete(0, END)
        self.acc_no_deposit_transfer.delete(0, END)
        self.amonut_transfer.delete(0, END)
        return

    def send_deposit(self):
        self.send=obj.deposit_amt(self.acc_no.get(), self.amonut.get())
        self.reset_deposit()
    def send_withdrawal_amt(self):
            self.send=obj.withdrawal_amt(self.acc_no_withdrawal.get(), self.amonut_withdrwal.get())
            if self.send==1:
                    self.reset_withdrawal()
            else:
                    self.messege='Insufficient Amount in Account'
                    messagebox.showinfo('showinfo',self.messege)
                    self.reset_withdrawal()
    def transfer_amt(self):
                obj.transfer_db(self.acc_no_withdrawal_tranfer.get(),self.acc_no_deposit_transfer.get(),self.amonut_transfer.get())
                self.reset_transfer()


    def check_balance(self):
            balance=obj.balance_valid(self.balance_account_no.get())
            #print(balance)
            #return balance
            ff=f'Total Amount in the bank account No:   {self.balance_account_no.get()} is:     {balance}'
            self.messege='Balance in Account'
            messagebox.showinfo('showinfo',ff)
    def Gui(self):

        emp_window=tk.Tk()
        emp_window.geometry("1500x900")
        emp_window.title("Employee Window")
        
#datatype declaration for deposit part---------------------------------------------------
        self.depositmoney=StringVar()
        self.accnum=IntVar()
        self.accname=StringVar()
        self.acc_amount=IntVar()
#End.......................................................................................
# 
# datatype declaration for withdrawal part------------------------------------------------
        self.Account_No_withdrawal=IntVar()
        self.Account_withdrawal_name=StringVar()
        self.Accoount_withdrawal=IntVar()
        self.Account_withdrawal_type=StringVar()
#End........................................................................................
#
#datatype declaraton for tranfer Amount part-----------------------------------------------

        self.Account_num_withdrawal_transfer=IntVar()
        self.Account_num_diposit_transfer=IntVar()
        self.Account_amount_transfer=IntVar()
#End.........................................................................................




#datatype declaration for check balance part--------------------------------------------------

        self.account_balance=StringVar()





        tk.Frame(emp_window, width=1450, height= 100, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(emp_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        tk.Label(emp_window, text='Employee', bg='cyan', fg='black', font=('arial', 12, 'bold')).place(x=175, y=75)
        #tk.Frame(emp_window, width=880, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=8)
        tk.Frame(emp_window, width=1450, height=700, bg="gainsboro", borderwidth=10, relief=SUNKEN).place(x=45, y=120)
        tk.Button(emp_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.add).place(x= 505, y=10)
        tk.Button(emp_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold"), command=objAdd_customer.delete).place(x= 505, y=57)
        tk.Button(emp_window, height=2, text="New Employee", bg="white", width=25, state=DISABLED,borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.Add_user_bank).place(x= 725, y=10)
        tk.Button(emp_window, height=2, text="Delete Employee", bg="white", width=25,state=DISABLED, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.delete_user_bank).place(x= 725, y=57)
        tk.Button(emp_window, height=2, text="Calculator", bg="white", width=25,  borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=10)
        tk.Button(emp_window, height=2, text="Attendance", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.Calculator_bank).place(x= 945, y=57)
        tk.Button(emp_window, height=2, text="Login Out", bg="red", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=emp_window.destroy).place(x= 1165, y=57)
        tk.Button(emp_window, height=2, text="Customer Profile", bg="White", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=objAdd_customer.customer_list).place(x= 1165, y=10)
        tk.Button(emp_window, height=5, text="Notice", bg="White", width=11, borderwidth=2, state=DISABLED, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold")).place(x= 1380, y=10)

        tk.Frame(emp_window, height=300, width=500, bg="White", borderwidth=3, relief='ridge').place(x=60,y=140)
        tk.Frame(emp_window, height=350, width=500, bg="White", borderwidth=3, relief='ridge').place(x=60,y=450)
        tk.Frame(emp_window, height=300, width=500, bg="White", borderwidth=3, relief='ridge').place(x=580,y=140)
        tk.Frame(emp_window, height=350, width=500, bg="White", borderwidth=3, relief='ridge').place(x=580,y=450)
        tk.Frame(emp_window, height=660, width=390, bg="White", borderwidth=3, relief='sunken').place(x=1090,y=140)
        
        lbs=tk.Label(emp_window, text='Amount Deposit', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=220,y=150)
        lbs=tk.Label(emp_window, text="Account No:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=210)
        self.acc_no=Entry(emp_window, textvariable=self.accnum, width=40)
        self.acc_no.place(x=220,y=210)
        lbs=tk.Label(emp_window, text="Name of holder:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=250)
        self.acc_name=Entry(emp_window, textvariable=self.accname, width=40)
        self.acc_name.place(x=220,y=250)
        lbs=tk.Label(emp_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=290)
        self.amonut=Entry(emp_window, textvariable=self.acc_amount, width=40)
        self.amonut.place(x=220,y=290)
        lbs=tk.Label(emp_window, text="Type:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=340)
        self.degisnation_radio1=Radiobutton(emp_window, text='Cash', variable=self.depositmoney, value="Cash",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=200, y=340)
        self.degisnation_radio1=Radiobutton(emp_window, text='Cheque', variable=self.depositmoney, value="Cheque",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=290, y=340)
        self.degisnation_radio1=Radiobutton(emp_window, text='DD', variable=self.depositmoney, value="DD",font=('arial', 12, 'bold'), bg='white')
        self.degisnation_radio1.place(x=390, y=340)
        self.reset=tk.Button(emp_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_deposit).place(x=100,y=390)
        self.reset=tk.Button(emp_window, text='Deposit', width=20, bg='Green', fg='white',font=('arail', 10,'bold'), command=self.send_deposit).place(x=300,y=390)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbs=tk.Label(emp_window, text='Amount Withdrawal', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=650,y=150)
        lbs=tk.Label(emp_window, text="Account No:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=210)
        self.acc_no_withdrawal=Entry(emp_window, textvariable=self.Account_No_withdrawal, width=40)
        self.acc_no_withdrawal.place(x=750,y=210)
        lbs=tk.Label(emp_window, text="Name of holder:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=250)
        self.acc_name_withdrawal=Entry(emp_window, textvariable=self.Account_withdrawal_name, width=40)
        self.acc_name_withdrawal.place(x=750,y=250)
        lbs=tk.Label(emp_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=290)
        self.amonut_withdrwal=Entry(emp_window, textvariable=self.Accoount_withdrawal, width=40)
        self.amonut_withdrwal.place(x=750,y=290)
        lbs=tk.Label(emp_window, text="Type:", bg='white', font=('arail', 12, 'bold')).place(x=600, y=340)
        self.With_type_radio1=Radiobutton(emp_window, text='Recipt', variable=self.Account_withdrawal_type, value="Recipt",font=('arial', 12, 'bold'), bg='white')
        self.With_type_radio1.place(x=750, y=340)
        self.With_type_radio1=Radiobutton(emp_window, text='Cheque', variable=self.Account_withdrawal_type, value="Cheque",font=('arial', 12, 'bold'), bg='white')
        self.With_type_radio1.place(x=900, y=340)
        
        self.reset=tk.Button(emp_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_withdrawal).place(x=650,y=390)
        self.reset=tk.Button(emp_window, text='Withdraw', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.send_withdrawal_amt).place(x=850,y=390)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbs=tk.Label(emp_window, text='Transfer Amount', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=220,y=460)
        lbs=tk.Label(emp_window, text="Account No(Tranfer From):", bg='white', font=('arail', 12, 'bold')).place(x=70, y=520)
        self.acc_no_withdrawal_tranfer=Entry(emp_window, textvariable=self.Account_num_withdrawal_transfer, width=40)
        self.acc_no_withdrawal_tranfer.place(x=290,y=520)
        lbs=tk.Label(emp_window, text="Account No(Deposit):", bg='white', font=('arail', 12, 'bold')).place(x=70, y=560)
        self.acc_no_deposit_transfer=Entry(emp_window, textvariable=self.Account_num_diposit_transfer, width=40)
        self.acc_no_deposit_transfer.place(x=290,y=560)
        lbs=tk.Label(emp_window, text="Amount:", bg='white', font=('arail', 12, 'bold')).place(x=70, y=620)
        self.amonut_transfer=Entry(emp_window, textvariable=self.Account_amount_transfer, width=40)
        self.amonut_transfer.place(x=290,y=620)
        self.reset=tk.Button(emp_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold'), command=self.reset_transfer).place(x=100,y=680)
        self.reset=tk.Button(emp_window, text='Transfer', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.transfer_amt).place(x=300,y=680)

        lbs=tk.Label(emp_window, text='Account Balance', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=750,y=460)
        lbs=tk.Label(emp_window, text="Account No:", bg='white', font=('arail', 15, 'bold')).place(x=600, y=520)
        self.balance_account_no=Entry(emp_window, textvariable=self.account_balance,font=('arial', 15, 'bold'),width=20)
        self.balance_account_no.place(x=750,y=520)

        #bal=self.check_balance()
        
        #self.reset=tk.Button(manager_window, text='Reset', width=20, bg='red', fg='white',font=('arail', 10,'bold')).place(x=100,y=680)
        self.reset=tk.Button(emp_window, text='Check', width=20, bg='Green', fg='white',font=('arail', 10,'bold'),command=self.check_balance).place(x=750,y=680)

        emp_window.mainloop()
    
#obj1=Manager()
#obj1.Gui()

  