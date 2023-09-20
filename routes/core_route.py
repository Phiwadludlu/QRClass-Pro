from flask import Blueprint
from controllers.mutliselect_controller import handleMultiSelect, handleSearchField, getAllItems # Multiselect Control - by m-mngadi
from controllers.core_controller import index, signIn
core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)
core_route.get('/sign_in')(signIn)


# Multiselect Control end.