from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox  # for showing message
import cv2                      # import this for using cv library
import mysql.connector          # for connecting mysql database
import os                       # for access of folders and files
import numpy as np              #NumPy is the fundamental package for scientific computing in Python which provides a multidimensional array object


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")          #set according to display size
        self.root.wm_iconbitmap("face.ico")

        # variables for taking input

        self.var_name = StringVar()
        self.var_school = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()

        bg1_lbl = Frame(self.root, bg="#5B7DB1")
        bg1_lbl.place(x=0, y=0, width=1530, height=1000)

        frame = Frame(bg1_lbl, bg="#FFF2F2")
        frame.place(x=600, y=100, width=400, height=500)

        # start from here

        get_start = Label(frame, text="Register User", font=(
            "times new roman", 25, "bold"), fg="red", bg="#FFF2F2")
        get_start.place(x=100, y=40)

        # inside frame

        inside_frame = LabelFrame(frame, bd=2, bg="#FFF2F2", relief=RIDGE,
                                  text="User Details", font=("times new roman", 12, "bold"))
        inside_frame.place(x=20, y=100, width=350, height=200)

        name_label = Label(inside_frame, text="Name:",
                           font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(
            inside_frame,  width=20, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        school_label = Label(inside_frame, text="School Name:",
                             font=("times new roman", 12, "bold"), bg="white")
        school_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        school_entry = ttk.Entry(
            inside_frame,  width=20, textvariable=self.var_school, font=("times new roman", 12, "bold"))
        school_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        username_label = Label(inside_frame, text="Username:",
                               font=("times new roman", 12, "bold"), bg="white")
        username_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        username_entry = ttk.Entry(
            inside_frame,  width=20, textvariable=self.var_username, font=("times new roman", 12, "bold"))
        username_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        password_label = Label(inside_frame, text="Password:",
                               font=("times new roman", 12, "bold"), bg="white")
        password_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        password_entry = ttk.Entry(
            inside_frame,  width=20, textvariable=self.var_password, font=("times new roman", 12, "bold"))
        password_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # save

        save_btn = Button(frame,  text="Save", command=self.add_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=20)
        save_btn.place(x=11, y=350, width=380)

        # take photo sample

        take_photo_sample_btn = Button(frame,  text="Take Photo Sample", command=self.face_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=20)
        take_photo_sample_btn.place(x=11, y=390, width=380)

    # function decration

    def add_data(self):
        if self.var_name.get() == "":
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
                my_cursor.execute("insert into login(name,school,username,password) values(%s,%s,%s,%s)", (

                    self.var_name.get(),
                    self.var_school.get(),
                    self.var_username.get(),
                    self.var_password.get()

                ))         


                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Success", "Students details has benn added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    #face recognize

    def face_data(self):
        if self.var_username.get() == "" and self.var_password.get() == "":
            messagebox.showerror("Error", "All Fields are Required",parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                my_cursor.execute("select * from login")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                conn.commit()
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

                cap = cv2.VideoCapture(0)               #for capture image by default camera
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "faces/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()             #it destroy the current window
                messagebox.showinfo(
                    "Result", "Generating data set completed", parent=self.root)
                self.train_classifier()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    #train data

    def train_classifier(self):
        data_dir = ("faces")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Train", imageNp)
            cv2.waitKey(1) == 13            # camera window is open until press enter. Please pree enter for closing camera window
        ids = np.array(ids)

        # Train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()      # for recognize face
        clf.train(faces, ids)                           # train the images into xml file

        clf.write("faces.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training datasets completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()