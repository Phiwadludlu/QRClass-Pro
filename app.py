from flask import Flask
from routes.core_route import core_route
from routes.api_route import api   
import flask_security
import models
def create_app():
    app = Flask(__name__)
    app.config.from_object('config') 

    return app


#Flask App instane
app = create_app()

#Linking models to app
models.db.init_app(app)


#Authentication config

user_datastore = flask_security.SQLAlchemySessionUserDatastore(session=models.db.session, user_model=models.User, role_model=models.Role)
security = flask_security.Security(app=app, datastore=user_datastore)
security.init_app(app=app,register_blueprint=False)




#Route Registrations here

app.register_blueprint(core_route, url_prefix = '/')
app.register_blueprint(api, url_prefix='/api/v1/')

if __name__ == '__main__':
    app.run(debug=True)