from src.middlewares.request_middleware import json_input
from src.middlewares.token_middleware import verify_rol
from flask import request, make_response, jsonify
from src.utils.functions import validate_input
from src.validators.historia_psicologia_validator import HistoriaPsicologiaSchema
from src.services.historia_psicologia_service import HistoriaPsicologiaService
from flask.views import MethodView

class HistoriaPsicologiaController(MethodView):

    def __init__(self):
        self.validator = HistoriaPsicologiaSchema()
        self.service = HistoriaPsicologiaService()

    @json_input
    #@verify_rol
    def post(self):
        content, valido = validate_input(self, request.get_json())
        nuevo_seguro = request.args.get("nuevo_seguro")
        if valido:
            if nuevo_seguro == None:
                response, status = self.service.create(content)
            elif nuevo_seguro not in ["0", "1"]:
                response = { "response": "Solo se aceptan 0 para False y 1 para True" }
                status = 400
            else:
                nuevo_seguro = bool(int(nuevo_seguro))
                response, status = self.service.create(content, nuevo_seguro)

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
        