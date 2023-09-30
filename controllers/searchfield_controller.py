from flask import request, get_template_attribute
from controllers import test_db as ddb
import json

def handleTableByStudentNumber():
    data = request.data
    unloaded = json.loads(data)

    student_id = unloaded['value']

    table = get_template_attribute("macros/__table__.html","self")
    filtered_modules = ddb.getStudentAttendance(student_id)

    return table(filtered_modules)