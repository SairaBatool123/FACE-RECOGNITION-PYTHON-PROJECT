from tkinter import*
import tkinter
from tkinter import ttk, RIDGE, W, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, X, Y, BOTH, END
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import os
from tkinter import filedialog

mydata = []
class attendance_sys:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FaceTrack Attendance Manager")
        self.root.wm_iconbitmap("face.ico")


        # ==========================variables===============

        self.var_name = tkinter.StringVar()
        self.var_studentID = tkinter.StringVar()
        self.var_dep = tkinter.StringVar()
        self.var_sem = tkinter.StringVar()
        self.var_date = tkinter.StringVar()
        self.var_time = tkinter.StringVar()
        self.var_attendance = tkinter.StringVar()


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
        page_2_lbl = tkinter.Label(bg_img, text="Attendance Manager", font=("times new roman", 25, "bold"),
                                   bg="navy blue", fg="white")
        page_2_lbl.place(x=0, y=0, width=1280, height=40)

        # main frame
        main_frame = tkinter.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=45, width=1265, height=435)

        # left label frame
        left_frame = tkinter.LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Student Information ",
                                        font=("times new roman", 12, "bold"))
        left_frame.place(x=3, y=5, width=550, height=424)

        # left upper image
        left_img = Image.open(r'C:\Users\PMLS\Desktop\images_project\temp.jpg')
        left_img = left_img.resize((540, 150), Image.LANCZOS)
        self.photoleft_img = ImageTk.PhotoImage(left_img)

        left_lbl = tkinter.Label(left_frame, image=self.photoleft_img)
        left_lbl.place(x=3, y=0, width=540, height=150)

        #  student details
        attendance_detail_frame = tkinter.LabelFrame(main_frame, bd=2)
        attendance_detail_frame.place(x=7, y=180, width=543, height=247)

        # name
        name_label = tkinter.Label(attendance_detail_frame, text="Name:",
                                          font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=0, padx=3)

        name_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_name, width=20,
                                      font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # student id
        student_id_label = tkinter.Label(attendance_detail_frame, text="Student ID:",
                                           font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=2, padx=5)

        student_id_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_studentID, width=20,
                                       font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=3, padx=0, pady=5, sticky=W)

        # department
        department_label = tkinter.Label(attendance_detail_frame, text="Department:", font=("times new roman", 12, "bold"),
                                      bg="white")
        department_label.grid(row=1, column=0, padx=3)

        roll_no_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_dep, width=20,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # semester
        semester_label = tkinter.Label(attendance_detail_frame, text="Semester:", font=("times new roman", 12, "bold"),
                                      bg="white")
        semester_label.grid(row=1, column=2, padx=3)

        semester_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_sem, width=20,
                                  font=("times new roman", 12, "bold"))
        semester_entry.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # date
        date_label = tkinter.Label(attendance_detail_frame, text="Date:", font=("times new roman", 12, "bold"),
                                       bg="white")
        date_label.grid(row=2, column=0, padx=3)

        date_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_date, width=20,
                                   font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # time
        time_label = tkinter.Label(attendance_detail_frame, text="Time:", font=("times new roman", 12, "bold"),
                                       bg="white")
        time_label.grid(row=2, column=2, padx=3)

        time_entry = ttk.Entry(attendance_detail_frame, textvariable=self.var_time, width=20,
                                   font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)

        # attendance status
        attend_status_label = tkinter.Label(attendance_detail_frame, text="Status:", font=("times new roman", 12, "bold"),
                                        bg="white")
        attend_status_label.grid(row=3, column=0, padx=3)

        attend_status_combo = ttk.Combobox(attendance_detail_frame,textvariable=self.var_attendance, width=18,
                                       font=("times new roman", 12, "bold"), state="readonly")
        attend_status_combo["values"] = ("Select status", "Present", "Absent")
        attend_status_combo.current(0)
        attend_status_combo.grid(row=3, column=1, padx=2, pady=5, sticky=W)

        # button frame
        button_frame = tkinter.LabelFrame(main_frame, bd=2, relief=RIDGE)
        button_frame.place(x=13, y=350, width=530, height=69)

        # import c_s_v button
        imp_c_s_v_button = tkinter.Button(button_frame, command=self.import_Csv, text="Import csv", width=26,
                                     font=("time new roman", 13, "bold"), bg="midnight blue", fg="white")
        imp_c_s_v_button.grid(row=0, column=0)

        # export csv button
        expo_c_s_v_button = tkinter.Button(button_frame, command=self.exportCsv, text="Export csv", width=26,
                                       font=("time new roman", 13, "bold"),
                                       bg="midnight blue", fg="white")
        expo_c_s_v_button.grid(row=0, column=1)

        # update button
        update_button = tkinter.Button(button_frame, text="Update", width=26,
                                       font=("time new roman", 13, "bold"),
                                       bg="midnight blue", fg="white")
        update_button.grid(row=1, column=0)

        # reset button
        reset_button = tkinter.Button(button_frame, command=self.reset_data, text="Reset", width=26,
                                      font=("time new roman", 13, "bold"),
                                      bg="midnight blue", fg="white")
        reset_button.grid(row=1, column=1)


    # =================   right label frame =========
        # right label frame
        right_table_frame = tkinter.LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Student Details ",
                                         font=("times new roman", 12, "bold"))
        right_table_frame.place(x=555, y=5, width=700, height=424)

        # the table
        table_frame = tkinter.LabelFrame(right_table_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=685, height=393)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_detail_table = ttk.Treeview(table_frame,
                                                    columns=("name", "studentID", "dep", "sem", "date", "time",
                                                             "attendance"), xscrollcommand=scroll_x.set,
                                                    yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_detail_table.xview)
        scroll_y.config(command=self.attendance_detail_table.yview)

        self.attendance_detail_table.heading("name", text="Student Name")
        self.attendance_detail_table.heading("studentID", text="Student ID")
        self.attendance_detail_table.heading("dep", text="Department")
        self.attendance_detail_table.heading("sem", text="Semester")
        self.attendance_detail_table.heading("date", text="Date")
        self.attendance_detail_table.heading("time", text="Time")
        self.attendance_detail_table.heading("attendance", text="Attendance Status")

        self.attendance_detail_table["show"] = "headings"

        self.attendance_detail_table.column("name", width=110)
        self.attendance_detail_table.column("studentID", width=110)
        self.attendance_detail_table.column("dep", width=110)
        self.attendance_detail_table.column("sem", width=110)
        self.attendance_detail_table.column("date", width=110)
        self.attendance_detail_table.column("time", width=110)
        self.attendance_detail_table.column("attendance", width=110)

        self.attendance_detail_table.pack(fill=BOTH, expand=1)

        self.attendance_detail_table.bind("<ButtonRelease>", self.get_cursor)


        # ==================== fetch data ==============

    def fetchData(self,rows):
        self.attendance_detail_table.delete(*self.attendance_detail_table.get_children())
        for i in rows:
            self.attendance_detail_table.insert("", END, values=i)
    # ============= import csv =========
    def import_Csv(self):
        global mydata
        mydata.clear()
        fill_in = filedialog.askopenfilename(initialdir=os.getcwd(), title="open CSV",
                                             filetypes=(("CSV File", "*.csv"), ("All File", ".")), parent=self.root)
        with open(fill_in) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ================= export csv ============

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No data found to export", parent=self.root)
                return False
            fill_in = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="open CSV",
                                             filetypes=(("CSV File", "*.csv"), ("All File", ".")), parent=self.root)
            with open(fill_in, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export",
                                    "Your data exported to "+os.path.basename(fill_in)+" Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to :(str(es))", parent=self.root)

    # ===================== get cursor for filling data ===========
    def get_cursor(self, event=""):
        cursor_row = self.attendance_detail_table.focus()
        content = self.attendance_detail_table.item(cursor_row)
        rows = content['values']
        self.var_name.set(rows[0])
        self.var_studentID.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_sem.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_attendance.set(rows[6])

        # ===================== get cursor for filling data ===========
    def reset_data(self, event=""):
        self.var_name.set("")
        self.var_studentID.set("")
        self.var_dep.set("")
        self.var_sem.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attendance.set("")



if __name__ == "__main__":
    root = tkinter.Tk()
    obj = attendance_sys(root)
    root.mainloop()
