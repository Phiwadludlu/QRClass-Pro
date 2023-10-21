from flask import request, jsonify
from models import db, Attendance, Student, ModuleSession, Module, Qualification, QR, TimeSlot, StudentRegister, Lecturer
from services import api_services as api_s
from datetime import datetime, timedelta
from flask_security.decorators import auth_required
from sqlalchemy import and_, or_
import json
from flask_login import current_user

def get_attendance_query():
    attendance_query = db.session.query(Attendance, ModuleSession, Student, Module)\
        .filter(
            and_(
                ModuleSession.id == Attendance.session_id,
                Student.id == Attendance.student_id,
                ModuleSession.module_id == Module.id,
                Attendance.created_at >= datetime.now() - timedelta(days=14)
            )
        )
    
    return attendance_query

def send_module(module_code):
    module = db.session.query(Module).filter(Module.module_code == module_code).first()

    return api_s.format_single_module(module)

def get_qr_query():
    qr_query = db.session.query(Module, QR, TimeSlot, ModuleSession)\
    .filter(
        and_(
            TimeSlot.id == ModuleSession.timeslot_id,
            QR.id == ModuleSession.qr_id, 
            Module.id == ModuleSession.module_id
        )
    )

    return qr_query

def get_timetable_query():
    timetable_query = db.session.query(Student, StudentRegister, Module, TimeSlot)\
        .filter(
            and_(
                Student.id == StudentRegister.student_id, 
                Module.id == StudentRegister.module_id, 
                TimeSlot.module_id == Module.id,
            )
        )

    return timetable_query

def get_timeslots_query():
    timeslot_query = db.session.query(Module, TimeSlot)\
    .filter(
        and_(
            TimeSlot.module_id == Module.id
        )
    )

    return timeslot_query

def send_all_timeslot():
    timeslot_query = get_timeslots_query()
    timeslots = timeslot_query.all()

    return api_s.format_timeslot_data(timeslots)

def send_timeslots_by_module():
    data = request.data
    unloaded = json.loads(data)

    module_code = unloaded['module_code']

    module_query = Module.query.filter(Module.module_code == module_code).first()
    timeslots = TimeSlot.query.filter(module_query.id == TimeSlot.module_id).all()

    return api_s.format_timeslot_data(timeslots)

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

def send_all_modules_by_lecturer(lecturer_staff_number):
    lecturer = Lecturer.query.filter(Lecturer.staff_number == lecturer_staff_number).first()
    modules = Module.query.filter(Module.lecturer_id == lecturer.id).all()

    return api_s.format_module_query(modules)

def send_all_modules_by_student(student_number):
    stud = Student.query.filter(Student.student_number == student_number).first()
    modules_reg = StudentRegister.query.filter(StudentRegister.student_id == stud.id).all()

    m = [item.module_id for item in modules_reg]

    modules = Module.query.filter(Module.id.in_(m)).all()

    return api_s.format_module_query(modules)

def send_all_qualifications():
    qualifications = Qualification.query.all()

    return api_s.format_qualification_query(qualifications)

def send_all_qr_data():
    qr_query = get_qr_query()
    expired_qrs = qr_query.filter(QR.expiration_date < datetime.now()).all()
    active_qrs = qr_query.filter(QR.expiration_date > datetime.now()).all()

    return (api_s.format_qr_query(active_qrs), api_s.format_qr_query(expired_qrs))

def send_user_timetable(student_number):
    timetable_query = get_timetable_query()
    print(timetable_query.all())
    timetable = timetable_query.filter(and_((StudentRegister.year == datetime.now().year), (StudentRegister.semester == api_s.get_semester_period()),(TimeSlot.day == datetime.now().strftime("%A")), (Student.student_number == student_number) )).all()

    return api_s.format_timetable_query(timetable)

@auth_required()
def add_module():
    try:
        data = request.data
        unloaded = json.loads(data)

        module_code = unloaded['module_code']
        print(module_code)
        user_type = unloaded['type']

        module_query = db.session.query(Module).filter(Module.module_code == module_code).first()

        if user_type == 'lecturer':
            if module_query.lecturer_id == None:
                module_query.lecturer_id = current_user.lecturer.id
                db.session.add(module_query)
            else:
                return jsonify({'code' : -1}) # someone else already teaches this module
        elif user_type == 'student':
            new_reg = StudentRegister(student_id=current_user.student.id, module_id=module_query.id, year=datetime.now().year, semester=api_s.get_semester_period())
            db.session.add(new_reg)
            
        db.session.commit()

        return jsonify({'code' : 1}) # all is well
    except:
        return jsonify({'code' : -2}) # server error 
