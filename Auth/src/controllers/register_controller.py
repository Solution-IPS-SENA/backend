from src.services import empleado_service, medico_service, paciente_service
from flask import request, make_response, jsonify
from src.validators import register_validator
from src.middlewares.token_middleware import verify_rol
from flask.views import MethodView

def validate_data(sender):
    if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "No se ha recibido un json."
            }), 400)
    content = request.get_json()
    errors = sender.validator.validate(content)
    if errors:
        return make_response(jsonify({
            "status": 400,
            "response": errors
        }), 400)
    
    return content

class RegisterPacienteController(MethodView):

    decorators = [verify_rol]

    def __init__(self):
        self.validator = register_validator.CreateRegisterPacienteSchema()
        self.service = paciente_service.PacienteService()

    def post(self):
        content = validate_data(self)
        response, status = self.service.add(content)
        return make_response(jsonify(response), status)

class RegisterMedicoController(MethodView):

    decorators = [verify_rol]

    def __init__(self):
        self.validator = register_validator.CreateRegisterMedicoSchema()
        self.service = medico_service.MedicoService()

    def post(self):
        content = validate_data(self)
        response, status = self.service.add(content)
        return make_response(jsonify(response), status)


class RegisterEmpleadoController(MethodView):

    def __init__(self):
        self.validator = register_validator.CreateRegisterEmpleadoSchema()
        self.service = empleado_service.EmpleadoService()

    def post(self):
        content = validate_data(self)
        response, status = self.service.add(content)
        return make_response(jsonify(response), status)
