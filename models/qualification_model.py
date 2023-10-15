from models import db
from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey

class Qualification(db.Model):
    __tablename__ = 'qualifications'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True)
    code = Column(String(255), unique=True)

class QualificationPeriod(db.Model):
    __tablename__ = 'qualification_period'
    
    id = Column(Integer(), primary_key=True)
    start_year = Column(Integer(), nullable=False)
    end_year = Column(Integer(), nullable=False)
    qualification_id = Column(Integer(),ForeignKey('qualifications.id'))
    student_id = Column(Integer(), ForeignKey('students.id'))