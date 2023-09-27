
"""The controllers module is for business logic"""
from flask import render_template
from controllers.mutliselect_controller import getAllQualifications, getAllModules

def studentAttendance():
    return render_template("layouts/student/StudentAttendance_layout.html")

def gettingstarted2():
    return render_template("layouts/student/GettingStarted2_layout.html", dropdown_items=[{'id':"chk-PRJB301", "name":"Project B 301","level":"3","code":"PRJB301"}], tags=[], limit=3)

def index():
    return render_template('layouts/LandingPage_layout.html')

def gettingStarted1():
    qualificationData = getAllQualifications()
    limit = 1
    return render_template('layouts/student/GetttingStarted1_layout.html', dropdown_items=qualificationData, limit=limit, tags=[])

def gettingStarted2():
    moduleData = getAllModules()
    limit = 5
    return render_template('layouts/student/GettingStarted2_layout.html', dropdown_items=moduleData, limit=limit, tags=[])