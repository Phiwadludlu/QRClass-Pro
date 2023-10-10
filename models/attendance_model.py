from models import db
from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey, Boolean
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = Column(Integer(), primary_key=True)
    is_present = Column(Boolean, default=False)
    student_id = Column(Integer(), ForeignKey('students.id'))
    session_id = Column(Integer(), ForeignKey('sessions.id'))
    created_at = Column(DateTime(), default=datetime.now())