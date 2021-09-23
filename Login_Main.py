import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class Login_Form(Tk):

    def Developer(self):
            dev_win=tk.Tk()
            dev_win.geometry("800x600")
            dev_win.title("Bank Management system developer")
            develop_exit_button=Button(dev_win, text="Exit", bg="red", fg="White", font=("arial", 10, 'bold'), command=dev_win.destroy).place(x=380, y=560)

            dev_win.mainloop()

    def Help_user(self):
        self.help_win=tk.Tk()
        self.help_win.geometry("800x2400")
        self.help_win.title('Help window')
        self.help_win.mainloop()



    def __init__(self):

        #main frame code
        logwin=tk.Tk()
        logwin.geometry("1400x800")
        logwin.title("Bank of Nagpur")
        toptitleframe=Frame(logwin, width=1300, height=100, bg="White", borderwidth=10,relief="ridge").place(x=50, y=25)
        bank_name_Label=Label(logwin, text="Bank of Nagpur. PVT, LTD", bg="white", fg="Black", font=('arial', 40, 'bold')).place(x=250, y=45)
        bank_enquire_details_contact=Label(logwin, text='Contact no: 5569933', fg="black", bg="white", font=("arial", 10, 'bold')).place(x=950,y=45)
        bank_enquire_details_website=Label(logwin, text='Website: www.bankofngp.in', fg="black", bg="white", font=("arial", 10, 'bold')).place(x=950,y=75)
        Developer_button=Button(logwin, text="<--Develop-->", width=20,bg="yellow", height=1)
        Developer_button['command']=self.Developer
        Developer_button.place(x=1180, y=45)
        Help_button=Button(logwin, text="Help", width=20, height=1, bg="light green", command=self.Help_user).place(x=1180, y=75)


        #LoginForm Frame
        post=IntVar()
        
        username=StringVar()
        password=StringVar()


        login_form_frame=Frame(logwin, width=750, height=600, bg="white", borderwidth=5, relief="sunken").place(x=600, y=150)
        degisnation_label=Label(login_form_frame, text="Degisnation:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=375)
        degisnation_radio=Radiobutton(login_form_frame, text='Manager', variable=post, value=1,font=('arial', 13, 'bold'), bg='white').place(x=900, y=375)
        degisnation_radio=Radiobutton(login_form_frame, text='Employee', variable=post, value=2,font=('arial', 13, 'bold'), bg='white').place(x=1050, y=375)

        Username_label=Label(login_form_frame, text="Username:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=425)
        Entry_username=Entry(login_form_frame, textvariable=username, bg="grey",font=2, width=25).place(x=900,y=425)
        Password_label=Label(login_form_frame, text="Password:",font=('arial', 18, 'bold'), bg="white").place(x=700,y=475)
        entry_password=Entry(login_form_frame, textvariable=password, bg="grey",font=2, width=25).place(x=900, y=475)

        login_button=Button(login_form_frame, text="Login", width=20, height=2, bg="light green", font=('arial', 10, 'bold')).place(x=900, y=650)
        reset_button=Button(login_form_frame, text="Reset", width=20, height=2, bg="red", font=('arial', 10, 'bold')).place(x=700, y=650)
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

        logwin.mainloop()




        

#if __name__==__main__:
    
start=Login_Form()