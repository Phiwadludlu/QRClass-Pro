from flask import Blueprint
from controllers import student_controller as st_controller

student_route = Blueprint("students", __name__)

student_route.get('/attendance')(st_controller.studentAttendance)
student_route.get('/getting-started')(st_controller.gettingStarted)