from flask import render_template, redirect, url_for, request
from flask_security.decorators import permissions_required,roles_required
from controllers import api_controller as apic
import json
from datetime import datetime
import base64
import qrcode
import qrcode.image.svg
from models import db, ModuleSession

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
    active_qrs_data, expired_qrs_data = apic.send_all_qr_data()
    print(active_qrs_data, expired_qrs_data)
    return render_template('layouts/lecturer/ActiveQR_layout.html', expired_qrs_data=json.loads(expired_qrs_data.data), active_qrs_data=json.loads(active_qrs_data.data), datetime=datetime)

@roles_required('lecturer')
def generateQR():
    return render_template('layouts/lecturer/GenerateQR_layout.html')

@roles_required('lecturer')
def showGeneratedQR():
    session_uuid = request.args['session']
    
    session = db.session.query(ModuleSession).filter(ModuleSession.session_uuid == session_uuid).first()

    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(session.qr.qr_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    if session_uuid:
        return render_template('layouts/lecturer/QRGenerated_layout.html', img_data=base64.b64encode(img.to_string(encoding="utf-8")).decode())
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
def edit_module():
    module_code = request.args['module']
    module = json.loads(apic.send_module(module_code).data)

    return render_template('layouts/lecturer/EditModules_layout.html', module=module)

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