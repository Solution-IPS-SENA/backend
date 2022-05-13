from flask import make_response, jsonify, request
from datetime import date, datetime
from src.config import APP

def datetime(time = None):
    return datetime.now().strftime(APP.DATETIME_FORMAT if time is not None else APP.DATE_FORMAT) 

def validate_input(sender, content):
    errors = sender.validator.validate(content)
    if errors:
        return make_response(jsonify({
            "response": errors
        }), 400), False
    
    return content, True

def validate_dict(content):
    for key in content:
        if content[key] == None:
            return make_response(jsonify({
                "response": f"Tiene que enviar por parámetro de consulta las llaves: {content.values()}"
             }), 400), False

    return content, True

def generate_dict(keys):
    content = {}
    for key in keys:
        content[key] = request.args.get(key)
    return content
