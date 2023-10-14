from models import db

from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class StudentRegister(db.Model):
    __tablename__ ='studentRegister'

    id = Column(Integer(), primary_key=True)
    module_id = Column(Integer(), db.ForeignKey('modules.id'))
    student_id = Column(Integer(), db.ForeignKey('students.id'))
    year = Column(Integer(), nullable=False)
    semester = Column(Integer(), nullable=False)

