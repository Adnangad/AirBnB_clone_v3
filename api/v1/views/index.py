#!/usr/bin/python3
""" Web app """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_stat():
    """ Returns status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count():
    """ gets  number of each objects """
    clas = [Amenity, City, Place, Review, State, User]
    name = ["amenities", "cities", "places", "reviews", "states", "users"]

    count = {}
    for i in range(len(clas)):
        count[name[i]] = storage.count(clas[i])

    return jsonify(count)
