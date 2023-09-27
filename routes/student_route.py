from flask import Blueprint
from controllers import student_controller as st_controller

student_route = Blueprint("students", __name__)

student_route.get('/student-attendance')(st_controller.studentAttendance)
student_route.get("/getting-started-1") (st_controller.gettingStarted1)
student_route.get("/getting-started-2") (st_controller.gettingStarted2)