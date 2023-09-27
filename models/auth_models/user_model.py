from models import db
from datetime import datetime
from flask_security.models import fsqla_v3 as fsqla
from .roles_model import RoleUsers, Role
from sqlalchemy.orm import relationship, backref

#USER MODEL 


class User(db.Model, fsqla.FsUserMixin):
    """Stores user information such as email username and password"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    student_number = db.Column(db.String(8), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    #Relationship with the roles table
    roles = db.relationship('Role', secondary='roles_users', backref=backref("users", lazy="dynamic"))

