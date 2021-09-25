import tkinter as tk
from tkinter import *


class Deposit():
    def Add_money(self):
        Addmoney_win=tk.Tk()
        Addmoney_win.geometry("2500x500+00+200")
        Addmoney_win.title("Deposit Window")
        Addmoney_win['bg']='white'
        Addmoney_win.resizable(False, False)
        Addmoney_win.mainloop()
addmoneytoacc=Deposit()
addmoneytoacc.Add_money()

class Manager():
    def Gui(self):

        manager_window=tk.Tk()
        manager_window.geometry("1500x900")
        manager_window.title("Manager Window")
        manager_window['bg']='white'

        #z=tk.Frame(manager_window, width=1500, height=740).place(x=00, y=00)
        tk.Frame(manager_window, width=440, height= 100, bg="cyan", borderwidth=3).place(x=45, y=8)
        tk.Label(manager_window, text="BON", bg="cyan", fg="purple", font=('arial', 40, 'bold')).place(x=225, y=9)
        tk.Frame(manager_window, width=955, height= 100, bg="peachpuff4", borderwidth=3).place(x=500, y=4)
        tk.Frame(manager_window, width=1410, height= 100, bg="peachpuff4", borderwidth=3).place(x=45, y=140)
        tk.Frame(manager_window, width=1410, height=550, bg="light green", borderwidth=10, relief=SUNKEN).place(x=45, y=250)
        
        tk.Button(manager_window, height=2, text="New Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 505, y=8)
        tk.Button(manager_window, height=2, text="Close Account", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="blue",font=("arial", 10, "bold")).place(x= 505, y=55)
        tk.Button(manager_window, height=2, text="New Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 725, y=8)
        tk.Button(manager_window, height=2, text="Delete Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 725, y=55)
        tk.Button(manager_window, height=2, text="Updata Employee", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=8)
        tk.Button(manager_window, height=2, text="Attendance", bg="white", width=25, borderwidth=2, fg="black", activebackground="black", activeforeground="deep sky blue",font=("arial", 10, "bold")).place(x= 945, y=55)

        tk.Button(manager_window, height=2, text="Withdraw", bg="white", width=30, borderwidth=2, fg="black",  activeforeground="White", activebackground="black",font=("arial", 10, "bold")). place(x=50,y=147)
        tk.Button(manager_window, height=2, text="Customer List", bg="white", width=40, borderwidth=2, fg="black", activeforeground="White",activebackground="black", font=("arial", 10, "bold")). place(x=50,y=192)
        tk.Button(manager_window, height=2, text="Transactions", bg="white", width=30, borderwidth=2, fg="black",  activeforeground="White", activebackground="black",font=("arial", 10, "bold")). place(x=551,y=147)
        tk.Button(manager_window, height=2, text="View Balance", bg="white", width=40, borderwidth=2, fg="black",  activeforeground="White", activebackground="black",font=("arial", 10, "bold")). place(x=710,y=192)
        tk.Button(manager_window, height=2, text="Devoloper", bg="white", width=50, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=1040,y=192)
        tk.Button(manager_window, height=2, text="Deposit", bg="white", width=30, borderwidth=2, activeforeground="White", activebackground="black",fg="black", font=("arial", 10, "bold"),command=addmoneytoacc.Add_money). place(x=300,y=147)
        tk.Button(manager_window, height=2, text="Profile of Customer", bg="white", width=40, borderwidth=2, fg="black",  activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=380,y=192)
        tk.Button(manager_window, height=2, text="Tranfer Amount", bg="white", width=30, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=801,y=147)
        tk.Button(manager_window, height=2, text="Request", bg="white", width=30, borderwidth=2, fg="black", activeforeground="White", activebackground="black", font=("arial", 10, "bold")). place(x=1051,y=147)
        tk.Button(manager_window, height=2, text="Login Out", bg="red", width=17, borderwidth=2, fg="White", activeforeground="black", activebackground="white", font=("arial", 10, "bold"), command=manager_window.destroy). place(x=1304,y=147)

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
    
#obj1=Manager()
#obj1.Gui()

  