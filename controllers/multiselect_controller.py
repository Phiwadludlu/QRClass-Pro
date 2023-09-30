from flask import request, get_template_attribute
from controllers import test_db as ddb
import json

def handleTableByModule():
    data = request.data
    unloaded = json.loads(data)

    action = unloaded['action']
    selection = unloaded['value']
    returnType = unloaded['returnType']

    print(unloaded)

    if returnType=="module-table":
        table = get_template_attribute("macros/__table__.html","self")
        filtered_modules = [item for item in ddb.getAllAttendance() if item["code"] == selection[0]]
        return table(filtered_modules)
    else:
        return {}