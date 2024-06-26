#!/usr/bin/python3
"""
Created a flask app, registed app_view blueprint,
created a handler for 404 errors and handled
cross origin relationships.
"""

from api.v1.views import app_views
from flask import Flask, jsonify
import os
from models import storage
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    """Ends the current storage session"""

    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """Return a JSON response with status code 404"""

    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
