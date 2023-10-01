from flask import Blueprint
from controllers import lecturer_controller as le_controller

lecturer_route = Blueprint("lecturers", __name__)

lecturer_route.get('/')(le_controller.lecturerMain)

lecturer_route.get('/attendance') (le_controller.viewByAllAttendance)
lecturer_route.get('/attendance/all') (le_controller.viewByAllAttendance)
lecturer_route.get('/attendance/module') (le_controller.viewByModuleAttendance)
lecturer_route.get('/attendance/student') (le_controller.viewByStudentAttendance)

lecturer_route.get('/manage') (le_controller.manage)

lecturer_route.get('/qr/active') (le_controller.activeQR)
lecturer_route.get('/qr/generate') (le_controller.generateQR)
lecturer_route.get('/qr/generated') (le_controller.showGeneratedQR)