from flask import Blueprint
from controllers import lecturer_controller as lc
from controllers import multiselect_controller as mc
from controllers import searchfield_controller as sfc
from controllers import api_controller as apic

api = Blueprint("api_routes",__name__)

api.get("/qualification/all")(apic.send_all_qualifications)
api.get("/module/all")(apic.send_all_modules)
api.get("/attendance/all")(apic.send_all_attendance)

api.post("/config/multiselect") (mc.handleTableByModule)
api.post("/config/searchfield") (sfc.handleTableByStudentNumber)