from flask import render_template
from controllers import test_db as ddb

def viewByAllAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_All_layout.html', attendance_data=ddb.getAllAttendance())

def viewByModuleAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_Module_layout.html', modules=ddb.getAllModules(), module_limit=1, module_tags=[])

def viewByStudentAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_Student_layout.html')

def activeQR():
    return render_template('layouts/lecturer/ActiveQR_layout.html', qr_data=ddb.getAllQR())

def generateQR():
    return render_template('layouts/lecturer/GenerateQR_layout.html')

def showGeneratedQR():
    return render_template('layouts/lecturer/QRGenerated_layout.html')

def lecturerMain():
    return render_template('layouts/lecturer/LecturerMain_layout.html', user_data={"username":"Lindelweyizizwe Manqele"})

def manage():
    return render_template('layouts/Manage_layout.html', modules=ddb.getAllModules())