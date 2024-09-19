import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\PMLS\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\PMLS\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face Track Attendance Manager.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "FaceTrack Attendance Manager",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images_project','data_capture','database','attend_file']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System ",
    executables = executables
    )