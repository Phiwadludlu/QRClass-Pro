from flask import Flask

#Route imports here
from routes.core_route import core_route
from routes.api_route import api   
from routes.student_route import student_route

def create_app():
    app = Flask(__name__)
    app.config.from_object('config') 

    return app


#Flask App instane
app = create_app()


#Route Registrations here

app.register_blueprint(core_route, url_prefix = '/')
app.register_blueprint(api, url_prefix='/api/v1/')
app.register_blueprint(student_route, url_prefix='/student/')


if __name__ == '__main__':
    app.run(debug=True)