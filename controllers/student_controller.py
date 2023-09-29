from flask import render_template
from controllers.mutliselect_controller import getAllQualifications, getAllModules

'''
def gettingStarted1():
    qualificationData = getAllQualifications()
    limit = 1
    return render_template('layouts/student/GetttingStarted1_layout.html', dropdown_items=qualificationData, limit=limit, tags=[])

def gettingStarted2():
    moduleData = getAllModules()
    limit = 5
    return render_template('layouts/student/GettingStarted2_layout.html', dropdown_items=moduleData, limit=limit, tags=[])
'''
def gettingStarted():
    return render_template('layouts/student/GettingStarted_layout.html', modules=getAllModules(), module_limit=4, qualifications=getAllQualifications(), qualification_limit=1, module_tags=[], qualification_tags=[], qualification_tags_length=0, module_tags_length=0)

def studentAttendance():
    return render_template("layouts/student/StudentAttendance_layout.html")