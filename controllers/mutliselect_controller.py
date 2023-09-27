from flask import render_template, request
from utils.multiselect_filter import filter
import json

def getAllQualifications():
    return [{'id':'BINCT1', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'code' : 'BINCT1', 'type':'qualification'},{'id':'DIIAD1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','code' : 'DIIAD1', 'type':'qualification'}]

def getAllModules():
    return [{'id':'SEN301','name' : 'Software Engineering', 'code' : 'SFEN301', 'type':'module'}, 
            {'id':'PRJB301','name' : 'Project B', 'code' : 'PRJB301', 'type':'module'}, 
            {'id':'MCHI301','name' : 'Machine Intelligence', 'code' : 'MCHI301', 'type':'module'}, 
            {'id':'PJMN301','name' : 'Project Management', 'code' : 'PJMN301', 'type':'module'},
            {'id':'PBDV301','name' : 'Platform Based Programming', 'code' : 'PBDV301', 'type':'module'}]

def handleMultiselectDropdown():
    data = request.data
    unpacked = json.loads(json.loads(data))

    tags = unpacked['tags']
    dropdown_items = unpacked['dropdown_items']
    limit=unpacked['limit']

    print(dropdown_items)
    
    return render_template("components/dropdown/multiselect.html", dropdown_items=dropdown_items, tags=tags, limit=limit)

def handleMultiselectSearch():
    if request.method == "POST":
        data = request.data
        unpacked = json.loads(json.loads(data))

        text = unpacked['value']
        dropdown_items = unpacked['dropdown_items']
        tags = unpacked['tags']
        limit=unpacked['limit']

        print(unpacked)

        items = filter(text, dropdown_items)

        if items:
            return render_template("components/dropdown/dropdown-item.html", dropdown_items=items, tags=tags, limit=limit)
        elif len(items) == 0:
            return "<p class='px-4 my-1 d-flex justify-content-center text-body-tertiary'>No match found</p>"
        elif text == "":
            return render_template("components/dropdown/dropdown-item.html", dropdown_items=dropdown_items, tags=tags, limit=limit)