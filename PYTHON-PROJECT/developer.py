from tkinter import*
import tkinter
from tkinter import ttk, RIDGE, W, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, X, Y, BOTH, END
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import os
from tkinter import filedialog

class Developer_info:
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
        train_lbl = tkinter.Label(bg_img, text="About Developers",
                                  font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl.place(x=0, y=10, width=1285, height=60)

        # Developer Info zahir shah
        dev_info_lbl = tkinter.Label(bg_img, text="Name: Zahir Shah      \n"
                                                  "Department: CS          \n"
                                                  "Semester: 2nd              \n"
                                                  "Skill: Python                ",
                                  font=("times new roman", 28, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=250, y=150)

        # Developer Info zakia gulam hussain
        dev_info_lbl = tkinter.Label(bg_img, text="Name: Zakia               \n"
                                                  "Department: CS          \n"
                                                  "Semester: 2nd              \n"
                                                  "Skill: Python                ",
                                  font=("times new roman", 28, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=250, y=350)

        # Developer Info saira batool
        dev_info_lbl = tkinter.Label(bg_img, text="Name: Saira Batool     \n"
                                                  "Department: CS          \n"
                                                  "Semester: 2nd              \n"
                                                  "Skill: Python                ",
                                  font=("times new roman", 28, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=650, y=150)

        # Developer Info areeba jameel
        dev_info_lbl = tkinter.Label(bg_img, text="Name: Areeba Jameel\n"
                                                  "Department: CS          \n"
                                                  "Semester: 2nd              \n"
                                                  "Skill: Python                ",
                                     font=("times new roman", 28, "bold"), bg="white", fg="navy blue")
        dev_info_lbl.place(x=650, y=350)


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Developer_info(root)
    root.mainloop()
