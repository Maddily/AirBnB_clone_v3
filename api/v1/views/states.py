#!/usr/bin/python3
"""
This module handles all default RESTFul API actions:
    - Retrieves a list of all State objects
    - Retrieves a State object
    - Creates a State object
    - Updates a State object
    - Deletes a State object
"""

from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves a list of all State objects"""

    states = [state.to_dict() for state in storage.all(State).values()]

    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    state.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state(state_id):
    """Creates a State object"""

    data = request.get_json()

    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)

    state = State(**data)
    state.save()

    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""

    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    data = request.get_json()

    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for k, v in data.items:
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(state, k, v)
    state.save()

    return make_response(jsonify(state.to_dict()), 200)
