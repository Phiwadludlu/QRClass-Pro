from flask import render_template
from flask_security.decorators import permissions_required,roles_required
from controllers import test_db as ddb

@roles_required('lecturer')
def viewByAllAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_All_layout.html', attendance_data=ddb.getAllAttendance())

@roles_required('lecturer')
def viewByModuleAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_Module_layout.html', modules=ddb.getAllModules(), module_limit=1, module_tags=[])

@roles_required('lecturer')
def viewByStudentAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_Student_layout.html')

@roles_required('lecturer')
def activeQR():
    return render_template('layouts/lecturer/ActiveQR_layout.html', qr_data=ddb.getAllQR())

@roles_required('lecturer')
def generateQR():
    return render_template('layouts/lecturer/GenerateQR_layout.html')

@roles_required('lecturer')
def showGeneratedQR():
    return render_template('layouts/lecturer/QRGenerated_layout.html')

@roles_required('lecturer')
def lecturerMain():
    return render_template('layouts/lecturer/LecturerMain_layout.html', user_data={"username":"Lindelweyizizwe Manqele"})

@roles_required('lecturer')
def manage():
    return render_template('layouts/Manage_layout.html', modules=ddb.getAllModules())
