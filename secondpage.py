from tkinter import *
import sys
sys.path.append("..")
from firstpage import *
from databasehelper import *
from sentiment import *
#from PycharmProjects.college_project.firstpage import *
#from PycharmProjects.basic.databasehelper import *
from PIL import ImageTk,Image
from tkinter import messagebox

class SecondPage(FirstPage):
    def __init__(self,root):
        super().__init__(root)
        self.add_widgets()
        #self.user_info()
    def user_info(self):
        username=self.e1.get()
        UserPhonemodel=self.e4.get()
        userEmail=self.e3.get()
        userContact=self.e2.get()
        #sentiment=self.senti.get()
        c= self.e7.get()
        #senti=sentiment_scores(result)
        query ="Select * from User1 where UserName='%s' and UserModelNo ='%s'"
        #query2="INSERT INTO User1 (UserName,UserContact,UserEmailId,UserModelNo,UserSentiment)";
        query2="Insert into User2(UserName,UserContact,UserEmailId,UserModelNo,UserSenti)Values('%s','%s','%s','%s','%s')"
        args=(username,UserPhonemodel,userEmail,userContact,c)
        params = (username,UserPhonemodel)
        #params1 = (username,UserPhonemodel,userContact,userEmail)
        result2 = DataBaseHelper.get_all_data(query, params)
        DataBaseHelper.execute_query(query2 %args)
        #DataBaseHelper.execute_all_data_multiple_input(query2,params1)
        #result3 = Insert into user1 where(
        #result3 = DataBaseHelper.execute_query(query,params)
        #result3=DataBaseHelper.execute_all_data_multiple_input(query,params)
        print(result2)
        print(username)
        print(UserPhonemodel)
    def get_screen(self):
        new_window=Toplevel()
        f = Frame(new_window, height=800, width=800)
        self.img1 = ImageTk.PhotoImage(Image.open("sentiment2.png"))
        self.panel = Label(f, image=self.img1)
        self.panel.pack()
        self.m = Message(f, width=600, font="Roman 20 bold italic",
                            text="Leave the feedback", bg="white", relief=SOLID
                            , borderwidth=2)
        self.m.place(x=20,y=50)
        l7 = Label(f, width=20, text="Comment")
        self.e7 = Entry(f, width=30, fg='black', bg='white')
        self.e7.place(x=180,y=150)
        self.e7.focus_set()
        l7.place(x=20,y=150)

        b3 = Button(f, text='Next', height=2, width=20,command = lambda : self.limit(new_window))
        b3.place(x=50,y=450)
        #b5 = Button(f, text='Admin page', height=2, width=10, command=lambda: self.user_info())
        #b5.place(x=300, y=450)

        f.pack()
        self.panel.pack_propagate(0)
        f.pack_propagate(0)
    def calculate(self,result):
        senti=sentiment_scores(result)
        if(senti>0):
            my_message="results : the overall sentiment is positive"
            messagebox.showinfo('Success',my_message)
        elif(senti==0):
            my_message="results : the overall sentiment is neutral"
            messagebox.showinfo('Success',my_message)
        else:
            my_message="results : overall sentiment is negative"
            messagebox.showinfo('Success',my_message)
    def limit(self,new_window):
        c= self.e7.get()
        result=c
        #new_window1=Toplevel()
        #f1=Frame(new_window1,height=600,width=700)
        b4=Button(new_window,text='Calculate the sentiment',height=2,width=20,command=lambda :self.calculate(result))
        b4.place(x=250,y=550)
        #f.pack()
        #messagebox.showinfo("valid entry", "click ok to check attendance")


    def add_widgets(self):
        l1 = Label(self.f, width=20, text="Name: ")
        self.e1 = Entry(self.f, width=30, fg='black', bg='white')
        l2 = Label(self.f, width=20, text="Contact: ")
        self.e2 = Entry(self.f, width=30, fg='black', bg='white')
        l3 = Label(self.f, width=20, text="EmailId: ")
        self.e3 = Entry(self.f, width=30, fg='black', bg='white')
        l4 = Label(self.f, width=20, text="Phone model number: ")
        self.e4 = Entry(self.f, width=30, fg='black', bg='white')
        self.e1.focus_set()
        l1.grid(row=1, column=1, padx=20, pady=20)
        l2.grid(row=2, column=1, padx=20, pady=20)
        l3.grid(row=3, column=1, padx=20, pady=20)
        l4.grid(row=4, column=1, padx=20, pady=20)
        self.e1.grid(row=1, column=2, padx=20, pady=20)
        self.e2.grid(row=2, column=2, padx=20, pady=20)
        self.e3.grid(row=3, column=2, padx=20, pady=20)
        self.e4.grid(row=4, column=2, padx=20, pady=20)
        b1 = Button(self.f, text='Next', height=2, width=10,command=lambda :self.get_screen())
        b1.place(x=100,y=270)
        b2 = Button(self.f, text='Reset', height=2, width=10,command=lambda: self.reset())
        b2.place(x=200, y=270)
        b5 = Button(self.f, text='Admin page', height=2, width=10, command=lambda: self.user_info())
        b5.place(x=300, y=270)
        #self.user_info()
        self.f.pack()
        self.f.grid_propagate(0)
    # def submit(self,val1,val2):
    #     a=val1.get()
    #     b=val2.get()
    #     print(a,b)
    def reset(self):
        self.e1.delete(0,END)
        self.e3.delete(0,END)
root=Tk()
m=SecondPage(root)
root.mainloop()
