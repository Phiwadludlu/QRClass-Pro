from flask import request, get_template_attribute
from controllers import api_controller as apic
import json

def handleTableByStudentNumber():
    data = request.data
    unloaded = json.loads(data)

    student_id = unloaded['value']

    table = get_template_attribute("macros/__table__.html","self")
    filtered_modules = json.loads(apic.send_attendance_by_student_number(student_id).data)

    return table(filtered_modules)