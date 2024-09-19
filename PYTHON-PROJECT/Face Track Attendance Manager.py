import os
import tkinter
from tkinter import *
from time import strftime
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from student import students
from train import Train_data
from face_rec import face_recognize
from attendance import attendance_sys
from developer import Developer_info
from help_disk import Help_disk


class FaceTrack_Attendance_Manager:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("FaceTrack Attendance Manager")
        self.root.wm_iconbitmap("face.ico")


        # upper image
        img = Image.open(r'C:\Users\PMLS\Desktop\images_project\img.jpg')
        img = img.resize((1285, 170), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = tkinter.Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1285, height=170)

        # background image
        img_1 = Image.open(r'C:\Users\PMLS\Desktop\images_project\background_1.jpg')
        img_1 = img_1.resize((1285, 500), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        bg_img = tkinter.Label(self.root, image=self.photoimg_1)
        bg_img.place(x=0, y=170, width=1285, height=500)
        # label

        title_lbl = tkinter.Label(bg_img, text="FaceTrack Attendance Manager", font=("times new roman", 25, "bold"),
                                  bg="navy blue", fg="white")
        title_lbl.place(x=0, y=0, width=1285, height=45)

        # ========================= current time =================
        def time():
            string = strftime('%H:%M:%S %p')
            label_1.config(text=string)
            label_1.after(1000, time)

        label_1 = tkinter.Label(title_lbl, font=("tines new roman", 14, 'bold'), background="navy blue", foreground='white')
        label_1.place(x=2, y=0, width=120, height=40)
        time()

        # student button
        img_2 = Image.open(r'C:\Users\PMLS\Desktop\images_project\student.png')
        img_2 = img_2.resize((140, 140), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        button_1 = tkinter.Button(bg_img, image=self.photoimg_2, command=self.student_details, cursor="hand2")
        button_1.place(x=255, y=80, width=140, height=140)

        button_1 = tkinter.Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_1.place(x=255, y=221, width=140, height=30)

        # face detection button
        img_3 = Image.open(r'C:\Users\PMLS\Desktop\images_project\face-scanner.png')
        img_3 = img_3.resize((140, 140), Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        button_2 = tkinter.Button(bg_img, image=self.photoimg_3, command=self.face_recognition, cursor="hand2")
        button_2.place(x=465, y=80, width=140, height=140)

        button_2 = tkinter.Button(bg_img, text="Face Detection", command=self.face_recognition, cursor="hand2",
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_2.place(x=465, y=221, width=140, height=30)

        # Attendance Details button
        img_4 = Image.open(r'C:\Users\PMLS\Desktop\images_project\attendance.png')
        img_4 = img_4.resize((140, 140), Image.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        button_4 = tkinter.Button(bg_img, image=self.photoimg_4, cursor="hand2", command=self.attendance_data, )
        button_4.place(x=665, y=80, width=140, height=140)

        button_4 = tkinter.Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data,
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_4.place(x=665, y=221, width=140, height=30)

        # Help desk button
        img_5 = Image.open(r'C:\Users\PMLS\Desktop\images_project\help.png')
        img_5 = img_5.resize((140, 140), Image.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        button_5 = tkinter.Button(bg_img, command=self.help_dsk, image=self.photoimg_5, cursor="hand2")
        button_5.place(x=865, y=80, width=140, height=140)

        button_5 = tkinter.Button(bg_img, command=self.help_dsk, text="Help Desk", cursor="hand2",
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_5.place(x=865, y=221, width=140, height=30)

        # Train Data button
        img_6 = Image.open(r'C:\Users\PMLS\Desktop\images_project\train.png')
        img_6 = img_6.resize((140, 140), Image.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        button_6 = tkinter.Button(bg_img, image=self.photoimg_6, cursor="hand2", command=self.train_data)
        button_6.place(x=255, y=280, width=140, height=140)

        button_6 = tkinter.Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_6.place(x=255, y=421, width=140, height=30)

        # photos button
        img_7 = Image.open(r'C:\Users\PMLS\Desktop\images_project\photos.png')
        img_7 = img_7.resize((140, 140), Image.LANCZOS)
        self.photoimg_7 = ImageTk.PhotoImage(img_7)

        button_7 = tkinter.Button(bg_img, image=self.photoimg_7, cursor="hand2", command=self.open_image,)
        button_7.place(x=465, y=280, width=140, height=140)

        button_7 = tkinter.Button(bg_img, text="photos", cursor="hand2", command=self.open_image,
                                  font=("times new roman", 15, "bold"),bg="navy blue", fg="white")
        button_7.place(x=465, y=421, width=140, height=30)

        # developer button
        img_9 = Image.open(r'C:\Users\PMLS\Desktop\images_project\developer.png')
        img_9 = img_9.resize((140, 140), Image.LANCZOS)
        self.photoimg_9 = ImageTk.PhotoImage(img_9)

        button_9 = tkinter.Button(bg_img, command=self.developer_data, image=self.photoimg_9, cursor="hand2")
        button_9.place(x=665, y=280, width=140, height=140)

        button_9 = tkinter.Button(bg_img, command=self.developer_data, text="Developer", cursor="hand2",
                                  font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_9.place(x=665, y=421, width=140, height=30)

        # Exit button
        img_10 = Image.open(r'C:\Users\PMLS\Desktop\images_project\exit.png')
        img_10 = img_10.resize((140, 140), Image.LANCZOS)
        self.photoimg_10 = ImageTk.PhotoImage(img_10)

        button_10 = tkinter.Button(bg_img, command=self.exit_window, image=self.photoimg_10, cursor="hand2")
        button_10.place(x=865, y=280, width=140, height=140)

        button_10 = tkinter.Button(bg_img, command=self.exit_window, text="Exit", cursor="hand2",
                                   font=("times new roman", 15, "bold"), bg="navy blue", fg="white")
        button_10.place(x=865, y=421, width=140, height=30)

        # ================ functions of all buttons =====================


    # photos club
    def open_image(self):
        os.startfile("data_capture")

    # ================ exit button ======================
    def exit_window(self):
        self.exit_window = tkinter.messagebox.askyesno("Exit", "Are your sure to exit", parent=self.root)
        if self.exit_window > 0:
            self.root.destroy()
        else:
            return

    # student details
    def student_details(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = students(self.new_window)

    # train data button
    def train_data(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = Train_data(self.new_window)

    # train data button
    def face_recognition(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = face_recognize(self.new_window)


    # attendance data
    def attendance_data(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = attendance_sys(self.new_window)

    # Developer details
    def developer_data(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = Developer_info(self.new_window)

    # Developer details
    def help_dsk(self):
        self.new_window = tkinter.Toplevel(self.root)
        self.app = Help_disk(self.new_window)


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = FaceTrack_Attendance_Manager(root)
    root.mainloop()
