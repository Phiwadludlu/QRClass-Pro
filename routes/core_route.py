from flask import Blueprint
from controllers.core_controller import index, studentAttendance, gettingStarted1, gettingStarted2
core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)
core_route.get('/student-attendance')(studentAttendance)
core_route.get("/getting-started-1") (gettingStarted1)
core_route.get("/getting-started-2") (gettingStarted2)