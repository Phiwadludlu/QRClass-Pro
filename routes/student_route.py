from flask import Blueprint
from controllers import student_controller as sc

student_route = Blueprint("students", __name__)

student_route.get("/")(sc.StudentMain)
student_route.get('/attendance')(sc.studentAttendance)
student_route.get('/getting-started')(sc.gettingStarted)
student_route.get('/qr/scan')(sc.scanQR)