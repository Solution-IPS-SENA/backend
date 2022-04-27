from flask import request, make_response, jsonify
from src.validators import login_validator
from src.models.paciente import Paciente
from src.models.empleado import Empleado
from src.models.medico import Medico
from flask.views import MethodView
from src.config import KEYS
from bcrypt import checkpw
import jwt
 
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

        tipos_usuario = [Paciente, Empleado, Medico]
        usuario_encontrado = False

        for i in range(len(tipos_usuario)):
            usuario = tipos_usuario[i].query.filter_by(correo=content.get('correo')).first()
            if usuario is not None:
                usuario_encontrado = True
                break;
        
        if not usuario_encontrado:
            return make_response(jsonify({
                    "status": 422,
                    "response": "El usuario no está registrado."
                }), 422)
            
        db_pass = bytes(usuario.password, 'utf8')
        pass_bytes = bytes(content.get("password"), 'utf8')
        
        if not checkpw(pass_bytes, db_pass):
            return make_response(jsonify({
                "status": 406,
                "response": "La contraseña es incorrecta."
            }), 406)

        token = jwt.encode(
                {
                    "correo": usuario.correo,
                    "documento": usuario.documento,
                    "rol": "EMPLEADO"
                }, KEYS.JWT, "HS256")
        
        token = bytes.decode(token, 'utf8')

        return make_response(jsonify({
            "status": 200,
            "response": "Inicio de sesión satisfactorio",
            "token": f"{token}"
        }), 200)