import models as m
from datetime import datetime

custom_date = '2023-10-10'
custom_start_time= '09:00:00.000000'
custom_end_time = '10:00:00.000000'
custom_is_active = False
custom_module_id = 1
custom_is_present = False
custom_slot_day = 'Wednesday'

def run():

    student = m.Student.query.get(1)
    qr = m.QR(expiration_date = datetime.now(), is_active=True, qr_url = "path to url")
    session = m.ModuleSession(date=datetime.now().date(),created_at = datetime.now(), modified_at = datetime.now(), module_id=custom_module_id, qr_id=qr.id)
    attendance = m.Attendance(is_present=False, student_id=student.id, session_id=session.id)
    student_register = m.StudentRegister(module_id=custom_module_id, year=datetime.now().year, semester=2)
    timeslot = m.TimeSlot(day=custom_slot_day, start_time=datetime.fromisoformat(str(custom_date + 'T' + custom_start_time)).time(),end_time=datetime.fromisoformat(str(custom_date + 'T' + custom_end_time)).time(), module_id=custom_module_id)

    m.db.session.add(qr)
    m.db.session.add(session)
    m.db.session.add(attendance)
    m.db.session.add(student_register)
    m.db.session.add(timeslot)

    m.db.session.commit()




