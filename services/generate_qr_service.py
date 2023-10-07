
from models.session_model import ModuleSession


class QRService:

    _code = ""

    def __init__(self, session:ModuleSession) -> None:
        
        pass

    def generate_qr_code(self)-> str:

        #Add logic to generate unique qr code
        #should return string
        pass
        
    
    def verify_qr_code(self, code)-> bool:

        #Add logic to verify qr service
        #should return True or False
        pass