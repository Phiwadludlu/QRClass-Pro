from models import db



def create_tables():
    from app import app
    with app.app_context():
        db.create_all()
