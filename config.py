import os
import dotenv

#Loading environment variables
dotenv.load_dotenv()

FLASK_ENV = "development"
FLASK_APP = "app"

SECRET_KEY = os.getenv("SECRET_KEY")

#Database config 
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qrcodepro_db_user:G4Z6Ro4W3XMLuXC6sPs9Xos7TUqLmthv@dpg-ckrokm81hnes7385pr90-a.oregon-postgres.render.com/qrcodepro_db'
SQLALCHEMY_ENGINE_OPTIONS =  {
    "pool_pre_ping": True,
}
SQLALCHEMY_TRACK_MODIFICATION = False




#Authentication config
"""This configs handle all things authentication"""
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
REMEMBER_COOKIE_SAMESITE = "strict"
SESSION_COOKIE_SAMESITE = "strict"

SECURITY_REGISTERABLE = False

SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": False}
SECURITY_POST_LOGIN_VIEW = "/redirect-proxy"
SECURITY_UNAUTHORIZED_VIEW = "/redirect-proxy"