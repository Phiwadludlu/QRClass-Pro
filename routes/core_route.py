from flask import Blueprint
from controllers import core_controller as core_controller

core_route = Blueprint('core_routes',__name__)

core_route.get("/") (core_controller.index)
