from models.auth_models.user_model import User
from wtforms import (EmailField, StringField, IntegerField, PasswordField, validators)
from models.lecturer_model import Lecturer

from models.student_model import Student



def student_number_validator(form,field):
    
    """Checks if theres no user with a similar student number"""

    student = Student.query.filter_by(student_number = field.data).first()

    if student:

        raise validators.ValidationError('Student Number is already in use')
    
    

def staff_number_validator(form,field):

    "Checks if a staff number already exists"

    staff = Lecturer.query.filter_by(staff_number = field.data).first()

    if staff:

        raise validators.ValidationError('Staff number already in use')

