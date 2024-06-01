# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

root=tk.Tk()

root.title("Sign Language Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# bg = Image.open(r"E:/carrier_choice_prediction/y9.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("s1.mp4", video_label,loop = 1, size = (w, h))
player.play()

w = tk.Label(root, text="SIGN LANGUAGE DETECTION ",width=100,background="black",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")


from tkinter import messagebox as ms


def login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])







d2=tk.Button(root,text="LOGIN",command=login,bg="blue",width=9,height=1,bd=0,foreground="#030303",font=("times new roman",17,"bold"))
d2.place(x=1050,y=10)


d3=tk.Button(root,text="  REGISTER",command=Register,width=10,height=1,bd=0,bg="green",foreground="#030303",font=("times new roman",17,"bold"))
d3.place(x=1200,y=10)



root.mainloop()
