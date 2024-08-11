from email import message
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector as database
class college_admin:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("\t\t\t\t\t\tADMIN PORTAL")
        self.root1.geometry("1200x800")
        self.id = StringVar()
        self.name = StringVar()
        self.father_name = StringVar()
        self.address = StringVar()
        self.session = StringVar()
        self.dob = StringVar()
        self.photo_id = StringVar()
        self.branch = StringVar()
        self.contact = StringVar()
        self.gender = StringVar()
        

       
        lable_title=Label(self.root1,bd=10,relief=RIDGE,text="ADMIN PORTAL",fg="red",bg="white",font=("times new roman",30,"bold"))
        lable_title.pack(side=TOP,fill=X)

    
        #***********************************Dataframe**************************************
        Dataframe=Frame(self.root1,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=70,width=1500,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,text="Student Information",font=("times new roman",10,"bold"))
        DataframeLeft.place(x=0,y=0,width=945,height=370)
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,text="View",font=("times new roman",10,"bold"))
        DataframeRight.place(x=970,y=0,width=480,height=370)
        #***********************************Dataframe**************************************
        Buttonframe=Frame(self.root1,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=470,width=1500,height=50)
        #***********************************Dataframe**************************************
        Detailsframe=Frame(self.root1,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=520,width=1500,height=280)

        #***********************************LeftDataframe**************************************
        Label_Name=Label(DataframeLeft,text="Admission No :",padx=2,pady=6,font=("aerial",12))
        Label_Name.grid(row=0,column=0)
        Text_Name=Entry(DataframeLeft,textvariable=self.id,width=30,font=("aerial",12))
        Text_Name.grid(row=0,column=1)

        Label_Father_name=Label(DataframeLeft,text="Student Name",padx=2,pady=6,font=("aerial",12))
        Label_Father_name.grid(row=1,column=0)
        Text_Father_name=Entry(DataframeLeft,textvariable=self.name,width=30,font=("aerial",12))
        Text_Father_name.grid(row=1,column=1)

        Label_Patient_Id=Label(DataframeLeft,text="Father Name",padx=2,pady=6,font=("aerial",12))
        Label_Patient_Id.grid(row=2,column=0)
        Text_Patient_Id=Entry(DataframeLeft,textvariable=self.father_name,width=30,font=("aerial",12))
        Text_Patient_Id.grid(row=2,column=1)

        Label_address=Label(DataframeLeft,text="Student Address",padx=2,pady=6,font=("aerial",12))
        Label_address.grid(row=3,column=0)
        Text_address=Entry(DataframeLeft,textvariable=self.address,width=30,font=("aerial",12))
        Text_address.grid(row=3,column=1)

        Label_bp=Label(DataframeLeft,text="Session Name :",padx=2,pady=6,font=("aerial",12))
        Label_bp.grid(row=4,column=0)
        Text_bp=Entry(DataframeLeft,textvariable=self.session,width=30,font=("aerial",12))
        Text_bp.grid(row=4,column=1)

        Label_dob=Label(DataframeLeft,text="Date Of Birth :",padx=2,pady=6,font=("aerial",12))
        Label_dob.grid(row=5,column=0)
        Text_dob=Entry(DataframeLeft,textvariable=self.dob,width=30,font=("aerial",12))
        Text_dob.grid(row=5,column=1)

        Label_Id_No=Label(DataframeLeft,text="AadharCard No :",padx=2,pady=6,font=("aerial",12))
        Label_Id_No.grid(row=6,column=0)
        Text_Id_No=Entry(DataframeLeft,textvariable=self.photo_id,width=30,font=("aerial",12))
        Text_Id_No.grid(row=6,column=1)

        Label_branch=Label(DataframeLeft,text="Program And Branch Name",padx=2,pady=6,font=("aerial",12))
        Label_branch.grid(row=7,column=0,sticky=W)
        Label_branch=ttk.Combobox(DataframeLeft,textvariable=self.branch,state="readonly",width=28,font=("aerial",12))
        Label_branch['value']=("Btech CSE (CSAI)","Btech CSE (CSDS)","Btech CSE (CSIOT)","Btech CSE (CSBS)","Btech CSE (CORE)","B PHARAMA","MBA",)
        Label_branch.grid(row=7,column=1)

        Label_assigned_doctor=Label(DataframeLeft,text="Contact Number",padx=2,pady=6,font=("aerial",12))
        Label_assigned_doctor.grid(row=8,column=0)
        Text_assigned_doctor=Entry(DataframeLeft,textvariable=self.contact,width=30,font=("aerial",12))
        Text_assigned_doctor.grid(row=8,column=1)

        Label_gender=Label(DataframeLeft,text="\tGender",padx=2,pady=6,font=("aerial",12))
        Label_gender.grid(row=9,column=0,sticky=W)
        Label_gender=ttk.Combobox(DataframeLeft,textvariable=self.gender,state="readonly",width=28,font=("aerial",12))
        Label_gender['value']=("Male","Female")
        #Label_gender.current(0)
        Label_gender.grid(row=9,column=1)

        
        self.textView=Text(DataframeRight,font=("aerial",12),width=50,height=18,padx=2,pady=6)
        self.textView.grid(row=0,column=0)


        #***********************************Buttons for Altering**************************************
        Button_prescription=Button(Buttonframe,text="View Data",command=self.view,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_prescription.grid(row=0,padx=15,column=1)

        Button_prescription_data=Button(Buttonframe,text="Adding data",command=self.add_data,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_prescription_data.grid(row=0,padx=4,column=2)

        Button_update=Button(Buttonframe,text="Update",command=self.update,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_update.grid(row=0,padx=10,column=3)

        Button_delete=Button(Buttonframe,text="Delete",command=self.delete,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_delete.grid(row=0,padx=10,column=4)

        Button_clear=Button(Buttonframe,text="Clear",command=self.clear,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_clear.grid(row=0,padx=10,column=5)

        Button_exit=Button(Buttonframe,text="Exit",command=self.exit,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_exit.grid(row=0,padx=10,column=6)

        #***********************************Buttons for Altering**************************************
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.student_table=ttk.Treeview(Detailsframe,column=("Admission No","Student Name","Father Name","Student Address","Session Name",
                                                             "Date of Birth","Photo Id No","Program And Branch Name","Contact Number","Gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)        
        scroll_x=ttk.Scrollbar(command=self.student_table.xview)  
        scroll_y=ttk.Scrollbar(command=self.student_table.yview)      

        self.student_table.heading("Admission No",text="Admission No")  
        self.student_table.heading("Student Name",text="Student Name")  
        self.student_table.heading("Father Name",text="Father Name") 
        self.student_table.heading("Student Address",text="Student Address")  
        self.student_table.heading("Session Name",text="Session Name")  
        self.student_table.heading("Date of Birth",text="Date of Birth")  
        self.student_table.heading("Photo Id No",text="Photo Id No")  
        self.student_table.heading("Program And Branch Name",text="Program And Branch Name") 
        self.student_table.heading("Contact Number",text="Contact Number") 
        self.student_table.heading("Gender",text="Gender")  
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.column("Admission No",width=100)  
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Father Name",width=100)    
        self.student_table.column("Student Address",width=100)  
        self.student_table.column("Session Name",width=100)  
        self.student_table.column("Date of Birth",width=100)  
        self.student_table.column("Photo Id No",width=100)  
        self.student_table.column("Program And Branch Name",width=120)
        self.student_table.column("Contact Number",width=100)   
        self.student_table.column("Gender",width=100)  
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.move_cursor)

        self.display()

         #***********************************Functionality declaration**************************************

    def add_data(self):
        if self.id=="":
            messagebox.showerror("Error","All fields are required")
        else:
            connection=database.connect(host="localhost",user="root",password="12345",database="project")
            my_cursor=connection.cursor()
            my_cursor.execute('insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                    self.id.get(),
                                                                                                    self.name.get(),
                                                                                                    self.father_name.get(),
                                                                                                    self.address.get(),
                                                                                                    self.session.get(),
                                                                                                    self.dob.get(),
                                                                                                    self.photo_id.get(),
                                                                                                    self.branch.get(),
                                                                                                    self.contact.get(),
                                                                                                    self.gender.get(),))
            connection.commit()
            self.display()
            connection.close()
            messagebox.showinfo("Success","Record has been inserted")

    
    def display(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()
        my_cursor.execute("select *from student_data")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    
    def move_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content["values"]
        self.id.set(row[0])
        self.name.set(row[1])
        self.father_name.set(row[2])
        self.address.set(row[3])
        self.session.set(row[4])
        self.dob.set(row[5])
        self.photo_id.set(row[6])
        self.branch.set(row[7])
        self.contact.set(row[8])
        self.gender.set(row[9])
        
    
    def update(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()
        my_cursor.execute('update student_data set id=%s,name=%s,father_name=%s,address=%s,session=%s,dob=%s,photo_id=%s,branch=%s,contact_number=%s,gender=%s where id=%s',(
                                                                                                    self.id.get(),
                                                                                                    self.name.get(),
                                                                                                    self.father_name.get(),
                                                                                                    self.address.get(),
                                                                                                    self.session.get(),
                                                                                                    self.dob.get(),
                                                                                                    self.photo_id.get(),
                                                                                                    self.branch.get(),
                                                                                                    self.contact.get(),
                                                                                                    self.gender.get(),
                                                                                                    self.id.get()))
        connection.commit()
        self.display()
        connection.close()
        messagebox.showinfo("Updated Successfullly","Record has been updated")

    
    def view(self):
        self.textView.insert(END,"      Addmission Number:\t\t\t"+ self.id.get()+"\n")
        self.textView.insert(END,"      Student Name:\t\t\t"+ self.name.get()+"\n")
        self.textView.insert(END,"      Father Name:\t\t\t"+ self.father_name.get()+"\n")
        self.textView.insert(END,"      Address:\t\t\t"+ self.address.get()+"\n")
        self.textView.insert(END,"      Batch Session:\t\t\t"+ self.session.get()+"\n")
        self.textView.insert(END,"      Date Of Birth:\t\t\t"+ self.dob.get()+"\n")
        self.textView.insert(END,"      Photo Id Number:\t\t\t"+ self.photo_id.get()+"\n")
        self.textView.insert(END,"      Program And Branch Name:\t\t\t"+ self.branch.get()+"\n")
        self.textView.insert(END,"      Contact Number:\t\t\t"+ self.contact.get()+"\n")
        self.textView.insert(END,"      Gender:\t\t\t"+ self.gender.get()+"\n")
    
    def delete(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()

        my_cursor.execute("delete from student_data where id=%s",(self.id.get(),))
        connection.commit()
        self.display()
        connection.close()
        messagebox.showinfo("Deleted Successfullly","Record has been deleted")

    

    def clear(self):
        self.id.set(""),
        self.name.set(""),
        self.father_name.set(""),
        self.address.set(""),
        self.session.set(""),
        self.dob.set(""),
        self.photo_id.set(""),
        self.branch.set(""),
        self.contact.set(""),
        self.gender.set(""),
        self.contact.set(""),
        self.textView.delete("1.0",END)    
        messagebox.showinfo("Clearing","Record has been clear") 

    def exit(self):
        exit=messagebox.askyesno("Admin Portal","Confirm you want to exit!!")
        print(exit)
        if exit>0:
            root1.quit()
            return  


if __name__=="__main__":
    root1=Tk()
    obj=college_admin(root1)
    root1.mainloop()
   