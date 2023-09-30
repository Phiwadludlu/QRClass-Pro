from flask import Blueprint
from controllers import lecturer_controller as lc
from controllers import multiselect_controller as mc
from controllers import searchfield_controller as sfc
from controllers import test_db as ddb

api = Blueprint("api_routes",__name__)

api.get("/qualification/all")(ddb.getAllQualifications)
api.get("/module/all")(ddb.getAllModules)
api.get("/attendance/all")(ddb.getAllAttendance)

api.post("/config/multiselect") (mc.handleTableByModule)
api.post("/config/searchfield") (sfc.handleTableByStudentNumber)