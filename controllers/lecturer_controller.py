from flask import render_template
from flask_security.decorators import permissions_required,roles_required
from controllers import api_controller as apic
import json

@roles_required('lecturer')
def viewByAllAttendance():
    attendance_data = json.loads(apic.send_all_attendance().data)
    return render_template('layouts/lecturer/LecturerAttendance_All_layout.html', attendance_data=attendance_data)

@roles_required('lecturer')
def viewByModuleAttendance():
    module_data = json.loads(apic.send_all_modules().data)
    return render_template('layouts/lecturer/LecturerAttendance_Module_layout.html', modules=module_data)

@roles_required('lecturer')
def viewByStudentAttendance():
    return render_template('layouts/lecturer/LecturerAttendance_Student_layout.html')

@roles_required('lecturer')
def activeQR():
    qr_data = json.loads(apic.send_all_qr_data().data)
    return render_template('layouts/lecturer/ActiveQR_layout.html', qr_data=qr_data)

@roles_required('lecturer')
def generateQR():
    return render_template('layouts/lecturer/GenerateQR_layout.html')

@roles_required('lecturer')
def showGeneratedQR():
    return render_template('layouts/lecturer/QRGenerated_layout.html')

@roles_required('lecturer')
def lecturerMain():
    return render_template('layouts/lecturer/LecturerMain_layout.html')

@roles_required('lecturer')
def manage():
    module_data = json.loads(apic.send_all_modules().data)
    return render_template('layouts/Manage_layout.html', modules=module_data)
