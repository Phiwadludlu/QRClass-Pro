from flask import Flask
from flask_cors import CORS
from forms.auth_forms.sign_up_form import StudentRegisterForm
from routes.core_route import core_route
from routes.api_route import api   
import flask_security
import models
import flask_migrate


#Route imports here
from routes.core_route import core_route
from routes.api_route import api   
from routes.student_route import student_route
from routes.lecturer_route import lecturer_route

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object('config')
    
    return app


#Flask App instane
app = create_app()

#Linking models to app
models.db.init_app(app)
flask_migrate.Migrate(app=app, db=models.db)



#Authentication config

user_datastore = flask_security.SQLAlchemySessionUserDatastore(session=models.db.session, user_model=models.User, role_model=models.Role)

security = flask_security.Security(app=app, datastore=user_datastore, register_form=StudentRegisterForm)

security.init_app(app=app,register_blueprint=False)




#Route Registrations here
app.register_blueprint(core_route, url_prefix = '/')
app.register_blueprint(api, url_prefix='/api/v1/')
app.register_blueprint(student_route, url_prefix='/student/')
app.register_blueprint(lecturer_route, url_prefix='/lecturer/')


if __name__ == '__main__':
    app.run(debug=True)