from models import db

from sqlalchemy import Column,Integer,String,Date,Time,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class StudentRegister(db.Model):
    __tablename__ ='studentRegister'

    id = Column(Integer(), primary_key=True)
    module_id = Column(Integer(), ForeignKey('modules.id'))
    year = Column(Integer(), nullable=False)
    semester = Column(Integer(), nullable=False)

    #Relationships
    #Relationship with student

    student = relationship("Student", back_populates="student_register")