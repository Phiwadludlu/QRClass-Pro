from flask import Blueprint
from controllers import lecturer_controller as le_controller

lecturer_route = Blueprint("lecturers", __name__)

lecturer_route.get('/attendance') (le_controller.viewAttendance)