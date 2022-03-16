from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models.paciente import Paciente
import jwt
from bcrypt import checkpw
from src.validators import login_validator
from os import getenv
 
class LoginController(MethodView):
    def __init__(self):
        self.model = Paciente()
        self.validator = login_validator.CreateLoginSchema()

    def post(self):
        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "No se ha recibido un json."
            }), 400)

        content = request.get_json()
        validation_errors = self.validator.validate(content)

        if validation_errors:
            return make_response(jsonify({
                "status": 400,
                "errors": validation_errors
            }), 400)

        bd_data = self.model.fetch_one(f"SELECT documento, password FROM paciente WHERE correo='{content.get('correo')}'", as_dict=True)

        if bd_data is None:
            return make_response(jsonify({
                "status": 422,
                "response": "El usuario no está registrado."
            }), 422)
            
        db_pass_bytes = bytes(bd_data.get("password"), 'utf8')
        pass_bytes = bytes(content.get("password"), 'utf8')
        
        if not checkpw(pass_bytes, db_pass_bytes):
            return make_response(jsonify({
                "status": 400,
                "response": "La contraseña es incorrecta."
            }), 400)

        token = jwt.encode(
                {"correo": content.get("correo"),
                    "documento": bd_data.get("documento"),
                    "rol": bd_data.get("rol")
                }, getenv("JWT_KEY"), "HS256")
        
        token_str = bytes.decode(token, 'utf8')

        return make_response(jsonify({
            "status": 200,
            "response": "Inicio de sesión satisfactorio",
            "token": f"{token_str}"
        }), 200)
