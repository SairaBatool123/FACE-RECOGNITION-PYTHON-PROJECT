import tkinter
import csv
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class face_recognize:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FaceTrack Attendance Manager")
        self.root.wm_iconbitmap("face.ico")

        # background image
        img_1 = Image.open(r'C:\Users\PMLS\Desktop\images_project\train_bg.jpg')
        img_1 = img_1.resize((1290, 680))
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        bg_img = tkinter.Label(self.root, image=self.photoimg_1)
        bg_img.place(x=0, y=0, width=1290, height=680)

        # label_1
        face_recognize_lbl = tkinter.Label(bg_img, text="Face Recognization", font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        face_recognize_lbl.place(x=0, y=10, width=1280, height=60)

        # label_2 back
        face_recognize_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        face_recognize_lbl_2.place(x=0, y=258, width=1285, height=80)

        # label_2 back
        face_recognize_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        face_recognize_lbl_2.place(x=0, y=420, width=1285, height=80)

        # label_2
        face_recognize_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="navy blue", fg="white")
        face_recognize_lbl_2.place(x=420, y=258, width=190, height=80)

        # label_2 button
        face_recognize_button_1 = tkinter.Button(bg_img, text="", command=self.face_recog,
                                     font=("times new roman", 30, "bold"), bg="white", fg="navy blue")
        face_recognize_button_1.place(x=0, y=340, width=1285, height=80)

        # label_2 button
        face_recognize_button_1 = tkinter.Button(bg_img, text="Face Recognize", command=self.face_recog,
                                    cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        face_recognize_button_1.place(x=480, y=340, width=290, height=80)

        # label_2
        face_recognize_lbl_2 = tkinter.Label(bg_img, text="",
                                    font=("times new roman", 30, "bold"), bg="navy blue", fg="white")
        face_recognize_lbl_2.place(x=650, y=420, width=190, height=80)

    # =================== attendance management ===============
    def mark_attendance(self, n, i, d, s):
        with open("attend_file/attend.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.extend(entry[:3])  # Extend the name_list with the first three elements of each line

            if (n not in name_list) and (i not in name_list) and (d not in name_list) and (s not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{n}, {i}, {d}, {s}, {d1}, {dtString}, Present")
                print(f"Attendance marked for {n}")

    # ====================== face detection function =============

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                identity, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="zahirali1!",
                    database="face_recognizer"
                )

                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where studentID = " + str(identity))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select studentID from student where studentID = " + str(identity))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select dep from student where studentID = " + str(identity))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select sem from student where studentID = " + str(identity))
                s = my_cursor.fetchone()
                s = "+".join(s)

                if confidence > 77:
                    cv2.putText(img, f"Name: {n}", (x, y - 70),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                    cv2.putText(img, f"ID No: {i}", (x, y - 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                    cv2.putText(img, f"Semester: {s}", (x, y - 10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                    self.mark_attendance(n, i, d, s)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf_1, facade):
            coord = draw_boundary(img, facade, 1.1, 10, (255, 25, 255), "Face", clf_1)
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img_1 = video_cap.read()
            img_1 = recognize(img_1, clf, face_cascade)
            cv2.imshow("Welcome To Face Recognization", img_1)

            if cv2.waitKey(1) == 13:

                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = face_recognize(root)
    root.mainloop()
