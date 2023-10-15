from sqlalchemy import Column,Integer,String,Time,ForeignKey, Time
from models import db

class TimeSlot(db.Model):
    __tablename__ = 'timeslots'

    id = Column(Integer(),primary_key=True)
    day = Column(String(255))
    start_time = Column(Time(), nullable=False)
    end_time = Column(Time(), nullable= False)
    module_id = Column(Integer(), ForeignKey('modules.id'))

    #Relationship

    sessions = db.relationship('ModuleSession', back_populates="timeslot")