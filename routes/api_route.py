from flask import Blueprint
from controllers import lecturer_controller as lc
from controllers import multiselect_controller as mc
from controllers import searchfield_controller as sfc
from controllers import api_controller as apic
from services import generate_qr_service as qrs

api = Blueprint("api_routes",__name__)

api.get("/qualification/all")(apic.send_all_qualifications)
api.get("/module/all")(apic.send_all_modules)
api.get("/attendance/all")(apic.send_all_attendance)
api.get("/timeslots/all")(apic.send_all_timeslot)
api.post("/timeslots/module")(apic.send_timeslots_by_module)
api.post("/module/add")(apic.add_module)

api.post("/config/multiselect") (mc.handleTableByModule)
api.post("/config/searchfield") (sfc.handleTableByStudentNumber)

api.post("/qr/generate")(qrs.generate_qr_code)
api.post("/qr/verify")(qrs.verify_qr_code)