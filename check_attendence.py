from asyncore import write
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
from csv import DictWriter

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
Year,Month,Day = date.split('-')

def check_attendence(attendance):      
    text = ''
    count = 1
    iswork = False
    col_names = attendance.columns
    attendance = attendance.values
    if len(attendance!= 0):
        while True: 
            filename = ".\Attendance\Attendance_"+Year+"-"+Month+".csv"
            check_data = pd.read_csv(".\Attendance\Attendance_"+Year+"-"+Month+".csv")
            check_data = check_data[check_data['Day'] == int(Day)]
            # if attendance[0][0] == "Unknown" or  attendance[0][0] == '':
            #     text = "Unknown"
            #     iswork = False
            #     break
            check = check_data[check_data.Id == attendance[0][0]]
            duocdiemdanh = False
            
            if (len(check) == 0):
                attendance[0][5] = 'Come'
                time = attendance[0][4]
                Hour,Minute,Second=time.split(":")
                if (int(Hour) > 7):
                    attendance[0][6] = True
                attendance = {'Id':attendance[0][0], 'Name':attendance[0][1],'Month':attendance[0][2], 'Day':attendance[0][3],
                'Time':attendance[0][4], 'Status':attendance[0][5],'IsLate':attendance[0][6]}

                with open(f".\Attendance\Attendance_{Year}-{Month}.csv", 'a') as f:
                    writer_object = DictWriter(f ,fieldnames=col_names)
                    writer_object.writerow(attendance)
                    f.close()
                text = 'Welcome to work!'
                iswork = True

            elif (len(check) == 1):
                attendance[0][5] = 'Go'
                time = attendance[0][4]
                Hour,Minute,Second=time.split(":")
                if (int(Hour) > 17):
                    attendance[0][6] = True
                hehe = check.Time.values
                time = hehe[0]
                Hour_1,Minute_1,Second=time.split(":")
                
                if int(Hour_1) < int(Hour) :
                    duocdiemdanh = True
                    iswork = True
                elif int(Hour_1) == int(Hour):
                    if (int(Minute) - int(Minute_1)) < 10:
                        text = 'you just finished taking attendance'
                    else:
                        iswork = True
                        duocdiemdanh = True
                if duocdiemdanh == True: 
                    attendance = {'Id':attendance[0][0], 'Name':attendance[0][1],'Month':attendance[0][2], 'Day':attendance[0][3], 
                    'Time':attendance[0][4], 'Status':attendance[0][5],'IsLate':attendance[0][6]}

                    with open(f".\Attendance\Attendance_{Year}-{Month}.csv", 'a') as f:
                        writer_object = DictWriter(f ,fieldnames=col_names)
                        writer_object.writerow(attendance)
                        f.close()
                    text = 'Good bye!'
            else:
                text = 'Too much attendence for today'
            count +=1
            if (count > 1):
                break
    else:
        text = 'Unknown'
        iswork = False
    return text, iswork