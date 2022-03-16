from flask import request, make_response, jsonify
from functools import wraps
from os import getenv
from jwt import decode, InvalidTokenError

"""
    :decorator @verify_token — Verifica el token enviado por cabecera y devuelve una autorización.
"""
def verify_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token: str = request.headers.get('Authorization', 'Auth')
        try:
            data = decode(token, getenv("JWT_KEY"), algorithms=["HS256"])
        except InvalidTokenError:
            return make_response(jsonify({
                "statusCode": 498,
                "message": "El token es inválido"
            }), 498)
        return func(*args, **kwargs)
    return wrapped
