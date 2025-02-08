from email import message
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector as database


class college_student:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("\t\t\t\t\t\tSTUDENT PORTAL")
        self.root1.geometry("1200x800")
        
        self.id = StringVar()
        self.name = StringVar()
        self.ont = StringVar()
        self.os = StringVar()
        self.tc = StringVar()
        self.dbms = StringVar()
        self.crypto = StringVar()
        self.cyber = StringVar()
        self.tafl = StringVar()

        lable_title=Label(self.root1,bd=10,relief=RIDGE,text="STUDENT PORTAL",fg="red",bg="white",font=("times new roman",30,"bold"))
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

        self.studenttextView=Text(DataframeLeft,font=("aerial",12),width=102,height=18,padx=2,pady=6)
        self.studenttextView.grid(row=1,column=1)

        self.textView=Text(DataframeRight,font=("aerial",12),width=50,height=18,padx=2,pady=6)
        self.textView.grid(row=0,column=0)

        #***********************************Buttons for Altering**************************************
        Button_prescription=Button(Buttonframe,text="View Marks",command=self.view_marks,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_prescription.grid(row=0,padx=15,column=1)

        Button_Info=Button(Buttonframe,text="Student Profile",command=self.view_info,padx=4,width=22,bg="green",fg="white",font=("aerial",13))
        Button_Info.grid(row=0,padx=15,column=2)


        Button_exit=Button(Buttonframe,text="Exit",command=self.exit,width=22,bg="green",padx=4,fg="white",font=("aerial",13))
        Button_exit.grid(row=0,padx=10,column=6)

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
    

   
    def view_marks(self):
        self.textView.insert(END,"      Operational Research And\n        Numerical Technique\t\t                          "+ self.ont.get()+"\n")
        self.textView.insert(END,"      Operating System\t\t\t\t"+ self.os.get()+"\n")
        self.textView.insert(END,"      Technical Communication:\t\t\t                 "+ self.tc.get()+"\n")
        self.textView.insert(END,"      Database Management System\t\t         "+ self.dbms.get()+"\n")
        self.textView.insert(END,"      Cryptoraphy\t\t\t\t"+ self.crypto.get()+"\n")
        self.textView.insert(END,"      Cyber Security\t\t\t\t"+ self.cyber.get()+"\n")
        self.textView.insert(END,"      Theory Of Automaton And\n      Formal Language\t                                  "+ self.tafl.get()+"\n")
    


    def view_info(self):
        self.studenttextView.insert(END,"      Addmission Number:\t\t\t"+ self.id.get()+"\n")
        self.studenttextView.insert(END,"      Student Name:\t\t\t"+ self.name.get()+"\n")
        self.studenttextView.insert(END,"      Father Name:\t\t\t"+ self.father_name.get()+"\n")
        self.studenttextView.insert(END,"      Address:\t\t\t"+ self.address.get()+"\n")
        self.studenttextView.insert(END,"      Batch Session:\t\t\t"+ self.session.get()+"\n")
        self.studenttextView.insert(END,"      Date Of Birth:\t\t\t"+ self.dob.get()+"\n")
        self.studenttextView.insert(END,"      Photo Id Number:\t\t\t"+ self.photo_id.get()+"\n")
        self.studenttextView.insert(END,"      Program And Branch Name:\t\t\t"+ self.branch.get()+"\n")
        self.studenttextView.insert(END,"      Contact Number:\t\t\t"+ self.contact.get()+"\n")
        self.studenttextView.insert(END,"      Gender:\t\t\t"+ self.gender.get()+"\n")

   

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
            root3.quit()
            return  


if __name__=="__main__":
    root3=Tk()
    obj=college_student(root3)
    root3.mainloop()
   
 