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

path = str("./TrainingImage/")
imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
#create empth face list
faces=[]
#create empty ID list
Ids=[]

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
    print(Id)
    Ids.append(Id)
print(Ids)