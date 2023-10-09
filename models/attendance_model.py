from models import db
from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = Column(Integer(), primary_key=True)
    student_id = Column(Integer(), ForeignKey('students.id'))
    session_id = Column(Integer(), ForeignKey('sessions.id'))
    created_at = Column(DateTime(), default=datetime.now())