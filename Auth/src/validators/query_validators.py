from marshmallow import Schema, fields
from marshmallow import validate
from src.models.anexos import anexos

class CreateQuerySchema(Schema):
    tipo_documento = fields.Str(required=True, validate=lambda x: x in anexos.TIPO_DOCUMENTO)
    documento = fields.Str(required=True, validate=validate.Length(min=1, max=12))
