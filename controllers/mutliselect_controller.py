from flask import render_template, request
from utils.multiselect_filter import filter
import json

def getAllItems():
    return [{'id':'chk-0', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'level' : '3', 'code' : 'BINCT'},{'id':'chk-1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','level': '2', 'code' : 'DIIAD1'}]

def handleMultiSelect():
    data = request.data
    unpacked = json.loads(json.loads(data))

    tags = unpacked['tags']
    dropdown_items = unpacked['dropdown_items']
    limit=unpacked['limit']

    print(dropdown_items)
    
    return render_template("components/dropdown/multiselect.html", dropdown_items=dropdown_items, tags=tags, limit=limit)

def handleSearchField():
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