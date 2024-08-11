from email import message
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector as database


class college_faculty:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("\t\t\t\t\t\tADMIN PORTAL")
        self.root1.geometry("1200x1000")
        self.id = StringVar()
        self.name = StringVar()
        self.ont = StringVar()
        self.os = StringVar()
        self.tc = StringVar()
        self.dbms = StringVar()
        self.crypto = StringVar()
        self.cyber = StringVar()
        self.tafl = StringVar()

       
        lable_title=Label(self.root1,bd=10,relief=RIDGE,text="FACULTY PORTAL",fg="red",bg="white",font=("times new roman",30,"bold"))
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
        Label_Name=Label(DataframeLeft,text="Admission No",padx=2,pady=6,font=("aerial",12))
        Label_Name.grid(row=0,column=0)
        Text_Name=Entry(DataframeLeft,textvariable=self.id,width=30,font=("aerial",12))
        Text_Name.grid(row=0,column=1)

        Label_Father_name=Label(DataframeLeft,text="Student Name",padx=2,pady=6,font=("aerial",12))
        Label_Father_name.grid(row=1,column=0)
        Text_Father_name=Entry(DataframeLeft,textvariable=self.name,width=30,font=("aerial",12))
        Text_Father_name.grid(row=1,column=1)

        Label_Patient_Id=Label(DataframeLeft,text="Operational research And\nNumerical Technique",padx=2,pady=6,font=("aerial",12))
        Label_Patient_Id.grid(row=2,column=0)
        Text_Patient_Id=Entry(DataframeLeft,textvariable=self.ont,width=30,font=("aerial",12))
        Text_Patient_Id.grid(row=2,column=1)

        Label_address=Label(DataframeLeft,text="Operating System",padx=2,pady=6,font=("aerial",12))
        Label_address.grid(row=3,column=0)
        Text_address=Entry(DataframeLeft,textvariable=self.os,width=30,font=("aerial",12))
        Text_address.grid(row=3,column=1)

        Label_bp=Label(DataframeLeft,text="Technical Communication",padx=2,pady=6,font=("aerial",12))
        Label_bp.grid(row=4,column=0)
        Text_bp=Entry(DataframeLeft,textvariable=self.tc,width=30,font=("aerial",12))
        Text_bp.grid(row=4,column=1)

        Label_dob=Label(DataframeLeft,text="Database Management \nSyatem",padx=2,pady=6,font=("aerial",12))
        Label_dob.grid(row=5,column=0)
        Text_dob=Entry(DataframeLeft,textvariable=self.dbms,width=30,font=("aerial",12))
        Text_dob.grid(row=5,column=1)

        Label_Id_No=Label(DataframeLeft,text="Cryptoraphy",padx=2,pady=6,font=("aerial",12))
        Label_Id_No.grid(row=6,column=0)
        Text_Id_No=Entry(DataframeLeft,textvariable=self.crypto,width=30,font=("aerial",12))
        Text_Id_No.grid(row=6,column=1)

        Label_branch=Label(DataframeLeft,text="       Cyber Security",padx=2,pady=6,font=("aerial",12))
        Label_branch.grid(row=7,column=0)
        Label_branch=Entry(DataframeLeft,textvariable=self.cyber,width=30,font=("aerial",12))
        Label_branch.grid(row=7,column=1)

        Label_b=Label(DataframeLeft,text="Theory Of Automaton And \nFormal Languages",padx=2,pady=6,font=("aerial",12))
        Label_b.grid(row=8,column=0)
        Label_b=Entry(DataframeLeft,textvariable=self.tafl,width=30,font=("aerial",12))
        Label_b.grid(row=8,column=1)

        
        self.textView=Text(DataframeRight,font=("aerial",12),width=50,height=18,padx=2,pady=6)
        self.textView.grid(row=0,column=0)


        #***********************************Buttons for Altering**************************************
        Button_prescription=Button(Buttonframe,text="View Marks",command=self.view,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_prescription.grid(row=0,padx=8,column=1)

        Button_prescription_data=Button(Buttonframe,text="Adding Marks",command=self.add_data,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_prescription_data.grid(row=0,padx=3,column=2)

        Button_update=Button(Buttonframe,text="Updating Matks",command=self.update,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_update.grid(row=0,padx=4,column=3)

        Button_delete=Button(Buttonframe,text="Delete Marks",command=self.delete,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_delete.grid(row=0,padx=4,column=4)

        Button_clear=Button(Buttonframe,text="Clear",command=self.clear,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_clear.grid(row=0,padx=4,column=5)

        Button_exit=Button(Buttonframe,text="Exit",command=self.exit,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_exit.grid(row=0,padx=4,column=6)

        #***********************************Buttons for Altering**************************************
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.student_table=ttk.Treeview(Detailsframe,column=("Admission No","Student Name","Operational Research And Numerical Technique","Operating System","Technical Communication",
                                                             "Database Management Syatem","Cryptoraphy","Cyber Security","Theory Of Automaton And Formal Language"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)        
        scroll_x=ttk.Scrollbar(command=self.student_table.xview)  
        scroll_y=ttk.Scrollbar(command=self.student_table.yview)      

        self.student_table.heading("Admission No",text="Admission No")  
        self.student_table.heading("Student Name",text="Student Name")  
        self.student_table.heading("Operational Research And Numerical Technique",text="Operational Research And Numerical Technique") 
        self.student_table.heading("Operating System",text="Operating System")  
        self.student_table.heading("Technical Communication",text="Technical Communication")  
        self.student_table.heading("Database Management Syatem",text="Database Management System")  
        self.student_table.heading("Cryptoraphy",text="Cryptoraphy")  
        self.student_table.heading("Cyber Security",text="Cyber Security") 
        self.student_table.heading("Theory Of Automaton And Formal Language",text="Theory Of Automaton And Formal Language") 
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.column("Admission No",width=50)  
        self.student_table.column("Student Name",width=50)
        self.student_table.column("Operational Research And Numerical Technique",width=210)    
        self.student_table.column("Operating System",width=100)  
        self.student_table.column("Technical Communication",width=100)  
        self.student_table.column("Database Management Syatem",width=120)  
        self.student_table.column("Cryptoraphy",width=60)  
        self.student_table.column("Cyber Security",width=60)
        self.student_table.column("Theory Of Automaton And Formal Language",width=200)   
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
            my_cursor.execute('insert into marks_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                    self.id.get(),
                                                                                                    self.name.get(),
                                                                                                    self.ont.get(),
                                                                                                    self.os.get(),
                                                                                                    self.tc.get(),
                                                                                                    self.dbms.get(),
                                                                                                    self.crypto.get(),
                                                                                                    self.cyber.get(),
                                                                                                    self.tafl.get(),))
            connection.commit()
            self.display()
            connection.close()
            messagebox.showinfo("Success","Record has been inserted")

    
    def display(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()
        my_cursor.execute("select *from marks_data")
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
        self.ont.set(row[2])
        self.os.set(row[3])
        self.tc.set(row[4])
        self.dbms.set(row[5])
        self.crypto.set(row[6])
        self.cyber.set(row[7])
        self.tafl.set(row[8])
    

    def update(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()
        my_cursor.execute('update marks_data set id=%s,name=%s,ont=%s,os=%s,tc=%s,dbms=%s,crypto=%s,cyber=%s,tafl=%s where id=%s',(self.id.get(),
                                                                                                                                    self.name.get(),
                                                                                                                                    self.ont.get(),
                                                                                                                                    self.os.get(),
                                                                                                                                    self.tc.get(),
                                                                                                                                    self.dbms.get(),
                                                                                                                                    self.crypto.get(),
                                                                                                                                    self.cyber.get(),
                                                                                                                                    self.tafl.get(),
                                                                                                                                    self.id.get(),))
        connection.commit()
        self.display()
        connection.close()
        messagebox.showinfo("Updated Successfullly","Record has been updated")

    def view(self):
        self.textView.insert(END,"      Addmission Number:\t\t\t\t"+ self.id.get()+"\n")
        self.textView.insert(END,"      Student Name:\t\t\t\t"+ self.name.get()+"\n")
        self.textView.insert(END,"      Operational Research And\n        Numerical Technique\t\t                          "+ self.ont.get()+"\n")
        self.textView.insert(END,"      Operating System\t\t\t\t"+ self.os.get()+"\n")
        self.textView.insert(END,"      Technical Communication:\t\t\t                 "+ self.tc.get()+"\n")
        self.textView.insert(END,"      Database Management System\t\t         "+ self.dbms.get()+"\n")
        self.textView.insert(END,"      Cryptoraphy\t\t\t\t"+ self.crypto.get()+"\n")
        self.textView.insert(END,"      Cyber Security\t\t\t\t"+ self.cyber.get()+"\n")
        self.textView.insert(END,"      Theory Of Automaton And\n      Formal Language\t                                  "+ self.tafl.get()+"\n")

    def delete(self):
        connection=database.connect(host="localhost",user="root",password="12345",database="project")
        my_cursor=connection.cursor()
        my_cursor.execute("delete from marks_data where id=%s",(self.id.get(),))
        connection.commit()
        self.display()
        connection.close()
        messagebox.showinfo("Deleted Successfullly","Record has been deleted")

    

    def clear(self):
        self.id.set(""),
        self.name.set(""),
        self.ont.set(""),
        self.os.set(""),
        self.tc.set(""),
        self.dbms.set(""),
        self.crypto.set(""),
        self.cyber.set(""),
        self.tafl.set(""),
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
    obj=college_faculty(root1)
    root1.mainloop()
   
 