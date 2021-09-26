import tkinter as tk
from tkinter import *


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
        tk.Button(manager_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 505, y=10)
        tk.Button(manager_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold")).place(x= 505, y=57)
        tk.Button(manager_window, height=2, text="New Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 725, y=10)
        tk.Button(manager_window, height=2, text="Delete Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 725, y=57)
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
    def Gui(self):


        emp_window=tk.Tk()
        emp_window.geometry("1500x900")
        emp_window.title("Employese Window")
    
        z=tk.Frame(emp_window, width=1570, height=740).place(x=30, y=30)
        tk.Frame(emp_window, width=440, height= 70, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(emp_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        tk.Frame(emp_window, width=955, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=4)
        tk.Frame(emp_window, width=1410, height= 100, bg="peachpuff4", borderwidth=3).place(x=45, y=140)
        
        tk.Button(emp_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 505, y=8)
        tk.Button(emp_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold")).place(x= 505, y=55)
        tk.Button(emp_window, height=2, text="Withdraw", bg="white", width=30, borderwidth=2, fg="black",  activeforeground="White", activebackground="black",font=("arial", 10, "bold")). place(x=50,y=147)
        tk.Button(emp_window, height=2, text="Customer List", bg="white", width=40, borderwidth=2, fg="black", activeforeground="White",state="disabled", activebackground="black", font=("arial", 10, "bold")). place(x=50,y=192)
        tk.Button(emp_window, height=2, text="Transactions", bg="white", width=30, borderwidth=2, fg="black",  activeforeground="White", state="disabled", activebackground="black",font=("arial", 10, "bold")). place(x=551,y=147)
        tk.Button(emp_window, height=2, text="View Balance", bg="white", width=40, borderwidth=2, fg="black",  activeforeground="White", activebackground="black",font=("arial", 10, "bold")). place(x=710,y=192)
        tk.Button(emp_window, height=2, text="Devoloper", bg="white", width=50, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=1040,y=192)
        tk.Button(emp_window, height=2, text="Deposit", bg="white", width=30, borderwidth=2, activeforeground="White", activebackground="black",fg="black", font=("arial", 10, "bold")). place(x=300,y=147)
        tk.Button(emp_window, height=2, text="Profile of Customer", bg="white", width=40, borderwidth=2, fg="black",  activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=380,y=192)
        tk.Button(emp_window, height=2, text="Tranfer Amount", bg="white", width=30, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=801,y=147)
        tk.Button(emp_window, height=2, text="Request", bg="white", width=30, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=1051,y=147)
        tk.Button(emp_window, height=2, text="Login Out", bg="red", width=17, borderwidth=2, fg="White", activeforeground="black", activebackground="white", font=("arial", 10, "bold"), command=emp_window.destroy). place(x=1304,y=147)
        emp_window.mainloop()
    
obj1=Manager()
obj1.Gui()

  