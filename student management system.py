from tkinter import  *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Mnagement System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="light grey")

        photo =PhotoImage(file=r"C:\\Users\\mpstate mining\\Downloads\\icon.png")
        root.iconphoto(False, photo)

        title = Label(self.root , text="STUDENT MANAGEMENT SYSTEM"  , font= ("times of roman",40,"bold") , bg="grey" , fg = "white")
        title.pack(side=TOP,fill = X,pady=15,padx=23)

        #creating variables
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.gender_var = StringVar()
        self.add_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()
        self.search_all = StringVar()

        #creating manage frame
        manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        manage_frame.place(x=20,y=100,width=450,height=580)

        m_title = Label(manage_frame,text="Student Details",bg="grey",fg="white",font=("times of roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,padx=100)

        lbl_roll = Label(manage_frame,text="Roll Number :",bg="grey",fg="white",font=("times of roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        text_roll = Entry(manage_frame,font=("times of roman", 14),textvariable= self.roll_var)
        text_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text="Name :", bg="grey", fg="white",
                         font=("times of roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        text_name = Entry(manage_frame, font=("times of roman", 14),textvariable= self.name_var)
        text_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(manage_frame, text="Email :", bg="grey", fg="white",
                         font=("times of roman", 15, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20,sticky="w")

        text_email = Entry(manage_frame, font=("times of roman", 14),textvariable= self.email_var)
        text_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender :", bg="grey", fg="white",
                          font=("times of roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender  = ttk.Combobox(manage_frame,font=("times of roman",14),width=18,state="readonly",textvariable= self.gender_var)
        combo_gender["values"] = ("male","female","other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(manage_frame, text="Contact :", bg="grey", fg="white",
                         font=("times of roman", 15, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20,sticky="w")

        text_contact = Entry(manage_frame, font=("times of roman", 14),textvariable= self.contact_var)
        text_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B. :", bg="grey", fg="white",
                            font=("times of roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        text_dob = Entry(manage_frame, font=("times of roman", 14),textvariable= self.dob_var)
        text_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_add = Label(manage_frame, text="Address :", bg="grey", fg="white",
                        font=("times of roman", 15, "bold"))
        lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.text_add = Text(manage_frame,width=20,height=3,font=("times of roman",14),wrap="word")
        self.text_add.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #creating buttons
        btn_frame = Frame(manage_frame,bg="grey")
        btn_frame.place(x=15,y=500,width=420)

        addbtn = Button(btn_frame,text="Add",width=10,command=self.add_data).grid(row=0,column=0,padx=11,pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=11, pady=10)
        delbtn = Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=11, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10,command=self.clear_data).grid(row=0, column=3, padx=11, pady=10)

        #creating detail frame
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg = "grey")
        detail_frame.place(x=500, y=100, width=825, height=580)

        #creating options
        lbl_search = Label(detail_frame,text="Search by :",bg="grey",fg="white",font=("times of roman",14,'bold'))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="e")

        combo_search = ttk.Combobox(detail_frame,font=("times of roman",13),state="readonly",width=11,textvariable=self.search_by)
        combo_search["values"] = ("Roll Number","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10,sticky="w")

        self.text_search = Entry(detail_frame,font=("times of roman",14),textvariable=self.search_text)
        self.text_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(detail_frame,text="Search",width=10,height=1,command=self.search_data).grid(row=0,column=4,padx=15,pady=20)
        searchallbtn = Button(detail_frame, text="All", width=10, height=1,command=self.fetch_data).grid(row=0, column=5, padx=15, pady=20)

        #creating table frame
        table_frame = Frame(detail_frame,bg="crimson")
        table_frame.place(x=10,y=65,width=800,height=500)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll no.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("roll",width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("email", width=200)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=300)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease-1>",self.get_cursor_row)
        self.fetch_data()

    #database connection functions

    #function to add student details
    def add_data(self):
        if self.roll_var.get() == "" or self.name_var.get() == "" :
            messagebox.showerror("Error","Roll no. and Name are required.")
        else:
            con = pymysql.connect(host="localhost",user="root",password="admin",database="student_management")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(  self.roll_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.text_add.get("1.0",END) ))
            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            messagebox.showinfo("Success", "Record inserted successfully.")

    #function to show details table in GUI
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="admin", database="student_management")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()

    def clear_data(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_add.delete("1.0",END)


    def get_cursor_row(self,e):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents["values"]
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_add.delete("1.0",END)
        self.text_add.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="admin", database="student_management")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s",(
            self.name_var.get(), self.email_var.get(), self.gender_var.get(),
            self.contact_var.get(), self.dob_var.get(), self.text_add.get("1.0", END),
            self.roll_var.get() ))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()
        messagebox.showinfo("Success", "Record updated successfully.")

    def delete_data(self):
        ans = messagebox.askquestion("Warning", "Are you sure want to delete the record?")
        if ans == "yes":
            con = pymysql.connect(host="localhost", user="root", password="admin", database="student_management")
            cur = con.cursor()
            cur.execute("delete from students where roll=%s",self.roll_var.get() )
            con.commit()
            con.close()
            self.fetch_data()
            self.clear_data()
            messagebox.showinfo("Success","Record deleted successfully.")


    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="admin", database="student_management")
        cur = con.cursor()
        sql = ""
        s = (self.text_search.get(),)
        if self.search_by.get() == "Roll Number":
            sql = "select * from students where roll = %s"
        if self.search_by.get() == "Name":
            sql = "select * from students where name = %s"
        if self.search_by.get() == "Contact":
            sql = "select * from students where contact = %s"

        result = cur.execute(sql,s)

        result = rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)

        if not result:
            messagebox.showerror("Error","Incorrect detail or Record not found.")

            con.commit()
        con.close()


root =Tk()
ob = student(root)
root.mainloop()