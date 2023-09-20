
"""The controllers module is for business logic"""
from flask import render_template

def index():
    dropdown_items = [{'id':'chk-0', 'name' : 'BACHELOR OF INF & COM TECHNOLOGY', 'level' : '3', 'code' : 'BINCT'},{'id':'chk-1','name':'DIPLOMA IN ICT APPLICATIONS DEVELOPMENT','level': '2', 'code' : 'DIIAD1'}];
    limit = 2
    return render_template('layouts/LandingPage_layout.html', dropdown_items=dropdown_items,tags=[],limit=limit)

def signIn ():
    return render_template('layouts/SignIn_layout.html')