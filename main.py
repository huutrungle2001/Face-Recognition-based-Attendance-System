from binascii import b2a_hqx
from fileinput import filename
from tkinter import *
import tkinter as tk
from turtle import left
import datetime as dt
from tkinter import messagebox
from time import strftime
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import show_attendance
import pyttsx3
import tkinter.messagebox as mbox
import io
from login import login_screen
from check_attendence import check_attendence

def main_begin():
    def login():
        window.destroy()
        login_screen()

    
    def Attendence():
        attendance_window = Tk()
        attendance_window.title("Hệ thống điểm danh")
        attendance_window.geometry('500x600')
        attendance_window.configure(background="orange")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Day','Time','Status','IsLate']
        attendance = pd.DataFrame(columns = col_names)   
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                            
                if(conf < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    Year,Month,Day = date.split('-')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+aa
                    Status = None
                    IsLate = False
                    attendance.loc[len(attendance)] = [Id,aa,Day,timeStamp,Status,IsLate]
    
                else:
                    Id='Unknown'                
                    tt=str(Id)  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im)
            if (cv2.waitKey(1)==ord('q')):
                break
        
        cam.release()
        cv2.destroyAllWindows()
        # #print(attendance)
        # res=attendance
        # mbox.showinfo("Information", res)
        attendance_window.mainloop()
        return attendance

    def check():
        attendance = Attendence()
        text = check_attendence(attendance)
        mbox.showinfo("Nofication", text)
    data_user = []

    window = Tk()
    window.title("Hệ thống điểm danh")
    window.geometry('500x600')
    window.configure(background="orange")

    bg_window = Image.open("IconImage/1.jpg")
    photo =  ImageTk.PhotoImage(bg_window)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand="yes")

    frame = Frame(window, width= "400", bg="black", height="500", relief="solid", borderwidth=2)

    frame.place(x = 50, y = 50)

    sign_in_image = Image.open('./IconImage/hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(frame, image=photo, bg='#040405')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=125, y=50)

    def text_to_speech(user_text):
        engine = pyttsx3.init()
        engine.say(user_text)
        engine.runAndWait()

    def my_time():
        time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 
        ts = time.time()

        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        if  Hour == "07" and Minute == "00" and Second == "00":
            text_to_speech("Start to work now!")
        elif  Hour == "17" and Minute == "00" and Second == "00":
            text_to_speech("Start to work now!")
        
    my_font=("yu gothic ui", 13, "bold") # display size and style

    l1=tk.Label(frame,font=my_font,bg='black',fg='white')
    l1.place(x=10, y=10)
    # l1.grid(row=1,column=1,padx=5,pady=25)

    my_time()

    framelgn_button = Image.open('./IconImage/btn1.png')
    photo = ImageTk.PhotoImage(framelgn_button)
    framelgn_button_label = Label(frame, image=photo, bg='#040405')
    framelgn_button_label.image = photo
    framelgn_button_label.place(x=46, y=200)
    framelogin = Button(framelgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=login)
    framelogin.place(x=20, y=10)

    framelgn_button_label_1 = Label(frame, image=photo, bg='#040405')
    framelgn_button_label_1.image = photo
    framelgn_button_label_1.place(x=46, y=270)
    frameattendence= Button(framelgn_button_label_1, text='ATTENDENCE', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=check)
    frameattendence.place(x=20, y=10)

    forgot_button = Label(frame, text="*Login for admin only",
                                font=("yu gothic ui", 13, "italic underline"), fg="white", relief=FLAT,
                                activebackground="#040405"
                                , borderwidth=0, background="#040405")
    forgot_button.place(x=100, y=350)

    image = Image.open("IconImage/4.png")

    resize_image = image.resize((40, 40))

    img = ImageTk.PhotoImage(resize_image)  

    button = Button(frame, command=window.destroy, text='OUT',fg = 'white',  font=('times',14,'bold'), image = img, borderwidth=0, bg ='#040405', compound = TOP)
    button.place(x=300, y=410)

    window.mainloop()

    return window

main_begin()