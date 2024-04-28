#!/usr/bin/python3
"""States module"""
from models.state import State
from flask import abort, jsonify, make_response, request
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """Retrieves a list of all state objects"""
    al = storage.all(State)
    ls = []
    for state in al.values():
        ls.append(state.to_dict())
    return jsonify(ls)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a state object based on id"""
    rez = storage.get(State, state_id)
    if rez is None:
        abort(404)
    return jsonify(rez.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a state object based on id"""
    rez = storage.get(State, state_id)
    if rez is None:
        abort(404)
    storage.delete(rez)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """Creates a new state obj"""
    dat = request.get_json()
    if not dat:
        abort(400, "Not a JSON")
    if 'name' not in dat:
        abort(400, "Missing name")
    ob = State(**dat)
    ob.save()
    return jsonify(ob.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['UPDATE'], strict_slashes=False)
def update_state(state_id):
    """Updates a state"""
    ob = storage.get(State, state_id)
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
