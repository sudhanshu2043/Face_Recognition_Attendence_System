from logging import exception
from tkinter import*
from tkinter import ttk
from turtle import color
from PIL import Image, ImageTk
from tkinter import messagebox

from setuptools import Command
import mysql.connector
import cv2
import os               #for accessing folders and files
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")              #set according to display size
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        # background

        bg1_lbl = Frame(self.root, bg="#E4D1B9")
        bg1_lbl.place(x=0, y=0, width=15300, height=10000)

        title_lbl = Label(bg1_lbl, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roma", 35, "bold"),bg="#B8F1B0", fg="#16003B")
        title_lbl.place(x=0, y=40, width=1530, height=45)

       
        #button

        img6 = Image.open(
            r"images\train.jpg")
        img6 = img6.resize((300, 300), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg1_lbl, image=self.photoimg6, cursor="hand2")
        b1.place(x=600, y=200, width=300, height=300)

        b1_1 = Button(bg1_lbl, text="Train Data",command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#764AF1", fg="white",activeforeground="white", activebackground="red")
        b1_1.place(x=600, y=500, width=300, height=40)

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

            cv2.imshow("Trian",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()   #for recognize face 
        clf.train(faces,ids)                       #train
        
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()