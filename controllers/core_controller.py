
"""The controllers module is for business logic"""
from flask import redirect, render_template,request, url_for,flash
from models.auth_models.roles_model import Role
from models import Lecturer,Student
import services

from flask_security import auth_required
from flask_security.registerable import register_user
from flask_security.utils import hash_password
from flask_security.decorators import anonymous_user_required

from models import db
from models.auth_models.user_model import User

#Form Imports
from forms.auth_forms.sign_up_form import StudentSignUp,LecturerSignUp, StudentRegisterForm, LecturerRegisterForm




def index():
    dropdown_items = [{'id':'chk-0', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'level' : '3', 'code' : 'BINCT'},{'id':'chk-1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','level': '2', 'code' : 'DIIAD1'}];
    limit = 2
    return render_template('layouts/LandingPage_layout.html', dropdown_items=dropdown_items,tags=[],limit=limit)


def create_tables():

    services.create_tables()
    
    return "Done", 200


def login():

    return "login"

@anonymous_user_required
def signUp():

    
    
    return render_template("auth/register.html")


@anonymous_user_required
def lecturer_sign_up():
    
    register_user_form=LecturerRegisterForm()

    
    if request.method=="POST":
        if register_user_form.validate_on_submit():


            lecturer_role = Role.query.filter_by(id=3).first_or_404()

            #Add user to DB logic here
            new_user = User(email= register_user_form.email.data, password=hash_password(register_user_form.password.data), active=True )
            new_user.fs_uniquifier = new_user.get_auth_token()
            new_user.is_active = True
            new_user.roles.append(lecturer_role)

            new_lecturer = Lecturer(staff_number = register_user_form.staff_number.data, user=new_user)

            db.session.add(new_user)
            db.session.add(new_lecturer)
            db.session.commit()

            flash("Account created successfully",category="info")

            return redirect(url_for("security.login"))

    return render_template("components/forms/auth_forms/lecturer_form.html",register_user_form=register_user_form )


@anonymous_user_required
def student_sign_up():
    
    register_user_form=StudentRegisterForm()
    
    if request.method=="POST":
        if register_user_form.validate_on_submit():


            student_role = Role.query.filter_by(id=2).first_or_404()

            #Add user to DB logic here
            new_user = User(email= register_user_form.email.data, password=hash_password(register_user_form.password.data), active=True )
            new_user.fs_uniquifier = new_user.get_auth_token()
            new_user.is_active = True
            new_user.roles.append(student_role)

            new_student = Student(student_number=register_user_form.student_number.data,user=new_user )

            db.session.add(new_user)
            db.session.add(new_student)
            db.session.commit()

            flash("Account created successfully",category="info")

            return redirect(url_for("security.login"))
        
    return render_template("components/forms/auth_forms/student_form.html",register_user_form=register_user_form )