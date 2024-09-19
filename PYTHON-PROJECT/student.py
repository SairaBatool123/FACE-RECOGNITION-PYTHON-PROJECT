import tkinter
from tkinter import ttk, RIDGE, W, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, X, Y, BOTH, END
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0") 
        self.root.title("FaceTrack Attendance Manager")
        self.root.wm_iconbitmap("face.ico")

        # ==========================variables===============

        self.var_dep = tkinter.StringVar()
        self.var_course = tkinter.StringVar()
        self.var_year = tkinter.StringVar()
        self.var_sem = tkinter.StringVar()
        self.var_studentID = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_division = tkinter.StringVar()
        self.var_roll_no = tkinter.StringVar()
        self.var_gender = tkinter.StringVar()
        self.var_dob = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_phone_no = tkinter.StringVar()
        self.var_address = tkinter.StringVar()
        self.var_teacher_name = tkinter.StringVar()

        # upper image
        img = Image.open(r'C:\Users\PMLS\Desktop\images_project\stud.jpg')
        img = img.resize((1285, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = tkinter.Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1285, height=200)

        # background image
        img_0 = Image.open(r'C:\Users\PMLS\Desktop\images_project\background_1.jpg')
        img_0 = img_0.resize((1285, 500), Image.LANCZOS)
        self.photoimg_0 = ImageTk.PhotoImage(img_0)

        bg_img = tkinter.Label(self.root, image=self.photoimg_0)
        bg_img.place(x=0, y=170, width=1285, height=500)

        # label
        page_2_lbl = tkinter.Label(bg_img, text="Students Details Manager", font=("times new roman", 25, "bold"),
                                   bg="navy blue", fg="white")
        page_2_lbl.place(x=0, y=0, width=1280, height=40)

        # main frame
        main_frame = tkinter.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=45, width=1265, height=435)

        # left label frame
        left_frame = tkinter.LabelFrame(main_frame, bd=2, bg="white")
        left_frame.place(x=5, y=5, width=600, height=424)

        # course Info
        course_frame = tkinter.LabelFrame(main_frame, bd=2, relief=RIDGE, text=" Course Information ",
                                          font=("times new roman", 12, "bold"))
        course_frame.place(x=9, y=7, width=590, height=120)

        # department label
        dep_label = tkinter.Label(course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=8)

        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "BBA", "Commerce")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # courses label
        course_label = tkinter.Label(course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=8)

        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),
                                    state="readonly")
        course_combo["values"] = ("Select Course", "ITC", "FOP", "Calculus", "Physics")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year label
        year_label = tkinter.Label(course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=8)

        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"),
                                  state="readonly")
        year_combo["values"] = ("Select Year", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester label
        sem_label = tkinter.Label(course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=8)

        sem_combo = ttk.Combobox(course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"),
                                 state="readonly")
        sem_combo["values"] = ("Select Semester", 1, 2, 3, 4)
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #  student details
        student_detail_frame = tkinter.LabelFrame(main_frame, bd=2, relief=RIDGE, text=" Student Details ",
                                                  font=("times new roman", 12, "bold"))
        student_detail_frame.place(x=9, y=130, width=590, height=295)

        # student ID
        student_id_label = tkinter.Label(student_detail_frame, text="Student ID:", font=("times new roman", 12, "bold"),
                                         bg="white")
        student_id_label.grid(row=0, column=0, padx=3)

        student_id_entry = ttk.Entry(student_detail_frame, textvariable=self.var_studentID, width=20,
                                     font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # student name
        student_name_label = tkinter.Label(student_detail_frame, text="Student Name:",
                                           font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=3)

        student_name_entry = ttk.Entry(student_detail_frame, textvariable=self.var_name, width=20,
                                       font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Class division
        class_div_label = tkinter.Label(student_detail_frame, text="Division:", font=("times new roman", 12, "bold"),
                                        bg="white")
        class_div_label.grid(row=1, column=0, padx=3)

        class_div_combo = ttk.Combobox(student_detail_frame, textvariable=self.var_division, width=18,
                                       font=("times new roman", 12, "bold"), state="readonly")
        class_div_combo["values"] = ("Select Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # roll number
        roll_no_label = tkinter.Label(student_detail_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                                      bg="white")
        roll_no_label.grid(row=1, column=2, padx=3)

        roll_no_entry = ttk.Entry(student_detail_frame, textvariable=self.var_roll_no, width=20,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Gender
        gender_label = tkinter.Label(student_detail_frame, text="Gender:", font=("times new roman", 12, "bold"),
                                     bg="white")
        gender_label.grid(row=2, column=0, padx=3)

        gender_combo = ttk.Combobox(student_detail_frame, textvariable=self.var_gender, width=18,
                                    font=("times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # date of birth
        d_o_b_label = tkinter.Label(student_detail_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        d_o_b_label.grid(row=2, column=2, padx=3)

        d_o_b_entry = ttk.Entry(student_detail_frame, textvariable=self.var_dob, width=20,
                                font=("times new roman", 12, "bold"))
        d_o_b_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)

        # E-mail
        e_mail_label = tkinter.Label(student_detail_frame, text="Email:", font=("times new roman", 12, "bold"),
                                     bg="white")
        e_mail_label.grid(row=3, column=0, padx=3)

        e_mail_entry = ttk.Entry(student_detail_frame, textvariable=self.var_email, width=20,
                                 font=("times new roman", 12, "bold"))
        e_mail_entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)

        # Phone no
        phone_no_label = tkinter.Label(student_detail_frame, text="Phone  No:", font=("times new roman", 12, "bold"),
                                       bg="white")
        phone_no_label.grid(row=3, column=2, padx=3)

        phone_no_entry = ttk.Entry(student_detail_frame, textvariable=self.var_phone_no, width=20,
                                   font=("times new roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=2, pady=5, sticky=W)

        # Address
        address_label = tkinter.Label(student_detail_frame, text="Address:", font=("times new roman", 12, "bold"),
                                      bg="white")
        address_label.grid(row=4, column=0, padx=3)

        address_entry = ttk.Entry(student_detail_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=2, pady=5, sticky=W)

        # Teacher name
        teacher_name_label = tkinter.Label(student_detail_frame, text="Teacher Name:",
                                           font=("times new roman", 12, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=3)

        teacher_name_entry = ttk.Entry(student_detail_frame, textvariable=self.var_teacher_name, width=20,
                                       font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=2, pady=5, sticky=W)

        # radio button
        self.var_radio_1 = tkinter.StringVar()
        radio_button_1 = ttk.Radiobutton(student_detail_frame, variable=self.var_radio_1,
                                         text="Take Photo Sample", value="Yes")
        radio_button_1.grid(row=6, column=0)
        radio_button_2 = ttk.Radiobutton(student_detail_frame, variable=self.var_radio_1,
                                         text="No Photo Sample", value="No")
        radio_button_2.grid(row=6, column=1)

        # button frame
        button_frame = tkinter.LabelFrame(main_frame, bd=2, relief=RIDGE)
        button_frame.place(x=13, y=350, width=582, height=71)

        # save button
        save_button = tkinter.Button(button_frame, command=self.add_data, text="Save", width=13,
                                     font=("time new roman", 13, "bold"), bg="midnight blue", fg="white")
        save_button.grid(row=0, column=0)

        # update button
        update_button = tkinter.Button(button_frame, command=self.update_data, text="Update", width=13,
                                       font=("time new roman", 13, "bold"),
                                       bg="midnight blue", fg="white")
        update_button.grid(row=0, column=1)

        # Delete button
        delete_button = tkinter.Button(button_frame, command=self.delete_data, text="Delete", width=14,
                                       font=("time new roman", 13, "bold"),
                                       bg="midnight blue", fg="white")
        delete_button.grid(row=0, column=2)

        # reset button
        reset_button = tkinter.Button(button_frame, command=self.reset_data, text="Reset", width=15,
                                      font=("time new roman", 13, "bold"),
                                      bg="midnight blue", fg="white")
        reset_button.grid(row=0, column=3)

        # take/update button frame
        button_frame = tkinter.LabelFrame(main_frame, bd=1, relief=RIDGE)
        button_frame.place(x=13, y=386, width=583, height=34)

        # Take photo sample button
        take_photo_sam_button = tkinter.Button(button_frame, command=self.gen_photo_sam, text="Take Photo Sample", width=28,
                                               font=("time new roman", 13, "bold"), bg="midnight blue", fg="white")
        take_photo_sam_button.grid(row=0, column=0)

        # Update Photo Sample button
        update_photo_s_button = tkinter.Button(button_frame, text="Update Photo Sample", width=29,
                                               font=("time new roman", 13, "bold"), bg="midnight blue", fg="white")
        update_photo_s_button.grid(row=0, column=1)

        # ===============Right label frame=====================
        right_frame = tkinter.LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE)
        right_frame.place(x=617, y=5, width=636, height=423)

        # search by system
        search_by_frame = tkinter.LabelFrame(right_frame, bd=2, relief=RIDGE, text=" Search By Info ",
                                             font=("times new roman", 12, "bold"))
        search_by_frame.place(x=5, y=0, width=622, height=68)

        # Search button
        search_by_button = tkinter.Button(search_by_frame, text="Search By:", width=10,
                                          font=("time new roman", 12, "bold"), bg="red", fg="white")
        search_by_button.grid(row=0, column=0, padx=5, pady=7)

        search_by_combo = ttk.Combobox(search_by_frame, width=14, font=("times new roman", 12, "bold"),
                                       state="readonly")
        search_by_combo["values"] = ("Select", "ID", "Roll No", "Registration No")
        search_by_combo.current(0)
        search_by_combo.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # enter  the selected search by
        search_by_entry = ttk.Entry(search_by_frame, width=16, font=("times new roman", 12, "bold"))
        search_by_entry.grid(row=0, column=2, padx=2, pady=7)

        # search button
        search_button = tkinter.Button(search_by_frame, text="Search", width=12, font=("time new roman", 10, "bold"),
                                       bg="cyan", fg="white")
        search_button.grid(row=0, column=3, padx=2, pady=7)

        # show_all button
        show_all_button = tkinter.Button(search_by_frame, text="Show all", width=12,
                                         font=("time new roman", 10, "bold"), bg="cyan", fg="white")
        show_all_button.grid(row=0, column=4, padx=2, pady=7)

        # ======================== Table frame =============
        table_frame = tkinter.LabelFrame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=70, width=622, height=345)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=("dep", "course", "year", "sem", "studentID",
                                                   "name", "division", "roll_no", "gender", "dob",
                                                   "email", "phone_no", "address", "teacher_name", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dep', text="Department")
        self.student_table.heading('course', text="Course")
        self.student_table.heading('year', text="Year")
        self.student_table.heading('sem', text="Semester")
        self.student_table.heading('studentID', text="Student ID")
        self.student_table.heading('name', text="Student Name")
        self.student_table.heading('division', text="Division")
        self.student_table.heading('roll_no', text="Roll No")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading('dob', text="DOB")
        self.student_table.heading('email', text="Email")
        self.student_table.heading('phone_no', text="Phone No")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('teacher_name', text="Teacher Name")
        self.student_table.heading('photo', text="Photo Sample")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=110)
        self.student_table.column("course", width=110)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=110)
        self.student_table.column("studentID", width=110)
        self.student_table.column("name", width=110)
        self.student_table.column("division", width=110)
        self.student_table.column("roll_no", width=110)
        self.student_table.column("gender", width=110)
        self.student_table.column("dob", width=110)
        self.student_table.column("email", width=110)
        self.student_table.column("phone_no", width=110)
        self.student_table.column("address", width=110)
        self.student_table.column("teacher_name", width=110)
        self.student_table.column("photo", width=110)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ===================funtion declaration =============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "All  fields are required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="zahirali1!",
                    database="face_recognizer"
                )

                my_cursor = connection.cursor()
                my_cursor.execute("INSERT INTO student (dep, course, year, sem, studentID, name, division,"
                                  " roll_no, gender, dob, email, phone_no, address, teacher_name, photo) VALUES "
                                  "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_sem.get(),
                                      self.var_studentID.get(),
                                      self.var_name.get(),
                                      self.var_division.get(),
                                      self.var_roll_no.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone_no.get(),
                                      self.var_address.get(),
                                      self.var_teacher_name.get(),
                                      self.var_radio_1.get()

                                  ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("success", "Student details has been successfully added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ================= fetch data ================
    def fetch_data(self):
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="zahirali1!",
            database="face_recognizer"
        )

        my_cursor = connection.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            connection.commit()
        connection.close()

    # =============== get cursor ==============
    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_studentID.set(data[4])
        self.var_name.set(data[5])
        self.var_division.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone_no.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher_name.set(data[13])
        self.var_radio_1.set(data[14])

    # ================= update function =============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_dob.get() == "":
            messagebox.showerror("Error", "All  fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update", parent=self.root)
                if update > 0:
                    connection = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="zahirali1!",
                        database="face_recognizer"
                    )

                    my_cursor = connection.cursor()
                    my_cursor.execute(
                        "UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, "
                        "studentID=%s, name=%s, division=%s, roll_no=%s, gender=%s, dob=%s, "
                        "email=%s, phone_no=%s, address=%s, teacher_name=%s, photo=%s WHERE studentID=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_studentID.get(),
                            self.var_name.get(),
                            self.var_division.get(),
                            self.var_roll_no.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone_no.get(),
                            # You had 'phone_no' here, which needs to be consistent with the variable name.
                            self.var_address.get(),
                            self.var_teacher_name.get(),
                            self.var_radio_1.get(),
                            self.var_studentID.get()  # This is used to specify which record to update.
                        ))


                else:
                    if not update:
                        return
                messagebox.showinfo("success", "Student details has been successfully updated", parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

        # ==================== delete function ======================

    def delete_data(self):
        if self.var_studentID.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete the data", parent=self.root)
                if delete > 0:
                    connection = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="zahirali1!",
                        database="face_recognizer")
                    my_cursor = connection.cursor()
                    sql = "Delete from student Where studentID=%s"
                    val = (self.var_studentID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not update:
                        return
                messagebox.showinfo("success", "Student details has been deleted successfully",
                                             parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ===================== reset function ====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_studentID.set("")
        self.var_name.set("")
        self.var_division.set("Select Division")
        self.var_roll_no.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_teacher_name.set("")
        self.var_radio_1.set("")

    # ===================== generate photo sample =============
    def gen_photo_sam(self):
        if self.var_studentID.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="zahirali1!",
                    database="face_recognizer")
                my_cursor = connection.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for i in my_result:
                    id += 1
                my_cursor.execute(
                    "UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, "
                    "studentID=%s, name=%s, division=%s, roll_no=%s, gender=%s, dob=%s, "
                    "email=%s, phone_no=%s, address=%s, teacher_name=%s, photo=%s WHERE studentID=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_studentID.get(),
                        self.var_name.get(),
                        self.var_division.get(),
                        self.var_roll_no.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone_no.get(),
                        # You had 'phone_no' here, which needs to be consistent with the variable name.
                        self.var_address.get(),
                        self.var_teacher_name.get(),
                        self.var_radio_1.get(),
                        self.var_studentID.get() == id + 1  # This is used to specify which record to update.
                    ))

                connection.commit()
                self.fetch_data()
                self.reset_data()
                connection.close()

                # ============================== load predefined data frontal from opencv ===========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap_ture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap_ture.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1

                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data_capture/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap_ture.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Success", "Information successfully added!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = students(root)
    root.mainloop()
