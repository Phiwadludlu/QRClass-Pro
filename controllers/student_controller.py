from flask import render_template
from flask_security.decorators import roles_required
from controllers import api_controller as apic
import json
from flask_login import current_user

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
    return render_template("layouts/student/StudentMain_layout.html", timetable=timetable_data)

@roles_required('student')
def scanQR():
    return render_template("layouts/student/ScanQR_layout.html")