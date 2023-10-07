from flask import render_template
from flask_security.decorators import roles_required
from controllers import test_db as ddb

@roles_required('student')
def gettingStarted():
    return render_template('layouts/student/GettingStarted_layout.html', modules=ddb.getAllModules(), module_limit=4, qualifications=ddb.getAllQualifications(), qualification_limit=1, module_tags=[], qualification_tags=[], qualification_tags_length=0, module_tags_length=0)

@roles_required('student')
def studentAttendance():
    auth_user_id = "22175060"
    return render_template("layouts/student/StudentAttendance_layout.html", attendance_data=ddb.getStudentAttendance(auth_user_id))

@roles_required('student')
def StudentMain():
    return render_template("layouts/student/StudentMain_layout.html",
    user_data={"username":"Gugulethu Duma","qualification":"BINCT1", "timetable": ddb.getUserTimetable()})

@roles_required('student')
def scanQR():
    return render_template("layouts/student/ScanQR_layout.html")