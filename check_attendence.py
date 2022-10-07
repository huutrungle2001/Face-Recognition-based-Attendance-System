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
    col_names = attendance.columns
    attendance = attendance.values
    while True: 
        filename = f".\Attendance\Attendance_{Year}-{Month}.csv"
        check_data = pd.read_csv(filename)
        check_data = check_data[check_data['Day'] == int(Day)]
        check = check_data[check_data.Id == attendance[0][0]]

        if (len(check) == 0):
            attendance[0][4] = 'Come'
            time = attendance[0][3]
            Hour,Minute,Second=time.split(":")
            if (int(Hour) > 7):
                attendance[0][5] = True
            attendance = {'Id':attendance[0][0], 'Name':attendance[0][1],'Day':attendance[0][2], 
            'Time':attendance[0][3], 'Status':attendance[0][4],'IsLate':attendance[0][5],}

            with open(f".\Attendance\Attendance_{Year}-{Month}.csv", 'a') as f:
                writer_object = DictWriter(f ,fieldnames=col_names)
                writer_object.writerow(attendance)
                f.close()
            text = 'Welcome to work!'
    
        elif (len(check) == 1):
            attendance[0][4] = 'Go'
            time = attendance[0][3]
            Hour,Minute,Second=time.split(":")
            if (int(Hour) > 17):
                attendance[0][5] = True
            hehe = check.Time.values
            time = hehe[0]
            Hour_1,Minute_1,Second=time.split(":")
            duocdiemdanh = False
            if int(Hour_1) < int(Hour) :
                duocdiemdanh = True
            elif int(Hour_1) == int(Hour):
                if (int(Minute) - int(Minute_1)) < 10:
                    text = 'you just finished taking attendance'
                else:
                    duocdiemdanh = True
            if duocdiemdanh == True: 
                attendance = {'Id':attendance[0][0], 'Name':attendance[0][1],'Day':attendance[0][2], 
                'Time':attendance[0][3], 'Status':attendance[0][4],'IsLate':attendance[0][5],}

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
    return text