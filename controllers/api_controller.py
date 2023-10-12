from flask import jsonify
from models import db, Attendance, Student, ModuleSession, Module, Qualification, QR, TimeSlot, StudentRegister
from services import api_services as api_s
from datetime import datetime, timedelta
from sqlalchemy import and_

def get_attendance_query():
    attendance_query = db.session.query(Attendance, ModuleSession, Student,Module)\
        .join(ModuleSession, ModuleSession.id == Attendance.session_id)\
        .join(Student, Student.id == Attendance.student_id).join(Module, ModuleSession.module_id == Module.id ).filter( Attendance.created_at >= datetime.now() - timedelta(days=14))
    
    return attendance_query

def get_qr_query():
    qr_query = db.session.query(Module, QR, TimeSlot, ModuleSession)\
    .join(Module, Module.id == TimeSlot.module_id)\
    .join(QR, QR.id == ModuleSession.qr_id)

    return qr_query

def get_timetable_query():
    timetable_query = db.session.query(Student, StudentRegister, Module, TimeSlot, Attendance)\
    .join(Student, Student.student_register_id == StudentRegister.id)\
    .join(Module, StudentRegister.module_id == Module.id)\
    .join(TimeSlot, StudentRegister.module_id == TimeSlot.module_id)\
    .join(Attendance, Attendance.student_id == Student.id)

    return timetable_query

def send_attendance_by_module(module_code):
    attendance_query = get_attendance_query()
    attendance =  attendance_query.filter(Module.module_code == module_code).all()

    return api_s.format_attendance_query(attendance)
    
def send_attendance_by_student_number(student_number):
    attendance_query = get_attendance_query()
    attendance = attendance_query.filter(Student.student_number == student_number).all()

    return api_s.format_attendance_query(attendance)

def send_all_attendance():
    attendance_query = get_attendance_query()
    attendance = attendance_query.all()

    return api_s.format_attendance_query(attendance)

def send_all_modules():
    modules = Module.query.all()

    return api_s.format_module_query(modules)

def send_all_qualifications():
    qualifications = Qualification.query.all()

    return api_s.format_qualification_query(qualifications)

def send_all_qr_data():
    qr_query = get_qr_query()
    qrs = qr_query.all()

    return api_s.format_qr_query(qrs)

def send_user_timetable(student_number):
    timetable_query = get_timetable_query()
    timetable = timetable_query.filter(and_((StudentRegister.year == datetime.now().year), (StudentRegister.semester == api_s.get_semester_period()),(TimeSlot.day == datetime.now().strftime("%A")) )).all()

    return api_s.format_timetable_query(timetable)
