from flask import render_template

def viewAttendance():
    return render_template('layouts/lecturer/LecturerAttendance.html')