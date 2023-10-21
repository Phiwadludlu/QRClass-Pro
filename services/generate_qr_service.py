
from models import db, ModuleSession, Module, TimeSlot, QR, Student, Attendance, StudentRegister
from flask import request, jsonify
import json
import uuid
from datetime import datetime
from sqlalchemy import and_
from flask_login import current_user

def generate_qr_code():
    try:
        data = request.data
        unloaded = json.loads(data)
        module_code = unloaded['module_code']
        timeslot_id = unloaded['timeslot_id']
        expiration_date = unloaded['expiration_date']

        url_unique_identifier = str(uuid.uuid1())
        session_unique_identifier = str(uuid.uuid1())
        module = Module.query.filter(Module.module_code == module_code).first()
        timeslot = TimeSlot.query.filter(TimeSlot.id == timeslot_id).first()

        new_session = ModuleSession(date=datetime.now().date(), module_id = module.id, timeslot_id=timeslot.id, session_uuid=session_unique_identifier)
        db.session.add(new_session)
        db.session.flush()
        
        qr_url = "uuid=%s&session=%s" % (url_unique_identifier, session_unique_identifier)
        new_qr = QR(expiration_date=datetime.fromisoformat(expiration_date),url_uuid=url_unique_identifier)
        new_qr.qr_url = qr_url
        db.session.add(new_qr)
        db.session.flush()

        new_session.qr_id = new_qr.id
        db.session.add(new_session)

        db.session.commit()

        return jsonify({ "success" : 1, 'session_uuid' : session_unique_identifier})
    except:
        return jsonify({ "success" : 0})
    

def verify_qr_code():
    success = None
    try:
        data = request.data
        unloaded = json.loads(data)
        qr_uuid = unloaded['uuid']
        session_uuid = unloaded['session']
        
        query = QR.query.filter( QR.url_uuid == qr_uuid ).first()
        if query:
            qr_id = query.id
            if query.expiration_date >= datetime.now():
                session = db.session.query(ModuleSession).filter( ModuleSession.qr_id == qr_id).first()
                if session.session_uuid == session_uuid:
                    student_does_module = db.session.query(StudentRegister).filter( and_(StudentRegister.student_id == current_user.student.id, session.module_id == StudentRegister.module_id)).first()
                    if student_does_module:
                        has_logged = db.session.query(Attendance).filter(and_(Attendance.student_id == current_user.student.id, session.id == Attendance.session_id)).first()
                        if not has_logged:
                            log = Attendance(is_present=True, student_id=current_user.student.id, session_id=session.id)
                            db.session.add(log)
                            db.session.commit()
                            success=1 # success
                        else:
                            success=0 # already logged attendance
                    else:
                        success=-1 # student does not do module
                else:
                    success=-2 # invalid uuid
            else:
                success=-3 # expired qr
        else:
            success=-4 # server errors
        return jsonify({"code" : success}) 
    except:
        return jsonify({"code" : -4}) # server error

