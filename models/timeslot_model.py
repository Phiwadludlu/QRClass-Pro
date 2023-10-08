from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey, Time
from models import db

class TimeSlot(db.Model):
    __tablename__ = 'timeslots'

    id = Column(Integer(),primary_key=True)
    day = Column(String(255))
    time = Column(Time())
    module_id = Column(Integer(), ForeignKey('sessions.id'))

    #Relationship

    module_session = db.relationship('ModuleSession', back_populates="timeslot")