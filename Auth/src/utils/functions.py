from flask import make_response, jsonify
from datetime import datetime
from src.config import APP

def time():
    return datetime.now().strftime(APP.DATETIME_FORMAT)

def validate_input(sender, content):
    errors = sender.validator.validate(content)
    if errors:
        return make_response(jsonify({
            "response": errors
        }), 400), False
    
    return content, True