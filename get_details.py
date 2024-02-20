from tkinter import*
from tkinter import ttk
from turtle import color
from PIL import Image, ImageTk      # pip install pillow
from tkinter import messagebox      # for showing message
import mysql.connector              # for connecting mysql database
import cv2                          # import this for using cv library
import os
import numpy as np

getid=0
class Details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("15300x7900+0+0")                  #set according to display size
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        # here declared all the variables 

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


         # background

        bg1_lbl = Frame(self.root, bg="#5B7DB1")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roma", 35, "bold"),bg="#B8F1B0", fg="#16003B")
        title_lbl.place(x=0, y=40, width=1530, height=45)


        main_frame= Frame(bg1_lbl, bd=2, bg="#FFF2F2")
        main_frame.place(x=360, y=90, width=830, height=670)

        self.getid=0
        self.flag=0



        #search system

        search_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=9, y=10, width=800, height=160)

        search_label = Label(search_frame, text="Search By:",
                             font=("times new roman", 15, "bold"), bg="#36AE7C", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        face_btn = Button(search_frame,text="Scan Face",command=self.face_recog,font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white", width=40 ,activeforeground="white", activebackground="red")
        face_btn.grid(row=0, column=1, padx=2)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=175, width=800, height=460)

        # Current course information

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=9, y=10, width=778, height=130)




        #---------Create a combo box or entry box for taking data----------

        # Department

        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer",
                               "IT", "Electronics", "Civil", "Mechanical", "Food")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course

        course_label = Label(current_course_frame, text="Course",
                             font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = (
            "Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year

        year_label = Label(current_course_frame, text="Year",
                           font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        year_combo["values"] = (
            "Select year", "2020-21", "2021-22", "2022-23", "2022-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semesemester

        semester_label = Label(current_course_frame, text="Semester",
                               font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,  font=(
            "times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = (
            "Select semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=9, y=185, width=778, height=240)

        # studentId

        studentId_label = Label(class_student_frame, text="StudentId:",
                                font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.va_std_id,font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student name

        studentNmae_label = Label(class_student_frame, text="Student Name:",
                                  font=("times new roman", 12, "bold"), bg="white")
        studentNmae_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentNmae_entry = ttk.Entry(
            class_student_frame, width=20,textvariable=self.var_std_name, font=("times new roman", 12, "bold"))
        studentNmae_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_div_label = Label(class_student_frame, text="Class Divison:",
                                font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=(
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
            class_student_frame, width=20, textvariable=self.var_roll,font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender

        gender_label = Label(class_student_frame, text="Gender:",
                             font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Female",
                                  "Male", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Dob

        dob_label = Label(class_student_frame, text="DOB:",
                          font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob ,width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        email_label = Label(class_student_frame, text="Email:",
                            font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no

        phone_no_label = Label(class_student_frame, text="Phone No:",
                               font=("times new roman", 12, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(
            class_student_frame,textvariable=self.var_phone,  width=20, font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address:",
                              font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.var_address,font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name

        teacher_label = Label(class_student_frame, text="Teacher:",
                              font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.var_teacher,font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons

        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # table frame

        table_frame = Frame(search_frame, bd=2, bg="white", relief=RIDGE,)
        table_frame.place(x=9, y=50, width=770, height=75)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address","teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
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
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
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
        


    
    # Face Recognition

    def face_recog(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord =[]

            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                self.getid=i

                if confidence > 78:
                    cv2.putText(img,f"Id: {i}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.flag=1

                    

                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognizer",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        if self.flag==1:
            messagebox.showinfo("Success","Student Details Found",parent=self.root)
            self.search_data()
            self.flag=0
        else:
            messagebox.showerror("Error","No details found",parent=self.root)
            


    #search data

    def search_data(self):
        if self.flag==0:
            messagebox.showerror("Error","Student Details Not Found")
        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                query=("select * from student where Student_id=%s")
                value=(self.getid,)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please Enter valid student id",parent=self.root)
                else:
                    query=("select * from student where Student_id=%s")
                    value=(self.getid,)
                    my_cursor.execute(query,value)
                    data=my_cursor.fetchall()
                    if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
                    
                    
                
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)


    

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





if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
