from models import db
from datetime import datetime
from .auth_models.user_model import User
from sqlalchemy.orm import backref, relationship

class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer(), primary_key=True)
    student_number = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    qualification_id = db.Column(db.Integer(), db.ForeignKey('qualifications.id'))


    #Relationship with User model
    user = db.relationship("User", back_populates="student")

    #Relationship with qualificaiton model
    qualifications = relationship('Qualification', secondary='qualification_period', backref=backref('students', lazy="dynamic"))

    #Relationship with student reg
    modules = relationship('Module', secondary='studentRegister', backref=backref('students', lazy=True))

    #Relationship with session
    sessions = relationship("ModuleSession", secondary= "attendance", backref=backref('students', lazy=True))