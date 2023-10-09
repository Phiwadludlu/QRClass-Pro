from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .auth_models.user_model import User
from .auth_models.roles_model import Role,RoleUsers
from .lecturer_model import Lecturer
from .student_model import Student
from .module_model import Module
from .session_model import ModuleSession
from .attendance_model import Attendance
from .qr_model import QR
from .timeslot_model import TimeSlot
from .student_register_model import StudentRegister
from .qualification_model import Qualification