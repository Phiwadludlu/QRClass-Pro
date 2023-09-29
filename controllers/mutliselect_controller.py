from flask import get_template_attribute, render_template, request
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
    module_tags_length = unpacked['module_tags_length']
    qualification_tags_length = unpacked['qualification_tags_length']

    print('module_count [%s] | qualification_count [%s]' % (module_tags_length, qualification_tags_length))

    multiselect = get_template_attribute("macros/__multiselect__.html","self")

    return multiselect(dropdown_items, tags, limit, qualification_tags_length, module_tags_length)

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