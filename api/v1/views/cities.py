#!/usr/bin/python3
"""Cities module"""
from models.state import State
from models.cities import City
from flask import abort, jsonify, make_response, request
from models import storage
from api.v1.views import app_views


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a city objects"""
    al = storage.get(City, city_id)
    if al is None:
        abort(404)
    return jsonify(al.to_dict())


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_city(state_id):
    """Retrieves a city object based on id"""
    rez = storage.get(State, state_id)
    if rez is None:
        abort(404)
    ls = []
    for city in rez.cities:
        ls.append(city.to_dict())
    return jsonify(ls)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a city object based on id"""
    rez = storage.get(City, city_id)
    if rez is None:
        abort(404)
    storage.delete(rez)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """Creates a new city obj"""
    rez = storage.get(State, state_id)
    if rez is None:
        abort(404)
    dat = request.get_json()
    if not dat:
        abort(400, "Not a JSON")
    if 'name' not in dat:
        abort(400, "Missing name")
    ob = City(**dat)
    ob.state_id = rez.id
    ob.save()
    return jsonify(ob.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['UPDATE'], strict_slashes=False)
def update_city(city_id):
    """Updates a city"""
    ob = storage.get(City, city_id)
    if not ob:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(ob, key, value)
    ob.save()
    return jsonify(ob.to_dict()), 200
