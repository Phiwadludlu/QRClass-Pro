from flask import render_template
from controllers.mutliselect_controller import getAllQualifications, getAllModules

def gettingStarted1():
    qualificationData = getAllQualifications()
    limit = 1
    return render_template('layouts/student/GetttingStarted1_layout.html', dropdown_items=qualificationData, limit=limit, tags=[])

def gettingStarted2():
    moduleData = getAllModules()
    limit = 5
    return render_template('layouts/student/GettingStarted2_layout.html', dropdown_items=moduleData, limit=limit, tags=[])

def studentAttendance():
    return render_template("layouts/student/StudentAttendance_layout.html")