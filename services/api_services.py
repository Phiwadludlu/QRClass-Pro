from flask import jsonify
import datetime
import base64
import qrcode
import qrcode.image.svg

def format_attendance_query(data):
    result = []
    for item in data:
        attendance, _, student, module = item
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

def format_single_module(data):
    schema = {
            "id" : data.id,
            "code" : data.module_code,
            "name" : data.module_name,
            "type" : "module",
        }
    return jsonify(schema)

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
    for item in data:
        module, qr, timeslot, session = item
        qr_obj = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
        qr_obj.add_data(qr.qr_url)
        qr_obj.make(fit=True)
        img = qr_obj.make_image(fill_color="black", back_color="white")

        schema = {
            "module_name" : module.module_name,
            "session" : timeslot.start_time.isoformat(timespec='minutes') + ' - ' + timeslot.end_time.isoformat(timespec='minutes'),
            "expiration_date" : qr.expiration_date.date().isoformat(),
            "expiration_time" : qr.expiration_date.time().isoformat(timespec='minutes'),
            "session_uuid" : session.session_uuid,
        }
        result.append(schema)

    return jsonify(result)

def format_timetable_query(data):
    result = []
    for item in data:
        _, _, module, timeslot = item
        schema = {
            "module_name" : module.module_name,
            "day_of_week" : timeslot.day,
            "time" : timeslot.start_time.isoformat(timespec='minutes') + ' - ' + timeslot.end_time.isoformat(timespec='minutes'),
            "status" : get_session_status(timeslot.day, timeslot.start_time,timeslot.end_time),
        }
        result.append(schema)

    return jsonify(result)

def format_timeslot_data(timeslots):
    tmp = []

    for item in timeslots:
        _, slot = item
        schema = {
            "day" : slot.day,
            "timeslots" : {
                "timeslot_id" : slot.id, 
                "period" : {
                    "start_time" : slot.start_time.isoformat(), 
                    "end_time" : slot.end_time.isoformat()
                }
            }
        }
        tmp.append(schema)

    result = merge_timeslots(tmp)
    return jsonify(result)

def format_timeslot_module_data(timeslots):
    tmp = []

    for slot in timeslots:
        schema = {
            "day" : slot.day,
            "timeslots" : {
                "timeslot_id" : slot.id, 
                "period" : {
                    "start_time" : slot.start_time.isoformat(), 
                    "end_time" : slot.end_time.isoformat()
                }
            }
        }
        tmp.append(schema)

    result = merge_timeslots(tmp)
    return jsonify(result)

def get_session_status(day, start_time, end_time):
    if get_date_of_day(day).replace(hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0) <= datetime.datetime.now() <= get_date_of_day(day).replace(hour=end_time.hour, minute=end_time.minute, second=0, microsecond=0):
        return "Ongoing"
    elif get_date_of_day(day).replace(hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0) >= datetime.datetime.now():
        return "Upcoming"
    else:
        return "Ended"

def get_semester_period():
    if datetime.datetime(2023, 2, 1, 00, 0, 0, 000000) <= datetime.datetime.now() <= datetime.datetime(2023, 7, 14, 00, 0, 0, 000000):
        return 1
    elif datetime.datetime(2023, 7, 15, 00, 0, 0, 000000) <= datetime.datetime.now() <= datetime.datetime(2023, 12, 15, 00, 0, 0, 000000):
        return 2
    
def get_date_of_day(day_of_week):
    # Define a mapping from day names to their corresponding integer values (0=Monday, 6=Sunday).
    day_mapping = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }
    
    # Get the current date and the current day of the week as an integer.
    today = datetime.datetime.now()
    current_day = today.weekday()

    # Get the integer value of the requested day.
    requested_day = day_mapping.get(day_of_week.lower())
    if requested_day is None:
        return "Invalid day name"

    # Calculate the difference between the requested day and the current day.
    day_difference = requested_day - current_day

    if day_difference < 0:
        # The requested day has already passed this week, so we add 7 days to get to the next week.
        day_difference += 7

    # Calculate the date of the requested day in the current or following week.
    target_date = today + datetime.timedelta(days=day_difference)

    return target_date

def merge_timeslots(data):
    merged_data = {}  # Dictionary to store merged data
    for item in data:
        day = item['day']
        if day not in merged_data:
            # If 'day' is not in merged_data, initialize it with the current item's 'timeslots'
            merged_data[day] = {'day': day, 'timeslots': [item['timeslots']]}
        else:
            # If 'day' is already in merged_data, append the 'timeslots' to the existing list
            merged_data[day]['timeslots'].append(item['timeslots'])

    # Convert the values of the merged_data dictionary to a list
    result = list(merged_data.values())
    return result