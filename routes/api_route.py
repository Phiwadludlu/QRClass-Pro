from flask import Blueprint
from controllers.mutliselect_controller import getAllItems, handleMultiSelect, handleSearchField

api = Blueprint("api_routes",__name__)

# Multiselect Control - by m-mngadi
api.get("/dropdown-items")(getAllItems)
api.post("/dropdown-config") (handleMultiSelect)
api.post("/searchfield-config") (handleSearchField)