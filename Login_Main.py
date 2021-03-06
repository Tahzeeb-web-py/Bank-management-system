import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Entry
from database import Bank_data
import pymongo
from pymongo import MongoClient 
from designation import Manager
from tkinter import ttk
from designation import Employee
import PIL
from PIL import ImageTk, Image

obj=Bank_data()
obj1=Manager()
obj2=Employee()


class Login_Form(Tk):



    def Developer(self):
            dev_win=tk.Toplevel()
            dev_win.geometry("800x600")
            dev_win.title("Bank Management system developer")
            dev_win['bg']='grey'
            image1 = Image.open("developeer.png")
            
            resize_image=image1.resize((790,545), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize_image)
            panel=tk.Label(dev_win,image=test)
            panel.image=test
            panel.place(x=5,y=5)
            
            develop_exit_button=Button(dev_win, text="Exit", bg="red", fg="White", font=("arial", 15, 'bold'), command=dev_win.destroy).place(x=380, y=550)
            dev_win.mainloop()

    def Help_user(self):
        self.help_win=tk.Tk()
        self.help_win.geometry("800x2400")
        self.help_win.title('Help window')
        self.help_win.mainloop()

    def reset(self):

        self.entry_username.delete(0,END)
        self.entry_password.delete(0, END)
        return
   
    def fetch_all(self):
        self.get_post=self.post.get()
        self.user=self.entry_username.get()
        self.get_pass=self.entry_password.get()
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["bank_management_system_2021"]#database name
        Collection = db["Login_post"]#collection name
        result = Collection.find_one({"post":self.get_post,
                                      "Username":self.user,
                                      "Password":self.get_pass},{"_id":0, "Name":0, "Contact No":0})
        x={'Username': self.user, 'Password': self.get_pass, 'post':self.get_post}
      
        if(x==result):
            if(self.get_post=='Manager'):
                
                obj1.Gui()
               
                
                
                
            elif(self.get_post=="Employee"):
                obj2.Gui()
               
        else:
            messagebox.showinfo("warning", "Your Entered Details are Wrong \n Please Enter correct Details")
        
        
        
       


        
        
        



    def __init__(self):


        note=obj.fetch_notice()
        #main frame code
        logwin=tk.Tk()
        logwin.geometry("1400x800")
        logwin.title("Bank of Nagpur")
        toptitleframe=Frame(logwin, width=1150, height=100, bg="White", borderwidth=10,relief="ridge").place(x=200, y=25)
        bank_name_Label=Label(logwin, text="Bank of Nagpur. PVT, LTD", bg="white", fg="Black", font=('arial', 40, 'bold')).place(x=250, y=45)
        bank_enquire_details_contact=Label(logwin, text='Contact no: 5569933', fg="black", bg="white", font=("arial", 10, 'bold')).place(x=950,y=45)
        bank_enquire_details_website=Label(logwin, text='Website: www.bankofngp.in', fg="black", bg="white", font=("arial", 10, 'bold')).place(x=950,y=75)
        Developer_button=Button(logwin, text="<--Develop-->", width=20,bg="yellow", height=1, command=self.Developer)
        
        Developer_button.place(x=1180, y=45)
        Help_button=Button(logwin, text="Help", width=20, height=1, bg="light green", command=self.Help_user).place(x=1180, y=75)


        #LoginForm Frame
        self.post=StringVar()
        username=StringVar()
        password=StringVar()


        login_form_frame=Frame(logwin, width=750, height=600, bg="white", borderwidth=5, relief="sunken").place(x=600, y=150)
        degisnation_label=Label(login_form_frame, text="Degisnation:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=375)
        self.degisnation_radio1=Radiobutton(login_form_frame, text='Manager', variable=self.post, value="Manager",font=('arial', 13, 'bold'), bg='white')
        self.degisnation_radio1.place(x=900, y=375)
        self.degisnation_radio=Radiobutton(login_form_frame, text='Employee', variable=self.post, value="Employee",font=('arial', 13, 'bold'), bg='white')
        self.degisnation_radio.place(x=1050, y=375)

        Username_label=Label(login_form_frame, text="Username:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=425)
        self.entry_username=Entry(login_form_frame, textvariable=username, bg="grey",font=2, width=25)
        self.entry_username.place(x=900,y=425)
        Password_label=Label(login_form_frame, text="Password:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=475)
        self.entry_password=Entry(login_form_frame, textvariable=password, bg="grey",font=2, width=25)
        self.entry_password.place(x=900, y=475)

        login_button=Button(login_form_frame, text="Login", width=20, height=2, bg="light green", font=('arial', 10, 'bold'), command=self.fetch_all).place(x=900, y=650)
        reset_button=Button(login_form_frame, text="Reset", width=20, height=2, bg="red", font=('arial', 10, 'bold'), command=self.reset).place(x=700, y=650)
        exit_button=Button(login_form_frame, text="Exit", width=20, height=2, bg="red", font=('arial', 10, 'bold'), command=logwin.destroy)
        exit_button.place(x=1100, y=650)

        Login_lable=Label(login_form_frame, text='Login Here',bg='white', fg='black', font=('arial', 35, 'bold')).place(x=900,y=230)
        #img
        image1 = Image.open("user.ico")
        resize_image=image1.resize((200,100), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize_image)
        
        label1 =tk.Label(image=test)
        label1.image = test
        label1.place(x=650,y=210)
        

        #NoticeForm Frame
        notice_frame=Frame(logwin, width=500, height=600, borderwidth=5, relief='sunken', bg='White').place(x=50, y=150)
        notice_label=Label(notice_frame,text='Notice', font=('arail', 30, 'bold'), bg='White').place(x=250, y=175)
        note_frame=Frame(logwin, width=450, height=500, borderwidth=3, bg="grey").place(x=75, y=240)
        collabaration_frame=Frame(logwin, width=430, height=120, borderwidth=5, relief='sunken', bg='White').place(x=85, y=600)

        column_notice=('#1')
        self.tree_note=ttk.Treeview(login_form_frame, columns=column_notice,selectmode='none', show='headings', height=16)
        self.tree_note.column('#1',anchor=CENTER, width=430)
        self.tree_note.heading('#1', text='____________________________________________________________________________________')
        self.tree_note.bind('<<TreeviewSelect>>')
        self.tree_note.place(x=85, y=250)
        for x in obj.fetch_notice():
                
                z1=x['notices']
            
                self.tree_note.insert("",tk.END, value=[z1])
        vsb = ttk.Scrollbar(login_form_frame, orient="vertical", command=self.tree_note.yview)
        vsb.place(x=525, y=250)
        self.tree_note.configure(yscrollcommand=vsb.set)
        image1 = Image.open("bank_logo.png")
        resize_image=image1.resize((150,140), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize_image)
        
        label1 = tk.Label(image=test)
        label1.image = test
        
        # Position image
        label1.place(x=40,y=0)

        image1 = Image.open("partner.png")
        resize_image=image1.resize((90,90), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize_image)
        
        label1 = tk.Label(image=test)
        label1.image = test
        
        # Position image
        label1.place(x=120,y=620)

        logwin.mainloop()




        

#if __name__==__main__:
    
start=Login_Form()
#obj=Bank_data()
