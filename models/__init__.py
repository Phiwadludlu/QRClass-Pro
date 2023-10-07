from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .auth_models.user_model import User
from .auth_models.roles_model import Role,RoleUsers
from .lecturer_model import Lecturer
from .student_model import Student
from .module_model import Module
from .session_model import ModuleSession
