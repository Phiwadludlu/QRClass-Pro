
from models import db, ModuleSession, Module, TimeSlot, QR, Student, Attendance
from flask import request, jsonify
import json
import uuid
from datetime import datetime
import qrcode
import qrcode.image.svg

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
        new_qr = QR(expiration_date=datetime.fromisoformat(expiration_date),is_active=True,url_uuid=url_unique_identifier)
        new_qr.qr_url = qr_url
        db.session.add(new_qr)
        db.session.flush()

        new_session.qr_id = new_qr.id
        db.session.add(new_session)

        db.session.commit()
        
        qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
        qr.add_data(qr_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        return jsonify({ "success" : 1, 'img' : img.to_string(encoding='unicode')})
    except:
        print(module_code,timeslot_id,expiration_date)
        return jsonify({ "success" : 0})
    

def verify_qr_code():
    try:
        data = request.data
        unloaded = json.loads(data)
        student_number = unloaded['student_number']
        qr_uuid = unloaded['uuid']
        session_uuid = unloaded['session']

        query = QR.query.filter( QR.url_uuid == qr_uuid ).first()
        if query.id:
            qr_id = query.id
            session = ModuleSession.query.filter( ModuleSession.qr_id == qr_id).first()
            if session.session_uuid == session_uuid:
                student = Student.query.filter(Student.student_number == student_number).first()
                log = Attendance(is_present=True, student_id=student.id, session_id=session.id)
                db.session.add(log)
                db.session.commit()
                return jsonify({"success" : 1})
        return jsonify({"success" : 0})
    except:
        return jsonify({"success" : 0})

