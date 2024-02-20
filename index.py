from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk       # pip install pillow
from tkinter import messagebox       # for showing message
import mysql.connector               # for connecting mysql database
import cv2                           # for using openCv library
from register import Register        # from register.py import the Register class  
from main import Face_Recognition_System 


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("15500x800+0+0")      # set according to display size
        self.root.wm_iconbitmap("face.ico")

        # ------------background---------------------

        

        bg1_lbl = Frame(self.root, bg="#FF6B6B")
        bg1_lbl.place(x=0, y=0, width=15300, height=1000)

        frame = Frame(bg1_lbl, bg="black")
        frame.place(x=600, y=180, width=330, height=450)

        img1 = Image.open(r"images\log1.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=720, y=185, width=100, height=100)

        self.flag=0

        # --------------------start from here-------------------


        get_start = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_start.place(x=95, y=100)


        # labels

        username_lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # Icon

        img2 = Image.open(r"images\log1.png")
        img2 = img2.resize((22, 22), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=648, y=338, width=22, height=22)

        img3 = Image.open(r"images\key.png")
        img3 = img3.resize((22, 22), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=648, y=408, width=22, height=22)

        # login_button

        login_btn = Button(frame, text="Login",cursor="hand2" ,font=("times new roman", 15, "bold"), bd=3,
                           relief=RIDGE,command=self.login, fg="white", bg="sky blue", activeforeground="white", activebackground="red")
        login_btn.place(x=30, y=300, width=120, height=35)
        
        # detect_button

        detec_btn = Button(frame, text="Detect",cursor="hand2" ,font=("times new roman", 15, "bold"), bd=3,command=self.face_recog,
                           relief=RIDGE,fg="white", bg="sky blue", activeforeground="white", activebackground="red")

        detec_btn.place(x=200, y=300, width=120, height=35)

        # registration_button

        registration_btn = Button(frame, text="New User Register", cursor="hand2" ,font=("times new roman", 10, "bold"),command=self.register,
                                  borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        registration_btn.place(x=15, y=350, width=150, height=20)

        # forget_button

        forget_btn = Button(frame, text="Forget Password",cursor="hand2" , font=("times new roman", 10, "bold"),command=self.forget_password,
                            borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        forget_btn.place(x=15, y=373, width=150, height=20)

    #-------------face detector function-------------------

    def face_recog(self):
        flag=0
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord =[]
            

            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))              # it is forumula which calculate the percentage of face recognize with face data



                if confidence > 78:                  # set acccording to yourself    
                    cv2.putText(img,"Unlocked",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.flag=1
                    
                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img,"locked",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.flag=0
                    


                coord=[x,y,w,h]
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("faces.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognizer",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        self.login()
    
    def login(self):
        if self.txtuser.get()==" " or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)

        elif self.txtuser.get()=="user" and self.txtpass.get()=="user":
            self.face.LBPHFaceRecognizer_create()

        elif self.txtuser.get()=="user" and self.txtpass.get()=="user" and self.flag==1:
                messagebox.showinfo("Success","Successfully Login",parent=self.root)
                self.face()
                

        else:
            try:
                # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
                #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
                # my_cursor = conn.cursor()
                conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                            database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
                my_cursor = conn.cursor()
                my_cursor.execute("select * from login where username=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid login details")
                else:

                    open_main=messagebox.askyesno("Yes No","Access only admin",parent=self.root)
                    if self.flag==0:
                        messagebox.showerror("Error","Please Detect your face first",parent=self.root)
                    if open_main>0 and self.flag==1:
                        self.face()
                        self.flag=0
                    else:
                        if not open_main:
                            return

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To: {str(es)}", parent=self.root)



    #---------functions-----------------

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def face(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    
    #----------reset password--------------

    def  reset_pass(self):
        if self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the security answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
            #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
            # my_cursor = conn.cursor()
            conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                         database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
            my_cursor = conn.cursor()
            qury=("select * from login where username=%s and school=%s")
            vlue=(self.txtuser.get(),self.txt_security.get())
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct details",parent=self.root2)
            else:
                query=("update login set password=%s where username=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset successfully",parent=self.root2)
                self.root2.destroy()



    

    #---------------------forget passwor function---------------  


    def forget_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Pleas Enter the valid user name",parent=self.root)
        else:
            # conn = mysql.connector.connect(host="sql6.freemysqlhosting.net", user="sql6495753", password="KLdC4PA9zU",
            #                                   database="sql6495753", auth_plugin="mysql_native_password")            #please change it accoridng to database
            # my_cursor = conn.cursor()
            conn = mysql.connector.connect(host="localhost", user="root", password="@As11943",
                                         database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
            my_cursor = conn.cursor()
            query=("select * from login where username=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 25, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="Security Question",font=("times new roman", 12, "bold"), fg="black", bg="white")
                security_q.place(x=50,y=80)

                

                security_A=Label(self.root2,text="Enter Your School Name",font=("times new roman", 12, "bold"), fg="black", bg="white")
                security_A.place(x=50,y=130)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman", 12, "bold"))
                self.txt_security.place(x=50,y=160,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman", 12, "bold"), fg="black", bg="white")
                new_pass.place(x=50,y=200)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman", 12, "bold"))
                self.txt_newpass.place(x=50,y=230,width=250)

                #button

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass, font=("times new roman",15,"bold"),fg="white", bg="red", activeforeground="white", activebackground="green")
                btn.place(x=20,y=280,width=300)







if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
