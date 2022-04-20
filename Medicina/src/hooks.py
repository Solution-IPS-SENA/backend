from flask import request, make_response, jsonify
from functools import wraps
from jwt import decode, InvalidTokenError
from src.config import KEYS

def verify_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token: str = request.headers.get('Authorization')
        if token:
            try:
                decode(token, KEYS.JWT, algorithms=["HS256"])
                return func(*args, **kwargs)
            except Exception as e:
                return make_response(jsonify({
                    "statusCode": 498,
                    "response": "Token verification failed",
                    "error": str(e)
                }), 498)
        return make_response(jsonify({
                "statusCode": 417,
                "response": "Send a header with a Authorization key"
            }), 417)
    return wrapped
