from src.middlewares.request_middleware import json_input
from flask import request, make_response, jsonify
from src.utils.functions import validate_input
from src.validators import login_validator
from src.services import login_service
from flask.views import MethodView

class LoginController(MethodView):

    def __init__(self):
        self.validator = login_validator.CreateLoginSchema()
        self.service = login_service.LoginService()

    @json_input
    def post(self):
        content, valido = validate_input(self, request.get_json())
        if valido:
            response, status = self.service.login(content)
            return make_response(jsonify(response), status)
        return content
