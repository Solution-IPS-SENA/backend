from marshmallow import Schema, fields
from marshmallow import validate

class CreateRegisterEmpleadoSchema(Schema):
    documento = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    tipo_documento = fields.Str(required=True, validate=lambda x: True if x in ["CC", "TI", "RC", "CE", "CD"] else False)
    nombres = fields.Str(required=True, validate=validate.Length(max=200))
    apellidos = fields.Str(required=True, validate=validate.Length(max=200))
    fecha_nacimiento = fields.Date(required=True)
    lugar_nacimiento = fields.Str(required=True, validate=validate.Length(equal=3))
    nacionalidad = fields.Str(required=True, validate=validate.Length(equal=3))
    genero = fields.Str(required=True, validate=validate.ContainsOnly(['M', 'F']))
    direccion = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    telefono = fields.Str(required=True, validate=validate.Length(min=1, max=30))
    salario = fields.Integer(required=True)
    arl = fields.Str(required=True)
    eps = fields.Str(required=True)
    afp = fields.Str(required=True)
    correo = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(max=200))
    rol = fields.Str(required=True, validate=validate.Length(max=20))
    foto = fields.Str(required=False, validate=validate.Length(max=150))
