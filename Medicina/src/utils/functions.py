from flask import make_response, jsonify
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