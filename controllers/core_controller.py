
"""The controllers module is for business logic"""
from flask import render_template

def studentAttendance():
    return render_template("layouts/student/StudentAttendance_layout.html")

def gettingstarted2():
    return render_template("layouts/student/GettingStarted2_layout.html", dropdown_items=[{'id':"chk-PRJB301", "name":"Project B 301","level":"3","code":"PRJB301"}], tags=[], limit=3)

def index():
    dropdown_items = [{'id':'chk-0', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'level' : '3', 'code' : 'BINCT'},{'id':'chk-1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','level': '2', 'code' : 'DIIAD1'}];
    limit = 2
    return render_template('layouts/LandingPage_layout.html', dropdown_items=dropdown_items,tags=[],limit=limit)