from models import db, TimeSlot, ModuleSession, QR, StudentRegister, Attendance
import schedule
import time
from pytz import timezone
from datetime import datetime
from sqlalchemy import and_
import uuid
from services import api_services as api_s


def make_absent_attendance():
    qrs_expired_today = db.session.query(QR).filter( and_(QR.expiration_date < datetime.now(), QR.expiration_date >= datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)))
    todays_sessions = db.session.query(ModuleSession).filter(ModuleSession.created_at.date() == datetime.now().date())
    for session in todays_sessions:
        if not session.is_cancelled:
            # if there was a session today associated with an expired qr
            if qrs_expired_today.filter(QR.id == session.qr_id).first():
                # get students who do that module
                students_doing_module = db.session.query(StudentRegister).filter(and_(StudentRegister.year == datetime.now().year, StudentRegister.semester == api_s.get_semester_period(), StudentRegister.module_id == session.module_id)).all()
                for student in students_doing_module:
                    # if attendance for this session was not recorded for that student today, consider student 'absent'
                    if not db.session.query(Attendance).filter(and_(Attendance.student_id == student.student_id, Attendance.session_id == session.id)).first():
                        new_attendance = Attendance(student_id=student.student_id,session_id=session.id,is_present=False)
                        db.session.add(new_attendance)
    
    db.session.commit()
        

def session_creation():
    timeslots = db.session.query(TimeSlot).filter( TimeSlot.day == datetime.now().strftime("%A")).all()

    for slot in timeslots:
        new_session = ModuleSession(date=datetime.now().date(),module_id=slot.module_id,timeslot_id=slot.id,session_uuid=str(uuid.uuid1()))
        db.session.add(new_session)

    db.session.commit()

schedule.every().day.at("18:00", timezone("Africa/Johannesburg")).do(make_absent_attendance)
schedule.every().day.at("02:00", timezone("Africa/Johannesburg")).do(session_creation)

def run_jobs():
    while True:
        schedule.run_pending()
        time.sleep(1)