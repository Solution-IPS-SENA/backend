from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models.paciente import Paciente
from src.utils.db import db
from bcrypt import hashpw, gensalt
from src.validators import register_paciente_validator
import sqlalchemy
 
class RegisterPacienteController(MethodView):

    def __init__(self):
        self.validator = register_paciente_validator.CreateRegisterPacienteSchema()

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
                "response": errors
            }), 400)

        try:
            db.session.add(
                Paciente(
                    documento = content.get('documento'),
                    tipo_documento = content.get('tipo_documento'),
                    nombres = content.get('nombres'),
                    apellidos = content.get('apellidos'),
                    fecha_nacimiento = content.get('fecha_nacimiento'),
                    lugar_nacimiento = content.get('lugar_nacimiento'),
                    nacionalidad = content.get('nacionalidad'),
                    genero = content.get('genero'),
                    direccion = content.get('direccion'),
                    telefono = content.get('telefono'),
                    empresa = content.get('empresa'),
                    cargo = content.get('cargo'),
                    fecha_ingreso = content.get('fecha_ingreso'),
                    tiempo_cargo = content.get('tiempo_cargo'),
                    arl = content.get('arl'),
                    eps = content.get('eps'),
                    afp = content.get('afp'),
                    telefono_empresa = content.get('telefono_empresa'),
                    correo = content.get('correo'),
                    password = bytes.decode(hashpw(bytes(content.get('password'), encoding='utf8'), gensalt()), encoding='utf-8'),
                    rol = content.get('rol'),
                    foto = content.get('foto')
                )
            )
            db.session.commit()

            return make_response(jsonify({
                "status": 201,
                "response": "Paciente creado correctamente"
            }), 201)

        except sqlalchemy.exc.IntegrityError as e:
            print(e.hide_parameters)
            return make_response(jsonify({
                "status": 409,
                "response": "El documento y/o el correo ya se encuentran registrados."
            }), 409)
        
        except Exception as e:
            return make_response(jsonify({
                "status": 400,
                "response": str(e)
            }), 400)

