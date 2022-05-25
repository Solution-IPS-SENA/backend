from src.middlewares.request_middleware import json_input
from src.middlewares.token_middleware import verify_rol
from flask import request, make_response, jsonify
from src.utils.functions import validate_input
from src.validators.historia_fonoaudiologia_validator import HistoriaFonoaudiologiaSchema
from src.services.historia_fonoaudiologia_service import HistoriaFonoaudiologiaService
from flask.views import MethodView

class HistoriaFonoaudiologiaController(MethodView):

    def __init__(self):
        self.validator = HistoriaFonoaudiologiaSchema()
        self.service = HistoriaFonoaudiologiaService()

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
        num_historia = request.args.get("num_historia")
        if valido:
            if num_historia == None:
                response, status = self.service.update(content, False)
            elif num_historia.isnumeric():
                num_historia = int(num_historia)
                if num_historia  > 0:
                    response, status = self.service.update(content, num_historia)
            else:
                response, status = ({"response": "num_historia debe de ser un número entero mayor que 0."}, 400)
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
        