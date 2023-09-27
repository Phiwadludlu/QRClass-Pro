from flask import Blueprint
from controllers.core_controller import index

core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)
