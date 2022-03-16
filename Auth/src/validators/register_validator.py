from marshmallow import Schema, fields
from marshmallow import validate, ValidationError

class CreateRegisterSolutionSchema(Schema):
    documento = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    tipoDocumento = fields.Str(required=True, validate=lambda tipo: tipo.upper() in ("CC", "TI", "RC", "CE", "CD"))
    fecha_nacimiento = fields.DateTime(required=True)
    edad = fields.Int(required=True, validate=validate.Range(min=0, max=101))
    nacionalidad = fields.Str(required=True, validate=lambda nacionalidad : nacionalidad == "colombia")
    lugarNacimiento = fields.Str(required=True)
    genero = fields.Str(required=True, validate=validate.ContainsOnly(['h', 'm']))
    direccion = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    telefono = fields.Str(required=True, validate=validate.Length(min=1, max=30))
    empresa = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    cargo = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    fecha_Ingreso = fields.DateTime(required=True)
    tiempo_Cargo = fields.DateTime(required=True)
    arl = fields.Str(required=True)
    eps = fields.Str(required=True)
    afp = fields.Str(required=True)
    correo = fields.Str(required=True, validate=validate.Email())
    telefono_Empresa = fields.Str(required=True, validate=validate.Length(min=1, max=45))
