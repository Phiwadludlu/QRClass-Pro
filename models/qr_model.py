from models import db
from datetime import datetime

from sqlalchemy import Column,Integer,String,DateTime,Boolean

class QR(db.Model):
    __tablename__ = 'qr'
    id = Column(Integer(), primary_key=True)
    expiration_date = Column(DateTime, nullable=False)
    qr_url = Column(String(255))
    url_uuid = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, default=datetime.now())

    #Relationships

    session = db.relationship("ModuleSession", back_populates='qr')
