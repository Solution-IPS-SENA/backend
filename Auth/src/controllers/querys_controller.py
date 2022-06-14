from src.middlewares.request_middleware import json_input
from flask import request, make_response, jsonify
from src.services.querys_service import QuerysService
from src.validators.query_validators import CreateQuerySchema
from flask.views import MethodView

class PacienteController(MethodView):

    def __init__(self):
        self.service = QuerysService()
        self.validator = CreateQuerySchema()

    @json_input
    def post(self):
        if request.is_json:
            content = request.get_json()
            errors = self.validator.validate(content)
            if not errors:
                response, status = self.service.obtenerPaciente(content.get("tipo_doc"), content.get("doc"))
                return make_response(jsonify(response), status)
            return make_response(jsonify({
                "response": str(errors),
            }), 400)

        return make_response(jsonify({
                "response": "Envie un json. ",
            }), 400)