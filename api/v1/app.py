#!/usr/bin/python3
"""
This is the flask module
"""
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)

# Create a CORS instance allowing /* for 0.0.0.0
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close(error):  # Added 'error' parameter here
    """ Exits the db storage """
    storage.close()


@app.errorhandler(404)
def err(error):
    """ Handles the 404 error """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
