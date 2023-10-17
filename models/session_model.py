from models import db
from datetime import datetime

from sqlalchemy import Column,Integer,String,Date,Boolean,DateTime,ForeignKey

class ModuleSession (db.Model):

    """This is a session model"""
    __tablename__ = "sessions"

    id = Column(Integer(), primary_key=True)
    date = Column(Date(), nullable=False)
    is_cancelled = Column(Boolean, default=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.now())
    modified_at = Column(DateTime(), default= datetime.now())
    module_id = Column(Integer(), ForeignKey("modules.id"))
    timeslot_id = Column(Integer(), ForeignKey("timeslots.id"))
    qr_id = Column(Integer(), ForeignKey('qr.id'))
    session_uuid = Column(String(255))
    
    #Relationships

    module = db.relationship('Module',back_populates='session')

    timeslot = db.relationship('TimeSlot', back_populates='sessions')

    qr = db.relationship('QR', back_populates='session')