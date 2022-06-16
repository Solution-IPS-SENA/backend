from src.services import empleado_service, medico_service, paciente_service, empresa_service
from src.middlewares.request_middleware import json_input
from src.middlewares.token_middleware import verify_rol
from src.utils.functions import validate_input
from flask import request, make_response, jsonify
from src.validators import register_validator
from flask.views import MethodView

class RegisterPacienteController(MethodView):

    # decorators = [verify_rol]

    def __init__(self):
        self.validator = register_validator.CreateRegisterPacienteSchema()
        self.service = paciente_service.PacienteService()

    @json_input
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.add(content)
            return make_response(jsonify(response), status)
        return content
        

class RegisterMedicoController(MethodView):

    # decorators = [verify_rol]

    def __init__(self):
        self.validator = register_validator.CreateRegisterMedicoSchema()
        self.service = medico_service.MedicoService()

    @json_input
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.add(content)
            return make_response(jsonify(response), status)
        return content

class RegisterEmpresaController(MethodView):
    
    # decorators = [verify_rol]

    def __init__(self):
        self.validator = register_validator.CreateRegisterEmpresaSchema()
        self.service = empresa_service.EmpresaService()
    
    @json_input
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.add(content)
            return make_response(jsonify(response), status)
        return content

class RegisterEmpleadoController(MethodView):

    def __init__(self):
        self.validator = register_validator.CreateRegisterEmpleadoSchema()
        self.service = empleado_service.EmpleadoService()

    @json_input
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.add(content)
            return make_response(jsonify(response), status)
        return content
