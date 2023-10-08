from models import db
from datetime import datetime
from sqlalchemy import Column, Integer, Date,DateTime,String,ForeignKey



class Module (db.Model):

    __tablename__ = "modules"

    id = Column(Integer(), primary_key=True)
    module_name = Column(String(255), nullable=False)
    module_code = Column(String(25), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    modified_at = Column(DateTime(), default=datetime.now())
    lecutrer_id = Column(Integer(), ForeignKey("lecturers.id"))


    #Relationship
    lecturer = db.relationship('Lecturer', back_populates = 'module')

    session = db.relationship('ModuleSession', back_populates = 'module')