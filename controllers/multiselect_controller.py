from flask import request, get_template_attribute
from controllers import api_controller as apic
import json

def handleTableByModule():
    data = request.data
    unloaded = json.loads(data)

    action = unloaded['action']
    selection = unloaded['value']
    returnType = unloaded['returnType']

    print(unloaded)

    if returnType=="module-table":
        attendance_data = json.loads(apic.send_all_attendance().data)
        table = get_template_attribute("macros/__table__.html","self")
        filtered_modules = [item for item in attendance_data if item["module_code"] == selection[0]]
        return table(filtered_modules)
    else:
        return {}