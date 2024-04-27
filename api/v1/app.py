#!/usr/bin/python3
"""This is the flask module"""
from flask import Flask
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close():
    """Exits the db storage"""
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
    app.run(host=host, port=port, threaded=True)
