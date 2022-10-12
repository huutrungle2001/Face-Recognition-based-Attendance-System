from binascii import b2a_hqx
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
from gui import openmain
def login_screen(old_window):
	data_user = []

	window = Toplevel()
	window.title("Hệ thống điểm danh")
	window.geometry('700x700')
	window.configure(background="#99FF66")

	bg_window = Image.open("IconImage/login-back.png")
	photo =  ImageTk.PhotoImage(bg_window)
	bg_panel = Label(window, image=photo)
	bg_panel.image = photo
	bg_panel.pack(fill='both', expand="yes")

	def show():
		hide_button = Button(frame, image=hide_image, command=hide, relief=FLAT,
									activebackground="white"
									, borderwidth=0, background="white", cursor="hand2")
		hide_button.place(x=510, y=350)
		password_entry.config(show='')

	def hide():
		show_button = Button(frame, image=show_image, command=show, relief=FLAT,
									activebackground="white"
									, borderwidth=0, background="white", cursor="hand2")
		show_button.place(x=540, y=350)
		password_entry.config(show='*')

	def login():
		user = username_entry.get()
		password = password_entry.get()
		if (user == "") and (password == ""):
			mbox.showerror("Error", "Bạn chưa điền mật khẩu và tên tài khoản")
		elif (user == "") and (password != ""):
			mbox.showerror("Error", "Bạn chưa điền tên tài khoản")
		elif (user != "") and (password == ""):
			mbox.showerror("Error", "Bạn chưa điền mật khẩu")
		else:
			valid = False
			cs = f"./StudentDetails/EmployeerAccount.csv"
			with io.open(cs, "r", newline="") as csv_file:
				data = csv.reader(csv_file)
				for row in data:
					user_data = row[0]
					password_data = row[2]
					if (user_data==user) and (password_data!=password):
						valid = True
						data_user = row
				if (valid == False):
					mbox.showerror("Error", "Sai mật khẩu hoặc tên tài khoản")
				else:
					mbox.showinfo("Information", "Đã đăng nhập được rồi nhé =))")
					username_entry.delete(0, 'end')
					password_entry.delete(0, 'end')
					window.withdraw()
					openmain(data_user, window)
					

	frame = Frame(window, width= "630", bg="#99FF66", height="600", relief="solid", borderwidth=2)

	frame.place(x = 35, y = 50)

	sign_in_image = Image.open('./IconImage/hyy.png')
	photo = ImageTk.PhotoImage(sign_in_image)
	sign_in_image_label = Label(frame, image=photo, bg='#99FF66')
	sign_in_image_label.image = photo
	sign_in_image_label.place(x=250, y=50)

	# ========================================================================
	# ============ Sign In label =============================================
	# ========================================================================
	sign_in_label = Label(frame, text="Sign In", bg="#99FF66", fg="black",
							font=("yu gothic ui", 17, "bold"))
	sign_in_label.place(x=280, y=160)


	username_label = Label(frame, text="Username", bg="#99FF66", fg="black",
								font=("yu gothic ui", 13, "bold"))
	username_label.place(x=170, y=220)

	username_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg="#99FF66", fg="black",
								font=("yu gothic ui ", 12, "bold"))
	username_entry.place(x=200, y=265, width=270)

	username_line = Canvas(frame, width=300, height=2.0, bg="black", highlightthickness=0)
	username_line.place(x=170, y=289)


	frameusername_icon = Image.open('./IconImage/username_icon.png')
	photo = ImageTk.PhotoImage(frameusername_icon)
	frameusername_icon_label = Label(frame, image=photo, bg='#99FF66')
	frameusername_icon_label.image = photo
	frameusername_icon_label.place(x=170, y=262)


	framelgn_button = Image.open('./IconImage/btn1.png')
	photo = ImageTk.PhotoImage(framelgn_button)
	framelgn_button_label = Label(frame, image=photo, bg='#99FF66')
	framelgn_button_label.image = photo
	framelgn_button_label.place(x=170, y=380)
	framelogin = Button(framelgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
						bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=login)
	framelogin.place(x=20, y=10)

	password_label = Label(frame, text="Password", bg="#99FF66", fg="black",
										font=("yu gothic ui", 13, "bold"))
	password_label.place(x=170, y=310)

	password_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg="#99FF66", fg="black",
							font=("yu gothic ui", 12, "bold"), show="*")
	password_entry.place(x=200, y=346, width=244)

	password_line = Canvas(frame, width=300, height=2.0, bg="black", highlightthickness=0)
	password_line.place(x=170, y=370)
	# ======== Password icon ================
	password_icon = Image.open('./IconImage/password_icon.png')
	photo = ImageTk.PhotoImage(password_icon)
	password_icon_label = Label(frame, image=photo, bg='#99FF66')
	password_icon_label.image = photo
	password_icon_label.place(x=170, y=344)
	# ========= show/hide password ==================================================================
	show_image = ImageTk.PhotoImage \
	(file='./IconImage/show.png')

	hide_image = ImageTk.PhotoImage \
	(file='./IconImage/hide.png')

	show_button = Button(frame, image=show_image, command=show, relief=FLAT,
							activebackground="white"
							, borderwidth=0, background="white", cursor="hand2")
	show_button.place(x=510, y=350)



	forgot_button = Button(frame, text="Forgot Password ?",
								font=("yu gothic ui", 13, "bold underline"), fg="black", relief=FLAT,
								activebackground="#040405"
								, borderwidth=0, background="#99FF66", cursor="hand2")
	forgot_button.place(x=245, y=440)
	# =========== Sign Up ==================================================
	sign_label = Label(frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
							relief=FLAT, borderwidth=0, background="#99FF66", fg='black')
	sign_label.place(x=200, y=490)

	signup_img = ImageTk.PhotoImage(file='./IconImage/register.png')
	signup_button_label = Button(frame, image=signup_img, bg='#98a65d', cursor="hand2",
									borderwidth=0, background="#99FF66", activebackground="#040405")
	signup_button_label.place(x=320, y=485, width=111, height=35)

	# =====================================================================
		
		
	def back():
		window.destroy()
		old_window.deiconify()

	image = Image.open("IconImage/4.png")
	resize_image = image.resize((40, 40))
	img = ImageTk.PhotoImage(resize_image)  
	button = Button(frame, command=back, text='Back',fg = 'black',  font=('times',14,'bold'), image = img, borderwidth=0, bg ='#99FF66', compound = TOP)
	button.place(x=500, y=500)
	
	mainloop()