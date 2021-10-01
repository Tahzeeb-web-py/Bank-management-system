import tkinter as tk
from tkinter import *



class Account():
        def add(self):
                addNew_customer=tk.Tk()
                addNew_customer.geometry("950x530+100+100")
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
                D=tk.StringVar(addNew_customer)
                M=tk.StringVar(addNew_customer)
                Y=tk.StringVar(addNew_customer)
                var_alternative_num=StringVar()
                var_gender=StringVar()
                var_address=StringVar()
                var_city=StringVar()
                var_zip_code=IntVar()
                var_Deposit=IntVar()
                heading_frame=Frame(addNew_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(addNew_customer, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(addNew_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)

                label_firstname=Label(addNew_customer, text='New Account Opening',bg="White",font=('arail', 20, 'bold')).place(x=330, y=30)
                label_firstname=Label(addNew_customer, text='First Name',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                FirstName=Entry(addNew_customer, textvariable=Var_first_name, width=35)
                FirstName.place(x=220, y=130)
                label_firstname=Label(addNew_customer, text='Last Name',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                LastName=Entry(addNew_customer, textvariable=var_last_name, width=35)
                LastName.place(x=220, y=170)
                label_firstname=Label(addNew_customer, text="Father's Name",font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                FatherName=Entry(addNew_customer, textvariable=var_father_name, width=35)
                FatherName.place(x=220, y=210)
                label_firstname=Label(addNew_customer, text="Mothet's Name",font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                MotherName=Entry(addNew_customer, textvariable=var_mother_name, width=35)
                MotherName.place(x=220, y=250)
                label_firstname=Label(addNew_customer, text='Contact No.',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                Contactnum=Entry(addNew_customer, textvariable=var_contact_num, width=35)
                Contactnum.place(x=220, y=290)
                label_firstname=Label(addNew_customer, text='Aadhar Card No',font=('arail', 12, 'bold'), bg='White').place(x=70, y=330)
                Aadharnum=Entry(addNew_customer, textvariable=var_aadhar_num, width=35)
                Aadharnum.place(x=220, y=330)
                label_firstname=Label(addNew_customer, text='Pan Card',font=('arail', 12, 'bold'), bg='White').place(x=70, y=370)
                Pan=Entry(addNew_customer, textvariable=var_pan_num, width=35)
                Pan.place(x=220, y=370)
                label_firstname=Label(addNew_customer, text='Date of Birth',font=('arail', 12, 'bold'), bg='White').place(x=70, y=410)
                dates = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
                Months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
                Year = ['1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001',
                '2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020' ];


                droplist= OptionMenu(addNew_customer, D, *dates)
                droplist.config(width=7)
                D.set("Date") 
                droplist.place(x=220,y=400)
                droplist= OptionMenu(addNew_customer, M, *Months)
                droplist.config(width=7)
                M.set("Month") 
                droplist.place(x=300,y=400)
                droplist= OptionMenu(addNew_customer, Y, *Year)
                droplist.config(width=7)
                Y.set("Year") 
                droplist.place(x=380,y=400)


                label_firstname=Label(addNew_customer, text='Alternative No',font=('arail', 12, 'bold'), bg='White').place(x=500, y=290)
                Alternativenum=Entry(addNew_customer, textvariable=var_alternative_num, width=35)
                Alternativenum.place(x=650, y=290)
                label_firstname=Label(addNew_customer, text='Gender',font=('arail', 12, 'bold'), bg='White').place(x=500, y=250)
                label_firstname=Label(addNew_customer, text='Address',font=('arail', 12, 'bold'), bg='White').place(x=500, y=130)
                Address=Entry(addNew_customer, textvariable=var_address, width=35)
                Address.place(x=650, y=130)
                label_firstname=Label(addNew_customer, text='City',font=('arail', 12, 'bold'), bg='White').place(x=500, y=170)
                City=Entry(addNew_customer, textvariable=var_city, width=35)
                City.place(x=650, y=170)
                label_firstname=Label(addNew_customer, text='Zip Code',font=('arail', 12, 'bold'), bg='White').place(x=500, y=210)
                Zipcode=Entry(addNew_customer, textvariable=var_zip_code, width=35)
                Zipcode.place(x=650, y=210)
                label_firstname=Label(addNew_customer, text='Opening Deposit',font=('arail', 12, 'bold'), bg='White').place(x=500, y=330)
                Zipcode=Entry(addNew_customer, textvariable=var_Deposit, width=35)
                Zipcode.place(x=650, y=330)

                exit_button_addcustomer=Button(addNew_customer, text='Exit', bg='red', fg='Black', width=15,command=addNew_customer.destroy,font=('arail', 12, 'bold'))
                exit_button_addcustomer.place(x=380, y=470)
                reset_button_addcustomer=Button(addNew_customer, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_addcustomer.place(x=100, y=470)
                Save_button_addcustomer=Button(addNew_customer, text='Add', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'))
                Save_button_addcustomer.place(x=680, y=470)
                addNew_customer.resizable(False, False)


                addNew_customer.mainloop()

                
        def delete(self):
                dele_customer=tk.Tk()
                dele_customer.geometry("950x530+100+100")
                dele_customer.title("Delete Customer Window")
                dele_customer['bg']='grey'
                heading_frame=Frame(dele_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame(dele_customer, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame(dele_customer, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(dele_customer, text='Close Account',bg="White",font=('arail', 20, 'bold')).place(x=350, y=30)
                label_firstname=Label(dele_customer, text='Name of Account Holder:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                FirstName=Entry(dele_customer, width=35)
                FirstName.place(x=300, y=130)
                label_firstname=Label(dele_customer, text='Account Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                FirstName=Entry(dele_customer, width=35)
                FirstName.place(x=300, y=170)
                label_firstname=Label(dele_customer, text='Mobile Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                FirstName=Entry(dele_customer, width=35)
                FirstName.place(x=300, y=210)
                label_firstname=Label(dele_customer, text='Date of closing:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)


                label_firstname=Label(dele_customer, text='Remark:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                FirstName=Entry(dele_customer, width=35)
                FirstName.place(x=300, y=290)

                label_firstname=Label(dele_customer, text='Verify by:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=340)


                
                exit_button_delecustomer=Button(dele_customer, text='Exit', bg='red', fg='Black', width=15,command=dele_customer.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=380, y=470)
                reset_button_delecustomer=Button(dele_customer, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_delecustomer.place(x=100, y=470)
                Delete_button_delecustomer=Button(dele_customer, text='Close Account', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'))
                Delete_button_delecustomer.place(x=680, y=470)
                dele_customer.resizable(False, False)
                dele_customer.mainloop()

        def Add_user_bank(self):
                add_user=tk.Tk()
                add_user.geometry("950x530+100+100")
                add_user.title("Add Employee Window")
                add_user['bg']='grey'
                add_Empname=StringVar()
                add_username=StringVar()
                add_mobile=StringVar()
                add_password=StringVar()
                add_post=StringVar()
                add_varify=StringVar()

                heading_frame=Frame(add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame( add_user, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame( add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(add_user, text='Add Bank Employee',bg="White",font=('arail', 20, 'bold')).place(x=350, y=30)
                label_firstname=Label(add_user, text='Name of Employee:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=130)
                FirstName=Entry(add_user, width=35)
                FirstName.place(x=300, y=130)
                label_firstname=Label(add_user, text='Username:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                addusername=Entry(add_user,textvariable=add_username, width=35)
                addusername.place(x=300, y=170)
                label_firstname=Label(add_user, text='Mobile Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                addmobile=Entry(add_user,textvariable=add_mobile, width=35)
                addmobile.place(x=300, y=250)
                label_firstname=Label(add_user, text='Password:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                addpassword=Entry(add_user,textvariable=add_password, width=35)
                addpassword.place(x=300, y=210)

                label_firstname=Label(add_user, text='Post:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=290)
                select_post=Radiobutton(add_user, text='Manager', variable=add_post, bg='White',value=1)
                select_post.place(x=300, y=290)
                select_post=Radiobutton(add_user, text='Employee', variable=add_post,bg='White', value=2)
                select_post.place(x=420, y=290)

                label_firstname=Label(add_user, text='Verify by:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=340)
                select_varification=Radiobutton(add_user, text='Manager', variable=add_varify, bg='White',value=1)
                select_varification.place(x=300, y=340)
                

                
                exit_button_delecustomer=Button(add_user, text='Exit', bg='red', fg='Black', width=15,command=add_user.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=380, y=470)
                reset_button_delecustomer=Button(add_user, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_delecustomer.place(x=100, y=470)
                Delete_button_delecustomer=Button(add_user, text='Close Account', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'))
                Delete_button_delecustomer.place(x=680, y=470)
                add_user.resizable(False, False)
                add_user.mainloop()

        def delete_user_bank(self):
                add_user=tk.Tk()
                add_user.geometry("950x530+100+100")
                add_user.title("Delete Employee Window")
                add_user['bg']='grey'
                del_username=StringVar()
                del_password=StringVar()
                del_mobile=StringVar()
                heading_frame=Frame(add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=10)
                middle_frame=Frame( add_user, width=850, height=350, bg='White', relief=RIDGE).place(x=50, y=90)
                futter_frame=Frame( add_user, width=850, height=70, bg='White', relief=RIDGE).place(x=50, y=450)
                label_firstname=Label(add_user, text='Delete Bank Employee',bg="White",font=('arail', 20, 'bold')).place(x=350, y=30)
                label_firstname=Label(add_user, text='Username:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=170)
                delusername=Entry(add_user, textvariable=del_username,width=35)
                delusername.place(x=300, y=170)
                label_firstname=Label(add_user, text='Mobile Number:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=250)
                Delmobile=Entry(add_user,textvariable=del_mobile, width=35)
                Delmobile.place(x=300, y=250)
                label_firstname=Label(add_user, text='Password:',font=('arail', 12, 'bold'), bg='White').place(x=70, y=210)
                delpassword=Entry(add_user,textvariable=del_mobile,width=35)
                delpassword.place(x=300, y=210)
                exit_button_delecustomer=Button(add_user, text='Exit', bg='red', fg='Black', width=15,command=add_user.destroy,font=('arail', 12, 'bold'))
                exit_button_delecustomer.place(x=380, y=470)
                reset_button_delecustomer=Button(add_user, text='Reset', bg='yellow', fg='Black',width=15, font=('arail', 12, 'bold'))
                reset_button_delecustomer.place(x=100, y=470)
                Delete_button_delecustomer=Button(add_user, text='Delete Employee', bg='Green', fg='White', width=15,font=('arail', 12, 'bold'))
                Delete_button_delecustomer.place(x=680, y=470)
                add_user.resizable(False, False)
                add_user.mainloop()


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




    def Gui(self):

        manager_window=tk.Tk()
        manager_window.geometry("1920x1080")
        manager_window.title("Manager Window")
        manager_window['bg']='peach puff'





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





        tk.Frame(manager_window, width=1450, height= 100, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(manager_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        #tk.Frame(manager_window, width=880, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=8)
        tk.Frame(manager_window, width=1450, height=700, bg="gainsboro", borderwidth=10, relief=SUNKEN).place(x=45, y=120)
        tk.Button(manager_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.add).place(x= 505, y=10)
        tk.Button(manager_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold"), command=objAdd_customer.delete).place(x= 505, y=57)
        tk.Button(manager_window, height=2, text="New Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.Add_user_bank).place(x= 725, y=10)
        tk.Button(manager_window, height=2, text="Delete Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.delete_user_bank).place(x= 725, y=57)
        tk.Button(manager_window, height=2, text="Updata Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=10)
        tk.Button(manager_window, height=2, text="Attendance", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=57)
        tk.Button(manager_window, height=2, text="Login Out", bg="red", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=manager_window.destroy).place(x= 1165, y=57)
        tk.Button(manager_window, height=2, text="Customer Profile", bg="White", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold")).place(x= 1165, y=10)
        tk.Button(manager_window, height=5, text="Notice", bg="White", width=11, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold")).place(x= 1380, y=10)

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
        self.reset=tk.Button(manager_window, text='Deposit', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=300,y=390)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbs=tk.Label(manager_window, text='Amount Withdrawal', bg='black',fg='white',font=('Helvetica' ,15, 'bold italic')).place(x=650,y=150)
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
        self.reset=tk.Button(manager_window, text='Withdraw', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=850,y=390)
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
        self.reset=tk.Button(manager_window, text='Transfer', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=300,y=680)

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





        tk.Frame(emp_window, width=1450, height= 100, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(emp_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        #tk.Frame(emp_window, width=880, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=8)
        tk.Frame(emp_window, width=1450, height=700, bg="gainsboro", borderwidth=10, relief=SUNKEN).place(x=45, y=120)
        tk.Button(emp_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"), command=objAdd_customer.add).place(x= 505, y=10)
        tk.Button(emp_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold"), command=objAdd_customer.delete).place(x= 505, y=57)
        tk.Button(emp_window, height=2, text="New Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.Add_user_bank).place(x= 725, y=10)
        tk.Button(emp_window, height=2, text="Delete Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold"),command=objAdd_customer.delete_user_bank).place(x= 725, y=57)
        tk.Button(emp_window, height=2, text="Updata Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=10)
        tk.Button(emp_window, height=2, text="Attendance", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=57)
        tk.Button(emp_window, height=2, text="Login Out", bg="red", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold"), command=emp_window.destroy).place(x= 1165, y=57)
        tk.Button(emp_window, height=2, text="Customer Profile", bg="White", width=25, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold")).place(x= 1165, y=10)
        tk.Button(emp_window, height=5, text="Notice", bg="White", width=11, borderwidth=2, fg="Black", activebackground="black", activeforeground="White",font=("arial", 10, "bold")).place(x= 1380, y=10)

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
        self.reset=tk.Button(emp_window, text='Deposit', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=300,y=390)
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
        self.reset=tk.Button(emp_window, text='Withdraw', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=850,y=390)
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
        self.reset=tk.Button(emp_window, text='Transfer', width=20, bg='Green', fg='white',font=('arail', 10,'bold')).place(x=300,y=680)

        emp_window.mainloop()
    
obj1=Manager()
obj1.Gui()

  