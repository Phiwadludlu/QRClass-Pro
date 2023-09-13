from flask import Blueprint
from controllers.mutliselect_controller import handleMultiSelect, handleSearchField, getAllItems # Multiselect Control - by m-mngadi
from controllers.core_controller import index, studentAttendance
core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)
core_route.get('/student_attendance')(studentAttendance)
# Multiselect Control - by m-mngadi
core_route.get("/dropdown-items")(getAllItems)
core_route.post("/dropdown-config") (handleMultiSelect)
core_route.post("/searchfield-config") (handleSearchField)
# Multiselect Control end.