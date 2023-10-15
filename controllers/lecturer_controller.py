from flask import render_template, redirect, url_for, request
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
    img_data = request.args['img']
    if img_data:
        return render_template('layouts/lecturer/QRGenerated_layout.html', img_data=img_data)
    else:
        return redirect(url_for('not_found'))

@roles_required('lecturer')
def lecturerMain():
    return render_template('layouts/lecturer/LecturerMain_layout.html')

@roles_required('lecturer')
def manage():
    module_data = json.loads(apic.send_all_modules().data)
    return render_template('layouts/lecturer/Manage_layout.html', modules=module_data)

@roles_required('lecturer')
def edit_module(module_id):
    
    return render_template('layouts/lecturer/EditModules_layout.html')

@roles_required('lecturer')
def add_module():
    
    return render_template('layouts/lecturer/NewModule_layout.html')

@roles_required('lecturer')
def remove_module(module_id):
    '''
        It wont actually delete the module, will just un assign the lecturer teaching the module
    '''
    pass

@roles_required('lecturer')
def redirect_to_attendence():
    
    return redirect(url_for('lecturers.viewByAllAttendance'))

@roles_required('lecturer')
def redirect_to_manage():
    
    return redirect(url_for('lecturers.manage'))

@roles_required('lecturer')
def redirect_to_qr():
    
    return redirect(url_for('lecturers.activeQR'))