from flask import Blueprint
from controllers.mutliselect_controller import getAllItems, handleMultiSelect, handleSearchField
from controllers.core_controller import lecturer_sign_up, student_sign_up

api = Blueprint("api_routes",__name__)

# Multiselect Control - by m-mngadi
api.get("/dropdown-items")(getAllItems)
api.post("/dropdown-config") (handleMultiSelect)
api.post("/searchfield-config") (handleSearchField)
api.route("/lecturer-form", methods=['GET','POST'])(lecturer_sign_up)
api.route("/student-form", methods=["GET", "POST"])(student_sign_up)