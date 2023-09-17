import os
import dotenv

#Loading environment variables
dotenv.load_dotenv()

FLASK_ENV = "development"
FLASK_APP = "app"

SECRET_KEY = os.getenv("SECRET_KEY")

#Database config 
SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
SQLALCHEMY_ENGINE_OPTIONS =  {
    "pool_pre_ping": True,
}
SQLALCHEMY_TRACK_MODIFICATION = False




#Authentication config
"""This configs handle all things authentication"""
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
REMEMBER_COOKIE_SAMESITE = "strict"
SESSION_COOKIE_SAMESITE = "strict"
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": False}