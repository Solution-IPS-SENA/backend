from flask import make_response, request, jsonify
from functools import wraps

def json_input(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not request.is_json:
            return make_response(jsonify({
                "response": "No se ha recibido un json."
            }), 400)

        return func(*args, **kwargs)

    return wrapped