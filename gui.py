from ast import Try
from binascii import b2a_hqx
import PyPDF2
from tkinter import *
from tkinter import filedialog
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
from tkPDFViewer import tkPDFViewer as pdf
import os   
import tkinter.messagebox as mbox
import glob
import io

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


def openmain(data_user, login_old_window):

    window = Toplevel()
    window.title("Hệ thống điểm danh")
    window.geometry('1000x700')
    window.configure(background="orange")

    bg_window = Image.open("IconImage/admin-back.png")
    photo =  ImageTk.PhotoImage(bg_window)
    bg_panel = tk.Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand="yes")



    frame = Frame(window, bg="white", width= "900", height="600")
    frame.place(x = 50, y = 30)

    #==========================================================================================>
    frame_1 = Frame(frame, width= "900", bg="white", height="70", relief="solid", borderwidth=2)

    frame_1.place(x = 0, y = 0)

    a = tk.Label(
        frame_1,
        text=f"Chào mừng {data_user[1]} đến với phần mềm điểm danh của chúng tôi",
        bg="white",
        fg="black",
        font=("times", 14, 'bold'), borderwidth=2
    )
    a.place(x=280, y=20)

    time_to_attendence = ['07', '00', '00', '17', '0', '0']


    def my_time():
        time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 
        ts = time.time()

        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        if  Hour == time_to_attendence[0] and Minute == time_to_attendence[1] and Second == time_to_attendence[2]:
            text_to_speech("Start to work now!")
        elif  Hour == time_to_attendence[0] and Minute == time_to_attendence[0] and Second == time_to_attendence[0]:
            text_to_speech("Start to work now!")
        
    my_font=('times',12,'bold') # display size and style

    l1=tk.Label(frame_1,font=my_font,bg='white')
    l1.place(x=0, y=0)
    # l1.grid(row=1,column=1,padx=5,pady=25)

    my_time()

    image = Image.open("IconImage/logo.png")

    resize_image = image.resize((40, 40))

    img = ImageTk.PhotoImage(resize_image)  

    lb = tk.Label(frame_1, image = img, bg = 'white')
    lb.image = img
    lb.place(x = 830, y = 10)

    #==========================================================================================>



    def delete_employee():
        win_delete = Tk()
        # windo.iconbitmap("AMS.ico")
        win_delete.title("Chỉnh thời gian ra vào")
        win_delete.geometry("600x300")
        win_delete.resizable(0, 0)
        win_delete.configure(background="light blue")
        
        def xoa():
            id = tx.get()
            if (id == ''):
                t="Hãy điền id của bạn của bạn!!!"
                mbox.showwarning("Nofication", t)
            else: 
                count = 0
                done = False
                ishave = False
                cs = f"./StudentDetails/StudentDetails.csv"
                with io.open(cs, "r", newline="",encoding='utf8') as csv_file:
                    data = csv.reader(csv_file)
                    for row in data:
                        if (row[0] == id):

                            ishave = True

                if (ishave == True):
                    while True:
                        data = pd.read_csv('./StudentDetails/EmployeerAccount.csv')
                        data = data[data.Id != int(id)]
                        os.makedirs('./StudentDetails/', exist_ok=True)  
                        data.to_csv('./StudentDetails/EmployeerAccount.csv', index=False) 

                        data = pd.read_csv('./StudentDetails/StudentDetails.csv')
                        data = data[data.Id != int(id)]
                        os.makedirs('./StudentDetails/', exist_ok=True)  
                        data.to_csv('./StudentDetails/StudentDetails.csv', index=False)
              
                        folder_path = (r'./TrainingImage/')
                        #using listdir() method to list the files of the folder
                        test = os.listdir(folder_path)
                        #taking a loop to remove all the images
                        #using ".png" extension to remove only png images
                        #using os.remove() method to remove the files
                        for images in test:
                            if images.startswith(f' {id}'):
                                os.remove(os.path.join(folder_path, images))

                        done = True
                        
                        count +=1
                        if (count>=1):
                                break
                    if done == True :
                        mbox.showinfo("Thành công", 'Đã xóa thành công')
                    else:
                        mbox.showerror("Lỗi", "Xóa không thành công")
                else:
                    mbox.showerror("Lỗi", "Id không có trong danh sách nhân viên")

        tx = tk.Entry(
            win_delete,
            width=15,
            bd=5,
            bg="black",
            fg="white",
            relief=RIDGE,
            font=("times", 30, "bold")
            )
        tx.place(x=190, y=100)

        sub = tk.Label(
            win_delete,
            text="ID",
            width=10,
            height=2,
            bg="black",
            fg="white",
            bd=5,
            relief=RIDGE,
            font=("times new roman", 15),
        )
        sub.place(x=50, y=100)
        fill_a = tk.Button(
            win_delete,
            text="Xóa",
            command=xoa,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="white",
            height=2,
            width=10,
            relief=RIDGE,
        )
        fill_a.place(x=195, y=200)

        win_delete.mainloop()


    def show_thongke():
        show_attendance.thongke()
    #==========================================================================================>
    def clear():
        txt.delete(0, 'end')    
        res = ""
        message.configure(text= res)

    def clear2():
        txt2.delete(0, 'end')    
        res = ""
        message.configure(text= res)    

    def clear3():
        txt4.delete(0, 'end')    
        res = ""
        message.configure(text= res)  

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False
    #==========================================================================================>

    def support():
        win= Tk()
        #Set the Geometry
        win.geometry("750x450")
        #Create a Text Box
        text= Text(win,width= 80,height=30)
        text.pack(pady=20)
        #Open the PDF File
        pdf_file= PyPDF2.PdfFileReader("ReadPDF/1.pdf")
        #Select a Page to read
        page= pdf_file.getPage(0)
        #Get the content of the Page
        content=page.extractText()
        #Add the content to TextBox
        text.insert(1.0,content)
        win.mainloop()

    #==========================================================================================>

    def TakeImages():        
        Id=(txt.get())
        name=txt2.get()
        thongtin = txt4.get()
        if(is_number(Id)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+ Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Ảnh lưu với ID : " + Id
            row = [Id , str(name), thongtin]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile, lineterminator='\n')
                writer.writerow(row)
            csvFile.close()
            message.configure(text= res)
        else:
            if(is_number(Id) == False):
                res = "Điền tên với chữ cái"
                message.configure(text= res)
            # if(name.isalpha()):
            #     res = "ID phải là số tự nhiên"
            #     message.configure(text= res)
        
    def TrainImages():
        recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = getImagesAndLabels("./TrainingImage/")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel/Trainner.yml")
        print( str(Id[0]) + "hehe")
        res = "Ảnh đã train"#+",".join(str(f) for f in Id)
        message.configure(text= res)

    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths)
        
        #create empth face list
        faces=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            print(imagePath)
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[0])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)    
        return faces,Ids
    #==========================================================================================>
    #==========================================================================================>
    frame_2 = Frame(frame, width= "100", bg="white", height="530", relief="solid", borderwidth=2)

    frame_2.place(x = 0, y = 70)
    # def helloCallBack():
    #    msg = messagebox.showinfo( "Hello Python", "Hello World")

    # B = Button(frame_2, text = "Hello", command = helloCallBack)
    # B.place(x = 0,y = 0)
    image = Image.open("IconImage/1.png")

    resize_image = image.resize((40, 40))

    img = ImageTk.PhotoImage(resize_image)  

    button_1 = Button(frame_2, text = '  Đăng ký  ', font=('times',12,'bold'), image = img, compound = TOP, bg ='white', borderwidth=0)
    button_1.place(x = 8, y = 10)

    image_3 = Image.open("IconImage/3.png")

    resize_image_3 = image_3.resize((40, 40))

    img_3 = ImageTk.PhotoImage(resize_image_3)  

    button_3 = Button(frame_2, command= show_thongke, text = ' Thống kê ', font=('times',12,'bold'), image = img_3, compound = TOP, bg ='white', borderwidth=0)
    button_3.place(x = 8, y = 110)

    image_4 = Image.open("IconImage/delete.png")

    resize_image_4 = image_4.resize((40, 40))

    img_4 = ImageTk.PhotoImage(resize_image_4)  

    button_4= Button(frame_2, text = '     Xóa     ', command= delete_employee, font=('times',12,'bold'), image = img_4, compound = TOP, bg ='white', borderwidth=0)
    button_4.place(x = 8, y = 210)

    image_5 = Image.open("IconImage/5.png")

    resize_image_5 = image_5.resize((40, 40))

    img_5 = ImageTk.PhotoImage(resize_image_5)  

    button_5 = Button(frame_2, text = '    Hỗ trợ   ', font=('times',12,'bold'), image = img_5, compound = TOP, bg ='white', borderwidth=0, command=support)
    button_5.place(x = 8, y = 310)


    def dangxuat():
        window.destroy()
        login_old_window.deiconify()

    image_6 = Image.open("IconImage/4.png")

    resize_image_6 = image_6.resize((40, 40))

    img_6 = ImageTk.PhotoImage(resize_image_6)  

    button_6 = Button(frame_2, command=dangxuat, text = ' Đăng xuất ', font=('times',12,'bold'), image = img_6, compound = TOP, bg ='white', borderwidth=0)

    button_6.place(x = 8, y = 410)
    #==========================================================================================>
    frame_3 = Frame(frame, width= "800", bg="light blue", height="530", relief="solid", borderwidth=2)

    frame_3.place(x = 100, y = 70)


    lbl = tk.Label(frame_3, text="ID",width=15  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=100, y=15)

    txt = tk.Entry(frame_3,width=15   ,bg="white" ,fg="black",font=('times', 15, ' bold '))
    txt.place(x=300, y=15, height=50)

    lbl2 = tk.Label(frame_3, text="Họ và tên",width=15  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=100, y=100)

    txt2 = tk.Entry(frame_3,width=15  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
    txt2.place(x=300, y=100, height=50)

    lbl4 = tk.Label(frame_3, text="Thông tin",width=15  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl4.place(x=100, y=185)

    txt4 = tk.Entry(frame_3,width=15  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
    txt4.place(x=300, y=185, height=50)

    lbl3 = tk.Label(frame_3, text="Thông báo : ",width=15  ,fg="black"  ,bg="white"  ,height=2 ,font=('times', 15, ' bold underline ')) 
    lbl3.place(x=100, y=270)

    message = tk.Label(frame_3, text="" ,bg="white"  ,fg="black"  ,width=32  ,height=2, activebackground = "blue" ,font=('times', 15, ' bold ')) 
    message.place(x=300, y=270)


    clearButton = tk.Button(frame_3, text="Xóa", command=clear  ,fg="black"  ,bg="white"  ,width=15  ,height=1 ,activebackground = "blue" ,font=('times', 15, ' bold '))
    clearButton.place(x=500, y=15)
    clearButton2 = tk.Button(frame_3, text="Xóa", command=clear2  ,fg="black"  ,bg="white"  ,width=15  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
    clearButton2.place(x=500, y=100)  
    clearButton3 = tk.Button(frame_3, text="Xóa", command=clear3  ,fg="black"  ,bg="white"  ,width=15  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
    clearButton3.place(x=500, y=185)
    takeImg = tk.Button(frame_3, text="Chụp ảnh", command=TakeImages  ,fg="black"  ,bg="white"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
    takeImg.place(x=200, y=355)
    trainImg = tk.Button(frame_3, text="Train Images", command=TrainImages  ,fg="black"  ,bg="white"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
    trainImg.place(x=400, y=355)
    #==========================================================================================>
    window.mainloop()

