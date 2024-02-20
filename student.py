from tkinter import*
from tkinter import ttk
from turtle import color
from PIL import Image, ImageTk      # pip install pillow
from tkinter import messagebox      # for showing message
import mysql.connector              # for connecting mysql database
import cv2                          # import this for using cv library
import os
import numpy as np


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")                  #set according to display size
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        # here declared all the variables which is used to take data and sent to database

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_std_name = StringVar()
        self.var_radio1 = StringVar()



        #-------------------background--------------------


        
        bg1_lbl = Frame(self.root, bg="#5B7DB1")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roma", 35, "bold"),bg="#B8F1B0", fg="#16003B")
        title_lbl.place(x=0, y=40, width=1530, height=45)

        main_frame = Frame(bg1_lbl, bd=2, bg="#FFF2F2")
        main_frame.place(x=12, y=100, width=1500, height=672)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=20, width=800, height=620)

        # Current course information

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=9, y=10, width=778, height=150)




        #---------Create a combo box or entry box for taking data----------

        # Department

        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer",
                               "IT", "Electronics", "Civil", "Mechanical", "Food")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course

        course_label = Label(current_course_frame, text="Course",
                             font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = (
            "Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year

        year_label = Label(current_course_frame, text="Year",
                           font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        year_combo["values"] = (
            "Select year", "2020-21", "2021-22", "2022-23", "2022-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semesemester

        semester_label = Label(current_course_frame, text="Semester",
                               font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = (
            "Select semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=9, y=170, width=778, height=415)

        # studentId

        studentId_label = Label(class_student_frame, text="StudentId:",
                                font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_frame, textvariable=self.va_std_id, width=20, font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student name

        studentNmae_label = Label(class_student_frame, text="Student Name:",
                                  font=("times new roman", 12, "bold"), bg="white")
        studentNmae_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentNmae_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentNmae_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_div_label = Label(class_student_frame, text="Class Divison:",
                                font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("Select Division", "A",
                               "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Roll No

        roll_no_label = Label(class_student_frame, text="Roll No:",
                              font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender

        gender_label = Label(class_student_frame, text="Gender:",
                             font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Female",
                                  "Male", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Dob

        dob_label = Label(class_student_frame, text="DOB:",
                          font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        email_label = Label(class_student_frame, text="Email:",
                            font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no

        phone_no_label = Label(class_student_frame, text="Phone No:",
                               font=("times new roman", 12, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address:",
                              font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name

        teacher_label = Label(class_student_frame, text="Teacher:",
                              font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons

        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame1

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="#FFF2F2")
        btn_frame.place(x=6, y=215, width=760, height=35)

        # save

        save_btn = Button(btn_frame, command=self.add_data, text="Save", font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white", activeforeground="white", activebackground="red",width=22)
        save_btn.grid(row=0, column=0)

        # update

        update_btn = Button(btn_frame, command=self.update_data, text="Update", font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white", activeforeground="white", activebackground="red", width=20)
        update_btn.grid(row=0, column=1)

        # delete

        delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", font=(
            "times new roman", 12, "bold"),  bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=20)
        delete_btn.grid(row=0, column=2)

        # reset

        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=20)
        reset_btn.grid(row=0, column=3)

        # button frame2

        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="#FFF2F2")
        btn_frame2.place(x=6, y=248, width=760, height=35)

        # take photo sample

        take_photo_sample_btn = Button(btn_frame2, command=self.generate_dataset, text="Take Photo Sample", font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=83)
        take_photo_sample_btn.grid(row=1, column=0)


        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=820, y=20, width=660, height=620)



        # Search System

        search_frame = LabelFrame(Right_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=9, y=10, width=630, height=70)

        search_label = Label(search_frame, text="Search By:",
                             font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.var_combo_search=StringVar()


        search_combo = ttk.Combobox(search_frame,textvariable=self.var_combo_search, font=(
            "times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = (
            "Select", "Roll", "Phone","Name","Teacher","Student_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(
            search_frame,textvariable=self.var_search, width=14, font=("times new roman", 12, "bold"),)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",command=self.search_data, font=(
            "times new roman", 12, "bold"),  fg="white", width=10,bg="#764AF1" ,activeforeground="white", activebackground="red")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, text="Show All",command=self.fetch_data, font=(
            "times new roman", 12, "bold"), bg="#764AF1",  activeforeground="white", activebackground="red", fg="white", width=10)
        showAll_btn.grid(row=0, column=4, padx=2)

        # table frame

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE,)
        table_frame.place(x=9, y=90, width=630, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll",
                                           "gender", "dob", "email", "phone", "address","teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Divison")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=90)
        self.student_table.column("course", width=90)
        self.student_table.column("year", width=90)
        self.student_table.column("sem", width=90)
        self.student_table.column("id", width=90)
        self.student_table.column("name", width=90)
        self.student_table.column("div", width=90)
        self.student_table.column("roll", width=90)
        self.student_table.column("teacher", width=90)
        self.student_table.column("gender", width=90)
        self.student_table.column("dob", width=90)
        self.student_table.column("email", width=90)
        self.student_table.column("phone", width=90)
        self.student_table.column("address", width=90)
        self.student_table.column("photo", width=90)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # function decration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fileds are required", parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Students details has benn added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # fetch data

    def fetch_data(self):
        # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
        #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
        # my_cursor = conn.cursor()
        conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                        database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fileds are required", parent=self.root)

        else:
            try:
                Upadate = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root)
                if Upadate > 0:

                    #now connect with database please change according to your database system 

                    # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                    #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                    # my_cursor = conn.cursor()
                    conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                                database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where (Student_id=%s)", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()

                    ))   # write this according to database 


                else:
                    if not Upadate:
                        return
                messagebox.showinfo(
                    "Success", "Student details successsfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # delete function

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)

        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                    #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                    # my_cursor = conn.cursor()
                    conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                                database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted this student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Slect Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    

    #search data

    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        
        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                ans=my_cursor.execute("select * from student where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # Generate data set or take photo samples

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fileds are required", parent=self.root)

        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.va_std_id.get() == id+1

                ))
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()

                # load predefined data on face frontals from openCv

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # scaling factor = 1.3
                    # Minimum Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed",parent=self.root)
                open_main=messagebox.askyesno("Yes No","Do you want to train images now?",parent=self.root)
                if open_main>0:
                    self.train_classifier()
                else:
                    return
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)
    

    #train face data

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')   #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
