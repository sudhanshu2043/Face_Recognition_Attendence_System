# Face Recognition Based Attendance System with Face Authentication System

## How I build this project

Hello Everyone, Myself Sudhanshu Kumar. I am a 4th-year Undergrad Student in Electronics & Communication Engineering. I am pursuing my B.tech from Sant Longowal Institute of Engineering and Technology.
 

Simply I start with python. Learn python as per requirement then I learned how to build a GUI application with Python Tkinter. Then I learned a little bit about some libraries such as OpenCV, Numpy, and Face Recognition. I have also learned about the MySQL database.
 
During building this project I have faced a lot of problems such as the installation process of all libraries, connecting with the database, how to use face recognition and how to store the face data etc.
But solving all the problems finally, I have built this project. Firstly, I build a Face Recognition based Attendance System then after that I decided to build a standard Authentication system using face recognition. Then after building authentication, I attached it with Face Recognition based Attendance System.



## System Requirements

1.	Install python version 3.8.5
2.	Install MySql database
3.	Install mysql connector by command prompt pip install mysql-connector
4.	Install pillow by pip install pillow
5.	Install Tkinter by command prompt pip install tk
6.	Install OpenCv by pip install opencv-python
7.	Install Numpy by pip install numpy
8.	Install Face Recognition manually
9.	Install os by pip insatll os-sys

## Features

1. Face Authentication System
2. Forget Password Option
3. Update details of student
4. Delete details of student
5. Search option
6. Fetched all the registerd student data in frame
7. Mark Attendance
8. View attendance
9. Export attendance
10. View Details by scan face


## Some important point

Please write Student id sequentially otherwise face recognition alorithms will be not work properly.

If the face detector lag its means server working slow because it's database connected with online database system.

If any case get a error of mysql database then please use offline databse which is comment down in whole code.
Offline database code look like this:- 

#conn = mysql.connector.connect(host="localhost", user="root", password="123",
                              #database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
#my_cursor = conn.cursor()

Change this code in every python file where it is present, if online database will not worked properly.

Please don't forget to scan face after add student details and user data otherwise face recognition algorithm will not work properly.



## for developer

if you run index.py then its ask username and password.


For direct login use this:

username:-- user

password:-- user



