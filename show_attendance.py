from binascii import b2a_hqx
from email import header
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
import io
import tkinter
from tkmagicgrid import *
import ctypes  # An included library with Python install.   
import pyttsx3
import tkinter.messagebox as mbox

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

def thongke():
    window_thongke = Tk()
    # windo.iconbitmap("AMS.ico")
    window_thongke.title("window_thongke...")
    window_thongke.geometry("600x300")
    window_thongke.resizable(0, 0)
    window_thongke.configure(background="light blue")
    # window_thongke_logo = Image.open("UI_Image/0004.png")
    # window_thongke_logo = window_thongke_logo.resize((50, 47), Image.ANTIALIAS)
    # window_thongke_logo1 = ImageTk.PhotoImage(window_thongke_logo)
    titl = tk.Label(window_thongke, bg="light blue", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(window_thongke, image=window_thongke_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        window_thongke,
        text="Thống kê điểm danh",
        bg="light blue",
        fg="black",
        font=("arial", 25),
    )
    titl.place(x=150, y=12)

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Year,Month,Day=date.split("-")
    def count_solandiemdanh(list, id):
        count = 0
        count_1 = 0 
        count_2 = 0
        ten = ''
        for i in range (len(list)):
            if (list[i][0] == id):
                count+=1
                ten = list[i][1]
                if (list[i][4] == 'Come' and list[i][5] == 'True'):
                    count_1 +=1
                if (list[i][4] == 'Go' and list[i][5] == 'True'):
                    count_2 +=1
        return count, count_1, count_2, ten

    def xemtatca():
        root = tkinter.Tk()
        grid = MagicGrid(root)
        grid.pack(side="top", expand=1, fill="both")
        count = 0
        while True:
            cs = f"./Attendance/Attendance_{Year}-{Month}.csv"
            with io.open(cs, "r", newline="") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    grid.add_row(*row)
            count +=1
            if (count>=1):
                    break       

        root.mainloop()

    def xemthongke():
        Id = tx.get()
        if Id =="":
            t="Hãy điền id của bạn của bạn!!!"
            mbox.showwarning("Nofication", t)
        else: 
            thongkestatus = []
            
            new_csv = ['Id', 'Name', 'Attendence', 'Late', 'Overtime']
            count = 0
            while True:
                cs = f"./Attendance/Attendance_{Year}-{Month}.csv"
                with io.open(cs, "r", newline="") as csv_file:
                    reader = csv.reader(csv_file)

                    rows = []
                    for row in reader:
                        rows.append(row)
                    count, count_1, count_2, ten = count_solandiemdanh(rows, Id)
                    row = [Id, ten, count, count_1, count_2]
                    if (ten == ''):
                        mbox.showwarning("Warning", "Id isn't right!")
                    else:
                        root = tkinter.Tk()
                        grid = MagicGrid(root)
                        grid.pack(side="top", expand=1, fill="both")
                        grid.add_header(*new_csv)
                        grid.add_row(*row)
                        root.mainloop()
                count +=1
                if (count>=1):
                    break
            
    def xemdiemdanh():
        Id = tx.get()
        if Id =="":
            t="Hãy điền id của bạn của bạn!!!"
            mbox.showinfo("Nofication", t)
        else: 
            count = 0
            while True:
                cs = f"./Attendance/Attendance_{Year}-{Month}.csv"
                with io.open(cs, "r", newline="") as csv_file:
                    reader = csv.reader(csv_file)
                    header = []
                    header = next(reader)
                    rows = []
                    for row in reader:
                        if row[0] == Id:
                            rows.append(row)

                    if len(rows) == 0:
                        mbox.showwarning("Warning", "Id isn't there!")
                    else:
                        root = tkinter.Tk()
                        grid = MagicGrid(root)
                        grid.pack(side="top", expand=1, fill="both")
                        grid.add_header(*header)
                        for row in rows:
                            grid.add_row(*row)
                        root.mainloop()
                count +=1
                if (count>=1):
                    break

    xtc = tk.Button(
        window_thongke,
        text="Xem tất cả",
        command=xemtatca,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    xtc.place(x=20, y=200)

    attf = tk.Button(
        window_thongke,
        text="Xem điểm danh",
        command=xemdiemdanh,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    attf.place(x=350, y=200)

    sub = tk.Label(
        window_thongke,
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

    tx = tk.Entry(
        window_thongke,
        width=15,
        bd=5,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        window_thongke,
        text="Thống kê",
        command=xemthongke,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=10,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=200)
    window_thongke.mainloop()

    # def calculate_attendance():
    #     print("hehe")


            