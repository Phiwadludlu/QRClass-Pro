from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .auth_models.user_model import User
from .auth_models.roles_model import Role,RoleUsers
