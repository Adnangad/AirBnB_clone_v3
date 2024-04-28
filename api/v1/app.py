#!/usr/bin/python3
"""
Flask API Module

This module initializes a Flask application to serve an API. It registers blueprints for API endpoints,
configures CORS (Cross-Origin Resource Sharing), and sets up error handling.

The API allows clients to interact with resources managed by the application, and it supports 
cross-origin requests from any origin (0.0.0.0) using CORS.

Usage:
    To run the API server, execute this script directly:
        $ python3 <script_name.py>

    Environment variables:
        - HBNB_API_HOST: Host IP address. Default is '0.0.0.0'.
        - HBNB_API_PORT: Port number. Default is 5000.

Endpoints:
    - '/api/v1/*': API endpoints for version 1 of the API.
    - Error handling: 404 error returns a JSON response with {'error': 'Not found'}.

Dependencies:
    - Flask: Web application framework.
    - Flask-CORS: CORS support for Flask applications.

Note:
    This script is intended to serve as the entry point for the Flask application and should be executed
    to start the API server.
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
