from flask import Blueprint
from controllers.mutliselect_controller import getAllQualifications, getAllModules, handleMultiselectDropdown, handleMultiselectSearch

api = Blueprint("api_routes",__name__)

api.get("/qualification/all")(getAllQualifications)
api.get("/module/all")(getAllModules)
api.post("/config/multiselect/dropdown") (handleMultiselectDropdown)
api.post("/config/multiselect/search") (handleMultiselectSearch)