from flask import render_template, request, redirect
from flask_security.decorators import roles_required
from models import db, Module, StudentRegister
from controllers import api_controller as apic
import json
from flask_login import current_user
from sqlalchemy import and_

@roles_required('student')
def gettingStarted():
    return render_template('layouts/student/GettingStarted_layout.html')

@roles_required('student')
def studentAttendance():
    attendance_data = json.loads(apic.send_attendance_by_student_number(current_user.student.student_number).data)
    return render_template("layouts/student/StudentAttendance_layout.html", attendance_data=attendance_data)

@roles_required('student')
def StudentMain():
    timetable_data = json.loads(apic.send_user_timetable(current_user.student.student_number).data)
    print(timetable_data)
    return render_template("layouts/student/StudentMain_layout.html", timetable=timetable_data)

@roles_required('student')
def scanQR():
    return render_template("layouts/student/ScanQR_layout.html", student_number=current_user.student.student_number)

@roles_required('student')
def add_module():
    return render_template('layouts/student/NewModule_layout.html')

@roles_required('student')
def remove_module():
    module_code = request.args.get('module')

    if module_code:
        module_query = db.session.query(Module).filter(Module.module_code == module_code).first()
        if module_query:
            db.session.query(StudentRegister).filter(and_(StudentRegister.student_id == current_user.student.id, module_query.id == StudentRegister.module_id)).delete()
            db.session.commit()

    return redirect('/student/manage')

@roles_required('student')
def manage():
    module_data = json.loads(apic.send_all_modules_by_student(current_user.student.student_number).data)
    return render_template('layouts/student/ManageStudent_layout.html', modules=module_data, allow_edit=True)