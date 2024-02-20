from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from setuptools import Command
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("15300x7900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # background

        bg1_lbl = Frame(self.root, bg="#1A3C40")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roma", 35, "bold"),bg="#B8F1B0", fg="#16003B")
        title_lbl.place(x=0, y=40, width=1530, height=45)

        # detect face button

        img3 = Image.open(
            r"images\face.jpg")
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg1_lbl, image=self.photoimg3, cursor="hand2",command=self.face_recog)
        b1.place(x=600, y=200, width=300, height=300)

        b1_1 = Button(bg1_lbl, text="Face Detector", cursor="hand2",command=self.face_recog, font=(
            "times new roman", 15, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red")
        b1_1.place(x=600, y=500, width=300, height=40)




    #Attendance

    def mark_attendance(self,i,r,n,d):
        with open("Attendance_Report/Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
            




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

                if confidence > 79:
                    cv2.putText(img,f"Id: {i}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    

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




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
