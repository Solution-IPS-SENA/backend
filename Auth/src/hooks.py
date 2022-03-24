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
        token: str = request.headers.get('Authorization')
        print(token)
        if token:
            try:
                decode(token, getenv("JWT_KEY"), algorithms=["HS256"])
                return func(*args, **kwargs)
            except InvalidTokenError:
                return make_response(jsonify({
                    "statusCode": 498,
                    "response": "El token es inválido"
                }), 498)
        return make_response(jsonify({
                "statusCode": 417,
                "response": "Cabecera inválida, no se encuetra el token de autenticación. (Authorization)"
            }), 417)
    return wrapped
