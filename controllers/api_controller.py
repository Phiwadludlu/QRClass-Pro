from flask import request, jsonify
from models import db, Attendance, Student, ModuleSession, Module, Qualification, QR, TimeSlot, StudentRegister
from services import api_services as api_s
from datetime import datetime, timedelta
from flask_security.decorators import roles_required
from sqlalchemy import and_
import json
from flask_login import current_user

def get_attendance_query():
    attendance_query = db.session.query(Attendance, ModuleSession, Student, Module)\
        .join(ModuleSession, ModuleSession.id == Attendance.session_id)\
        .join(Student, Student.id == Attendance.student_id)\
        .join(Module, ModuleSession.module_id == Module.id ).filter( Attendance.created_at >= datetime.now() - timedelta(days=14))
    
    return attendance_query

def get_qr_query():
    qr_query = db.session.query(Module, QR, TimeSlot, ModuleSession)\
    .join(TimeSlot, TimeSlot.id == ModuleSession.timeslot_id )\
    .join(QR, QR.id == ModuleSession.qr_id)\
    .join(Module, Module.id == ModuleSession.module_id)

    return qr_query

def get_timetable_query():
    timetable_query = db.session.query(Student, StudentRegister, Module, TimeSlot, Attendance)\
    .join(Student, Student.id == StudentRegister.student_id)\
    .join(Module, Module.id == StudentRegister.module_id)\
    .join(TimeSlot, TimeSlot.module_id == StudentRegister.module_id)\
    .join(Attendance, Attendance.student_id == Student.id)

    return timetable_query

def get_timeslots_query():
    timeslot_query = db.session.query(Module, TimeSlot)\
    .join(TimeSlot, TimeSlot.module_id == Module.id)

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

def send_all_qualifications():
    qualifications = Qualification.query.all()

    return api_s.format_qualification_query(qualifications)

def send_all_qr_data():
    qr_query = get_qr_query()
    qrs = qr_query.all()

    return api_s.format_qr_query(qrs)

def send_user_timetable(student_number):
    timetable_query = get_timetable_query()
    timetable = timetable_query.filter(and_((StudentRegister.year == datetime.now().year), (StudentRegister.semester == api_s.get_semester_period()),(TimeSlot.day == datetime.now().strftime("%A")), (Student.student_number == student_number) )).all()

    return api_s.format_timetable_query(timetable)

@roles_required('lecturer')
def add_module():
    try:
        data = request.data
        unloaded = json.loads(data)

        module_code = unloaded['module_code']
        module_name = unloaded['module_name']
        timeslots = unloaded['timeslots']

        new_module = Module(module_name=module_name, module_code=module_code, lecturer_id=current_user.lecturer.id)
        db.session.add(new_module)
        db.session.flush()

        for slot in timeslots:
            for time in slot['times']:
                new_slot = TimeSlot(day=slot['day'],start_time=datetime.strptime(time.split("-")[0], '%H:%M').time(),end_time=datetime.strptime(time.split("-")[1], '%H:%M').time(), module_id=new_module.id)
                db.session.add(new_slot)
                new_slot = None

        
        db.session.commit()

        return jsonify({'success' : 1})
    except:
        return jsonify({'success' : 0})
