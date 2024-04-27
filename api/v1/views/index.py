#!/usr/bin/python3
"""
Web app
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def return_status():
    """returns status"""
    return jsonify(status='OK')
