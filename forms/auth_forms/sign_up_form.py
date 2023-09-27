from flask_wtf import FlaskForm

from flask_security.forms import RegisterForm

from wtforms import (EmailField, StringField, IntegerField, PasswordField, validators)

class StudentSignUp (FlaskForm):

    email = EmailField("Email", validators=[validators.Email(), validators.DataRequired()])
    student_number = IntegerField("Student Number", validators=[validators.DataRequired(), validators.length(min=8, max=8, message="Student number is invalid")])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[validators.DataRequired()])
    

class LecturerSignUp(FlaskForm):

    email = EmailField("Email", validators=[validators.Email(), validators.DataRequired()] )
    staff_number = IntegerField("Staff Number", validators=[validators.Length(min=8, max=10, message="Invalid staff number"), validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    confirm_password = PasswordField("Confrim password", validators=[validators.DataRequired()])


class MyRegisterForm (RegisterForm):

    student_number = StringField("Student Number", validators=[validators.DataRequired(), validators.length(min=8, max=8, message="Student number is invalid") ])

    