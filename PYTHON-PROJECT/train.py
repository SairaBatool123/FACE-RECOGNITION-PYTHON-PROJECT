import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train_data:
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
        train_lbl = tkinter.Label(bg_img, text="Train Data Set",
                                  font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl.place(x=0, y=10, width=1285, height=60)

        # label_2 back
        train_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl_2.place(x=0, y=258, width=1285, height=80)

        # label_2 back
        train_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl_2.place(x=0, y=420, width=1285, height=80)

        # label_2
        train_lbl_1 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="navy blue", fg="white")
        train_lbl_1.place(x=480, y=258, width=190, height=80)

        # label_2 button
        train_lbl_2 = tkinter.Button(bg_img, text="", command=self.train_classifier,
                                     font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        train_lbl_2.place(x=0, y=340, width=1285, height=80)

        # label_2 button
        train_lbl_1 = tkinter.Button(bg_img, text="Train", command=self.train_classifier, cursor="hand2",
                                     font=("times new roman", 30, "bold"), bg="red", fg="white")
        train_lbl_1.place(x=570, y=340, width=120, height=80)

        # label_2
        train_lbl_1 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="navy blue", fg="white")
        train_lbl_1.place(x=650, y=420, width=190, height=80)


    def train_classifier(self):
        data_dir = "data_capture"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            image_np = np.array(img, 'uint8')
            img_id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(img_id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier and save it
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training completed!")



if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Train_data(root)
    root.mainloop()
