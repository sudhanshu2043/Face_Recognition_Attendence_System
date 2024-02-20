from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from setuptools import Command
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv



mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("15300x7900+0+0")
        self.root.title("face Recognition System")          # set according to display size
        self.root.wm_iconbitmap("face.ico")

        #Variables for taking inputs

        self.var_attendanceId=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        # background

        bg1_lbl = Frame(self.root, bg="#5B7DB1")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="ATTENDANCE MANAGEMENT SYSTEM", font=(
            "times new roma", 35, "bold"), bg="#FFEBC1", fg="black")
        title_lbl.place(x=0, y=40, width=1530, height=45)

        main_frame = Frame(bg1_lbl, bd=2, bg="#FFF2F2")
        main_frame.place(x=110, y=100, width=1300, height=672)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=20, width=630, height=620)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="#FFF2F2")
        left_inside_frame.place(x=12, y=7, width=600, height=400)

        # Label Entry

        # Attendance id

        attendanceId_label = Label(left_inside_frame, text="AttendanceId:",
                                   font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=18,textvariable=self.var_attendanceId, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=9, sticky=W)

        # Roll

        roll_label = Label(left_inside_frame, text="Roll:",
                           font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=8, sticky=W)

        roll_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=8, pady=9, sticky=W)

        # Name

        name_label = Label(left_inside_frame, text="Name:",
                           font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=8, sticky=W)

        name_entry = ttk.Entry(
            left_inside_frame, width=18,textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=9, sticky=W)

        # Department

        dep_label = Label(left_inside_frame, text="Department:",
                          font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=8, sticky=W)

        dep_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_dep, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=8, pady=9, sticky=W)

        # Time

        time_label = Label(left_inside_frame, text="Time:",
                           font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=8, sticky=W)

        time_entry = ttk.Entry(
            left_inside_frame, width=18,textvariable=self.var_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=8, pady=9, sticky=W)

        # Date

        date_label = Label(left_inside_frame, text="Date:",
                           font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=8, sticky=W)

        date_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=8, pady=9, sticky=W)

        # Attendance Status

        attend_label = Label(left_inside_frame, text="Attendance Stauts:",
                             font=("times new roman", 12, "bold"), bg="white")
        attend_label.grid(row=3, column=0, padx=8, pady=5, sticky=W)

        attend_combo = ttk.Combobox(left_inside_frame,  font=(
            "times new roman", 12, "bold"), state="readonly", width=18,textvariable=self.var_attendance,)
        attend_combo["values"] = ("Stauts", "Present",
                                  "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3, column=1, padx=8, pady=10, sticky=W)

        # button frame1

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=350, width=600, height=35)

        # import

        import_btn = Button(btn_frame,  text="Imporst csv",command=self.importCsv, font=(
            "times new roman", 12, "bold"),bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=20)
        import_btn.grid(row=0, column=0)

        # Export

        export_btn = Button(btn_frame,  text="Export csv",command=self.exportCsv , font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=20)
        export_btn.grid(row=0, column=1, padx=2)


        # reset

        reset_btn = Button(btn_frame,  text="Reset", font=(
            "times new roman", 12, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red", width=22,command=self.reset_data)
        reset_btn.grid(row=0, column=2, padx=1)

        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=660, y=20, width=622, height=620)

        # button frame2

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#FFF2F2")
        table_frame.place(x=9, y=5, width=600, height=550)

        # Scroll Bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100,)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #fetch data

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    
    
    #import csv


    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    
    #export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" suceessfully",parent=self.root)

        except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_attendanceId.set(row[0])
        self.var_roll.set(row[1])
        self.var_name.set(row[2])
        self.var_dep.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendance.set(row[6])


    #reset
    def reset_data(self):
        self.var_attendanceId.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
