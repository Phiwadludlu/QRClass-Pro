from flask import Blueprint
from controllers.mutliselect_controller import handleMultiSelect, handleSearchField, getAllItems # Multiselect Control - by m-mngadi
from controllers.core_controller import index,create_tables,login, signUp
core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)

core_route.get("/create-tables")(create_tables)

core_route.route("/register",methods=["GET","POST"]) (signUp)

# Multiselect Control end.