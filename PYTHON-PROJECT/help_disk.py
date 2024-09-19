from tkinter import*
import tkinter
from tkinter import ttk, RIDGE, W, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, X, Y, BOTH, END
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import os
from tkinter import filedialog

class Help_disk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FaceTrack Attendance Manager")
        self.root.wm_iconbitmap("face.ico")

        # background image
        img_2 = Image.open(r'C:\Users\PMLS\Desktop\images_project\train_bg.jpg')
        img_2 = img_2.resize((1290, 680))
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        bg_img = tkinter.Label(self.root, image=self.photoimg_2)
        bg_img.place(x=0, y=0, width=1290, height=680)

        # label_1
        train_lbl = tkinter.Label(bg_img, text="Happy To Help You",
                                  font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl.place(x=0, y=10, width=1285, height=60)

        # about project
        dev_info_lbl = tkinter.Label(bg_img, text="A desktop app for managing student attendance using face detection\n"
                                                  "is a software application designed to streamline the process of \n"
                                                  "marking attendance in educational institutions. It utilizes facial\n"
                                                  " recognition technology to identify and record the presence of\n"
                                                  "students during classes or events. The app typically includes\n"
                                                  "features for face detection, attendance logging, database\n"
                                                  "management, a user-friendly interface, notification systems,\n"
                                                  "data security, and the option to generate attendance reports and\n "
                                                  "analytics. This technology aims to simplify attendance management,\n"
                                                  " reduce manual efforts, and enhance accuracy in tracking student\n "
                                                  "attendance, ultimately benefiting both educators and students. ",
                                     font=("times new roman", 20, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=250, y=150)

        dev_info_lbl = tkinter.Label(bg_img, text=": zahirshah@gmail.com\n"
                                                  ": 03334455349               ",
                                     font=("times new roman", 20, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=450, y=510)














if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Help_disk(root)
    root.mainloop()