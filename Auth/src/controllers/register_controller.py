from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models.paciente import Paciente
from bcrypt import hashpw, gensalt
from datetime import datetime
from src.validators import register_validator
 
class RegisterController(MethodView):

    def __init__(self):
        self.model = Paciente()
        self.validator = register_validator.Register()

    def post(self):
        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "No se ha recibido un json."
            }), 400)
            
        content = request.get_json()
        documento = content.get('documento')
        tipoDocumento = content.get('tipoDocumento')
        nombres = content.get('nombres')
        apellidos = content.get('apellidos')
        fechaNacimiento = content.get('fechaNacimiento')
        edad = content.get('edad')
        nacionalidad = content.get('nacionalidad')
        lugarNacimiento = content.get('lugarNacimiento')
        genero = content.get('genero')
        direccion = content.get('direccion')
        celular = content.get('celular')
        empresa = content.get('empresa')
        cargo = content.get('cargo')
        fechaIngreso = content.get('fechaIngreso')
        tiempoCargo = content.get('tiempoCargo')
        arl = content.get('arl')
        eps = content.get('eps')
        afp = content.get('afp')
        telefonoEmpresa = content.get('telefonoEmpresa')
        observaciones = content.get('observaciones')
        correo = content.get('correo')
        password = bytes(content.get('password'), encoding='utf8')
        rol = content.get('rol')
        join_at = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        hashed_pass = hashpw(password, gensalt())
        self.model.execute_query(
            f"""INSERT INTO paciente VALUES(
                '{documento}',
                '{tipoDocumento}',
                '{nombres}',
                '{apellidos}',
                '{fechaNacimiento}',
                '{edad}',
                '{nacionalidad}',
                '{lugarNacimiento}',
                '{genero}',
                '{direccion}',
                '{celular}',
                '{empresa}',
                '{cargo}',
                '{fechaIngreso}',
                '{tiempoCargo}',
                '{arl}',
                '{eps}',
                '{afp}',
                '{telefonoEmpresa}',
                '{observaciones}',
                '{correo}',
                '{bytes.decode(hashed_pass, 'utf8')}',
                '{rol}',
                '{join_at}',
                '{join_at}'
            )"""
        )
        return make_response(jsonify({
            "status": 201,
            "response": "Paciente creado correctamente"
        }), 201)
