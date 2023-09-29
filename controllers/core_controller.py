
"""The controllers module is for business logic"""
from flask import render_template
from controllers.mutliselect_controller import getAllQualifications, getAllModules

def index():
    return render_template('layouts/LandingPage_layout.html')