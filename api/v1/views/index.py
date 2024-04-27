#!/usr/bin/python3
"""Web App"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def return_status():
    stat = {"status": "OK"}
    return jsonify(stat)
