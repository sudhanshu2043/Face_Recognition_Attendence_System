from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from get_details import Details
import tkinter


# for creating window
# ----------------------------


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("15300x7900+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # background

        bg1_lbl = Frame(self.root, bg="#BDE6F1")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=(
            "times new roma", 35, "bold"),bg="#B8F1B0", fg="#16003B")
        title_lbl.place(x=0, y=40, width=1530, height=45)

        # student button

        img2 = Image.open(
            r"images\student.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg1_lbl, image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=220, y=130, width=220, height=220)

        b1_1 = Button(bg1_lbl, text="Student Registration",command=self.student_details,cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=220, y=320, width=220, height=40)

        # detect face and make attendance button

        img3 = Image.open(
            r"images\face.jpg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg1_lbl, image=self.photoimg3, cursor="hand2",command=self.face_data)
        b1.place(x=660, y=130, width=220, height=220)

        b1_1 = Button(bg1_lbl, text="Make Attendance", cursor="hand2",command=self.face_data ,font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=660, y=320, width=220, height=40)

        # View Attendance 

        img4 = Image.open(
            r"images\attendance.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg1_lbl, image=self.photoimg4, cursor="hand2",command=self.attendance_data)
        b1.place(x=1100, y=130, width=220, height=220)

        b1_1 = Button(bg1_lbl, text="View Attendance", cursor="hand2",command=self.attendance_data ,font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=1100, y=320, width=220, height=40)

        

        # Train Face

        img6 = Image.open(
            r"images\train.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg1_lbl, image=self.photoimg6,command=self.train_data, cursor="hand2")
        b1.place(x=220, y=380, width=220, height=220)

        b1_1 = Button(bg1_lbl,command=self.train_data, text="Train", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=220, y=580, width=220, height=40)

        # Get details of students

        img7 = Image.open(
            r"images\std1.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg1_lbl, image=self.photoimg7, cursor="hand2",command=self.get_details)
        b1.place(x=660, y=380, width=220, height=220)

        b1_1 = Button(bg1_lbl, text="Student Details", cursor="hand2",command=self.get_details, font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=660, y=580, width=220, height=40)

        

        # Exit

        img9 = Image.open(
            r"images\exit.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg1_lbl, image=self.photoimg9, cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg1_lbl, text="Exit", cursor="hand2",command=self.exit, font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)







    #create a functions for calling 

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def get_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

# ---------------------------------
