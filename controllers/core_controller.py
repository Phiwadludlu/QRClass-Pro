
"""The controllers module is for business logic"""
from flask import render_template

def index():
    return render_template('layouts/LandingPage_layout.html')