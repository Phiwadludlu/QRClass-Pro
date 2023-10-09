from flask import Blueprint
from controllers.core_controller import index,create_tables,login, signUp, lecturer_sign_up, student_sign_up, proxy_redirect

core_route = Blueprint('core_routes',__name__)

core_route.get("/") (index)

core_route.get("/create-tables")(create_tables)

core_route.route("/register",methods=["GET","POST"]) (signUp)
core_route.route("/register/lecturer", methods=['GET','POST'])(lecturer_sign_up)
core_route.route("/register/student", methods=["GET", "POST"])(student_sign_up)
core_route.route("/redirect-proxy")(proxy_redirect)

