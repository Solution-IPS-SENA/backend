from flask import request, make_response, jsonify
from functools import wraps
from jwt import decode
from src.config import KEYS

def verify_rol(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token: str = request.headers.get('Authorization')
        if token:
            try:
                decodificado = decode(token, KEYS.JWT, algorithms=["HS256"])
                if decodificado["rol"] in ["MEDICO", "EMPLEADO"]:
                    return func(*args, **kwargs)
                return make_response(jsonify({
                    "statusCode": 401,
                    "response": "Permisos insuficientes",
                }), 401)
            except Exception as e:
                return make_response(jsonify({
                    "statusCode": 498,
                    "response": "Verificacion de token fallida",
                    "error": str(e)
                }), 498)
        return make_response(jsonify({
                "statusCode": 417,
                "response": "Envie un header con un token de autorización"
            }), 417)
    return wrapped
