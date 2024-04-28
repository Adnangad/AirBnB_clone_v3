#!/usr/bin/python3
"""States module"""
from models.amenity import Amenity
from flask import abort, jsonify, make_response, request
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenity():
    """Retrieves a list of all state objects"""
    al = storage.all(Amenity)
    ls = []
    for amenity in al.values():
        ls.append(amenity.to_dict())
    return jsonify(ls)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a state object based on id"""
    rez = storage.get(Amenity, amenity_id)
    if rez is None:
        abort(404)
    return jsonify(rez.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a state object based on id"""
    rez = storage.get(Amenity, amenity_id)
    if rez is None:
        abort(404)
    storage.delete(rez)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """Creates a new state obj"""
    dat = request.get_json()
    if not dat:
        abort(400, "Not a JSON")
    if 'name' not in dat:
        abort(400, "Missing name")
    ob = Amenity(**dat)
    ob.save()
    return jsonify(ob.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['UPDATE'], strict_slashes=False)
def update_amenity(amenity_id):
    """Updates a state"""
    ob = storage.get(Amenity, amenity_id)
    if ob is None:
        abort(404)
    nw = request.get_json()
    if not nw:
        abort(400, "Not a JSON")
     for key, value in nw.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(ob, key, value)
    ob.save()
    return jsonify(ob.to_dict()), 200
