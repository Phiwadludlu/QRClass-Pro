from flask import Blueprint
from controllers import lecturer_controller as le_controller

lecturer_route = Blueprint("lecturers", __name__)

lecturer_route.get('/')(le_controller.lecturerMain)

lecturer_route.get('/attendance') (le_controller.viewByAllAttendance)
lecturer_route.get('/attendance/') (le_controller.redirect_to_attendence)
lecturer_route.get('/attendance/all') (le_controller.redirect_to_attendence)
lecturer_route.get('/attendance/module') (le_controller.viewByModuleAttendance)
lecturer_route.get('/attendance/student') (le_controller.viewByStudentAttendance)

# cut out manage modules screen, too hard
lecturer_route.get('/manage') (le_controller.manage)
lecturer_route.get('/manage/') (le_controller.redirect_to_manage)
lecturer_route.get('/manage/edit') (le_controller.edit_module)
lecturer_route.get('/manage/add') (le_controller.add_module)
lecturer_route.get('/manage/remove') (le_controller.remove_module)

lecturer_route.get('/qr')(le_controller.activeQR)
lecturer_route.get('/qr/') (le_controller.redirect_to_qr)
lecturer_route.get('/qr/generate') (le_controller.generateQR)
lecturer_route.get('/qr/share') (le_controller.showGeneratedQR)