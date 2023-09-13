from flask import Flask
from routes.core_route import core_route
from routes.api_route import api   

def create_app():
    app = Flask(__name__)
    app.config.from_object('config') 

    return app


#Flask App instane
app = create_app()


#Route Registrations here

app.register_blueprint(core_route, url_prefix = '/')
app.register_blueprint(api, url_prefix='/api/v1/')

if __name__ == '__main__':
    app.run(debug=True)