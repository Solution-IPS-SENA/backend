from marshmallow import Schema, fields
from marshmallow import validate

class CreateLoginSchema(Schema):
    correo = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=4, max=200))
