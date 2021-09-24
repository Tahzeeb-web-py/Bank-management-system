import tkinter as tk
from tkinter import *





class Manager():
    def __init__(self):

        manager_window=tk.Tk()
        manager_window.geometry("1400x800")
        manager_window.title("Manager Window")
        manager_window.mainloop()

class Employee():
    def __init__(self):


        emp_window=tk.Tk()
        emp_window.geometry("1400x800")
        emp_window.title("Employese Window")
        emp_window.mainloop()
    
obj1=Employee()
