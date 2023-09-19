from flask import Blueprint
from controllers.mutliselect_controller import handleMultiSelect, handleSearchField, getAllItems # Multiselect Control - by m-mngadi
from controllers.core_controller import index, studentAttendance, gettingstarted2
core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)
core_route.get('/student_attendance')(studentAttendance)
core_route.get("/getting_started2")(gettingstarted2)
# Multiselect Control - by m-mngadi
core_route.get("/dropdown-items")(getAllItems)
core_route.post("/dropdown-config") (handleMultiSelect)
core_route.post("/searchfield-config") (handleSearchField)
# Multiselect Control end.