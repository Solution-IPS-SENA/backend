from src.middlewares.request_middleware import json_input
from src.middlewares.token_middleware import verify_rol
from flask import request, make_response, jsonify
from src.utils.functions import validate_input
from src.validators.historia_medica_validator import HistoriaMedicaSchema
from src.services.historia_medica_service import HistoriaMedicaService
from flask.views import MethodView

class HistoriaMedicaController(MethodView):

    def __init__(self):
        self.validator = HistoriaMedicaSchema()
        self.service = HistoriaMedicaService()

    @json_input
    #@verify_rol
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.create(content)
            return make_response(jsonify(response), status)
        return content

    @json_input
    #@verify_rol
    def put(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.update(content)
            return make_response(jsonify(response), status)
        return content

    #@verify_rol
    def get(self):
        if not request.args.get("doc"):
            return make_response(jsonify({
                "response": "Envie un parametro de ruta 'doc'"
            }), 400)
        response, status = self.service.get(request.args.get("doc"))
        return make_response(jsonify(response), status)
        