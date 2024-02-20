# Face Recognition Based Attendance System with Face Authentication System

## How I build this project

Hello Everyone, Myself Aryan Jaiswal. I am a 2nd-year Undergrad Student in Computer Science and Engineering. I am pursuing my B.tech from the Kalinga Institute of Industrial Technology.
 
First of all, I would like to thank Microsoft for giving this great mentorship program. In this mentorship program, I have learned many things.
 
In the starting, I have no idea how to start because I have no more knowledge of development. Simply I start with python. Learn python as per requirement then I learned how to build a GUI application with Python Tkinter. Then I learned a little bit about some libraries such as OpenCV, Numpy, and Face Recognition. I have also learned about the MySQL database.
 
During building this project I have faced a lot of problems such as the installation process of all libraries, connecting with the database, how to use face recognition and how to store the face data etc.
But solving all the problems finally, I have built this project. Firstly, I build a Face Recognition based Attendance System then after that I decided to build a standard Authentication system using face recognition. Then after building authentication, I attached it with Face Recognition based Attendance System.

## Demo

https://youtu.be/4llekhpDu5M


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

#conn = mysql.connector.connect(host="localhost", user="root", password="Aryan@123",
                              #database="face_recognition", auth_plugin="mysql_native_password")            #please change it accoridng to database
#my_cursor = conn.cursor()

Change this code in every python file where it is present, if online database will not worked properly.

Please don't forget to scan face after add student details and user data otherwise face recognition algorithm will not work properly.

## Online Databse Credentials

Server: sql6.freemysqlhosting.net
Name: sql6495753
Username: sql6495753
Password: KLdC4PA9zU
Port number: 3306

## for developer

if you run index.py then its ask username and password.


For direct login use this:

username:-- user

password:-- user

## Download Executable File

https://drive.google.com/file/d/1-LExsWzuFhs99sKF2raQSdUZbukhA3NX/view?usp=sharing

After download this file move it into this github folder and run this executable file.

It will not work outside this folder so please first move this into this demo folder then run it.

## Document

https://drive.google.com/file/d/1vm4LqeFC0X8cGfSadA-fMirUTOHiSCVc/view?usp=sharing
