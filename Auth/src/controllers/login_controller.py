from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models.paciente import Paciente
import jwt
from bcrypt import checkpw
from src.validators import login_validator
from os import getenv
 
class LoginController(MethodView):

    def __init__(self):
        self.validator = login_validator.CreateLoginSchema()

    def post(self):
        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "No se ha recibido un json."
            }), 400)

        content = request.get_json()
        errors = self.validator.validate(content)

        if errors:
            return make_response(jsonify({
                "status": 400,
                "errors": errors
            }), 400)

        paciente = Paciente.query.filter_by(correo=content.get('correo')).first()
        if paciente is None:
            return make_response(jsonify({
                "status": 422,
                "response": "El usuario no está registrado."
            }), 422)
            
        db_pass = bytes(paciente.password, 'utf8')
        pass_bytes = bytes(content.get("password"), 'utf8')
        
        if not checkpw(pass_bytes, db_pass):
            return make_response(jsonify({
                "status": 406,
                "response": "La contraseña es incorrecta."
            }), 406)

        token = jwt.encode(
                {
                    "correo": paciente.correo,
                    "documento": paciente.documento,
                    "rol": paciente.rol
                }, getenv("JWT_KEY"), "HS256")
        
        token = bytes.decode(token, 'utf8')

        return make_response(jsonify({
            "status": 200,
            "response": "Inicio de sesión satisfactorio",
            "token": f"{token}"
        }), 200)
