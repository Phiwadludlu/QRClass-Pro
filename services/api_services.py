from flask import jsonify
import datetime

def format_attendance_query(data):
    result = []
    for attendance, _, student, module in data:
        schema = {
            "student_number": student.student_number,
            "module_code": module.module_code,
            "module_name": module.module_name,
            "attendance_date" : attendance.created_at.date().isoformat(),
            "attendance_time" : attendance.created_at.time().isoformat(timespec='minutes'),
            "attendance_status" : "Present" if attendance.is_present == True else "Absent",
        }
        result.append(schema)

    return jsonify(result)

def format_module_query(data):

    result = []
    for item in data:
        schema = {
            "id" : item.id,
            "code" : item.module_code,
            "name" : item.module_name,
            "type" : "module",
        }
        result.append(schema)

    return jsonify(result)

def format_qualification_query(data):

    result = []
    for item in data:
        schema = {
            "id" : item.id,
            "code" : item.code,
            "name" : item.name,
            "type" : "qualification",
        }
        result.append(schema)

    return jsonify(result)

def format_qr_query(data):
    result = []
    for module, qr, timeslot, _ in data:
        schema = {
            "module_name" : module.module_name,
            "session" : timeslot.start_time.isoformat(timespec='minutes') + ' - ' + timeslot.end_time.isoformat(timespec='minutes'),
            "expiration_date" : qr.expiration_date.date().isoformat(),
            "expiration_time" : qr.expiration_date.time().isoformat(timespec='minutes'),
            "is_active" : qr.is_active,
            "qr_url" : qr.qr_url,
        }
        result.append(schema)

    return jsonify(result)

def format_timetable_query(data):
    result = []
    for _, _, module, timeslot, attendance in data:
        schema = {
            "module_name" : module.module_name,
            "day_of_week" : timeslot.day,
            "time" : timeslot.start_time.isoformat(timespec='minutes') + ' - ' + timeslot.end_time.isoformat(timespec='minutes'),
            "status" : get_session_status(timeslot.start_time,timeslot.end_time, attendance.is_present),
        }
        result.append(schema)

    print(result)

    return jsonify(result)

def get_session_status(start_time, end_time, is_present):
    if datetime.datetime.combine(datetime.datetime.now().date(), start_time) <= datetime.datetime.now() <= datetime.datetime.combine(datetime.datetime.now().date(), end_time):
        return "Ongoing"
    elif datetime.datetime.combine(datetime.datetime.now().date(), start_time) >= datetime.datetime.now():
        return "Upcoming"
    else:
        return "Present" if is_present == True else "Absent"

def get_semester_period():
    if datetime.datetime(2023, 2, 1, 00, 0, 0, 000000) <= datetime.datetime.now() <= datetime.datetime(2023, 7, 14, 00, 0, 0, 000000):
        return 1
    elif datetime.datetime(2023, 7, 15, 00, 0, 0, 000000) <= datetime.datetime.now() <= datetime.datetime(2023, 12, 15, 00, 0, 0, 000000):
        return 2