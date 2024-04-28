#!/usr/bin/python3
"""This is the flask module"""
import models
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, make_response


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close():
    """ Exits the db storage """
    models.storage.close()


@app.errorhandler(404)
def err(error):
    """ Handles the 404 error """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
    app.run(host=host, port=port, threaded=True)
