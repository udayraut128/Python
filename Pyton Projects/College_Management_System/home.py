print("\t\t\t\t\t\tCOLLEGE MANAGEMENT SYSTEM")
#from email import message
from logging import root
from tkinter import *
from tkinter import ttk
from admin import college_admin
from teacher import college_faculty 
from student import college_student                   
import time,datetime 
from tkinter import messagebox
from typing import Counter 
from PIL import ImageTk,Image

print("***********************************************************************************************************************")
class college:
    def __init__(self,root):
        self.root=root
        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.root.title("\t\t\t\t\t\tCOLLEGE MANAGEMENT SYSTEM")
        self.root.geometry("1400x700+1+1")
        
        #creating background photo
        self.img = ImageTk.PhotoImage(file='Collage_background.jpg')
        self.label=Label(self.root,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)

        lable_title=Label(self.root,bd=20,relief=RIDGE,text="COLLEGE MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",40,"bold"))
        lable_title.pack(side=TOP,fill=X)

        #***********************************creating buttons**************************************
        Left_Dataframe=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        self.Left_image=ImageTk.PhotoImage(file="Admin.png")
        Button(root, text="creating login window", image=self.Left_image,command = self.login).place(x=120,y=270,width=260,height=260)
        Left_Dataframe.place(x=100,y=250,width=300,height=300)

        Middle_Dataframe=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        self.Middle_image=ImageTk.PhotoImage(file="teachr.jpeg")
        Button(root, text="creating login window", image=self.Middle_image,command = self.login).place(x=620,y=270,width=260,height=260)
        Middle_Dataframe.place(x=600,y=250,width=300,height=300)

        Right_Dataframe=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        self.Right_image=ImageTk.PhotoImage(file="student.jpeg")
        Button(root, text="creating login window", image=self.Right_image,command = self.login).place(x=1120,y=270,width=260,height=260)
        Right_Dataframe.place(x=1100,y=250,width=300,height=300)

    def login(self):
        #global login_screen
        login_screen = Toplevel(self.root)
        #Setting title of screen
        login_screen.title("Login Form")
        #setting height and width of screen
        login_screen.geometry("500x400")
        #Creating layout of login form
        Label(login_screen,width="300", text="Please enter details below",font=5, bg="orange",fg="white").pack()
        #Username Labe
        Label(login_screen, text="Username * ",font=3).place(x=50,y=100)
        #Username textbox
        Entry(login_screen, textvariable=self.username,font=4).place(x=190,y=98)
        #Password Label
    
        
        #Password textbox
        Entry(login_screen, textvariable=self.password ,show="*",font=4).place(x=190,y=169)
        #Label for displaying login status[success/failed]
        Label(login_screen, text="",textvariable=self.message,font=3).place(x=105,y=210)
        #Login button
        Button(login_screen, text="Login", width=10, height=1, bg="orange",command=self.check_login,font=3).place(x=135,y=250)

    def check_login(self):
        if self.username.get()=='' or self.password.get()=='':
            self.message.set("fill the empty field!!!")
            #messagebox.showerror("fill the empty field!!!")
        else:
            if self.username.get()=="@" and self.password.get()=="2":
                self.message.set("Login success")
                self.goto_admin_portal()
                
            elif self.username.get()=="#" and self.password.get()=="2":
                self.message.set("Login success")
                self.goto_faculty_portal()

            elif self.username.get()=="$" and self.password.get()=="2":
                self.message.set("Login success")
                self.goto_student_portal()
                
                #messagebox.showinfo("Login success","Welcome to admin portal")
            else:
                self.message.set("Wrong username or password!!!")
                #messagebox.showerror("Wrong username or password!!!")

    def goto_admin_portal(self):
        self.admin=Toplevel(self.root)
        self.root1=college_admin(self.admin)
        #self.exit()

    def goto_faculty_portal(self):
        print("This is faculty")
        self.faculty=Toplevel(self.root)
        self.root2=college_faculty(self.faculty)

    def goto_student_portal(self):
        print("This is faculty")
        self.student=Toplevel(self.root)
        self.root3=college_student(self.student)
    
    def exit(self):
        exit=messagebox.askyesno("Admin Portal","Confirm you want to exit!!")
        print(exit)
        if exit>0:
            root.quit()
            return  


if __name__=="__main__":
    root=Tk()
    obj=college(root)
    root.mainloop()
