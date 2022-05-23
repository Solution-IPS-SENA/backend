from marshmallow import Schema, fields
from marshmallow import validate
from src.config import APP
from src.models.anexos import anexos

class BaseSchema():
    documento = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    tipo_documento = fields.Str(required=True, validate=lambda x: x in anexos.TIPO_DE_DOCUMENTO)
    nombres = fields.Str(required=True, validate=validate.Length(max=200))
    apellidos = fields.Str(required=True, validate=validate.Length(max=200))
    fecha_nacimiento = fields.DateTime(required=True, format=APP.DATE_FORMAT)
    lugar_nacimiento = fields.Str(required=True, validate=lambda x: x in anexos.LUGAR_DE_NACIMIENTO)
    nacionalidad = fields.Str(required=True, validate=lambda x: x in anexos.PAISES)
    genero = fields.Str(required=True, validate=lambda x: x in anexos.GENERO)
    direccion = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    telefono = fields.Str(required=True, validate=validate.Length(min=1, max=30))
    arl = fields.Str(required=True, validate=lambda x: x in anexos.ARL)
    eps = fields.Str(required=True, validate=lambda x: x in anexos.EPS)
    afp = fields.Str(required=True, validate=lambda x: x in anexos.AFP)
    correo = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(max=200))
    rol = fields.Str(required=True, validate=validate.Length(max=20))
    foto = fields.Str(required=False, validate=validate.Length(max=150))

class CreateRegisterEmpleadoSchema(BaseSchema, Schema):
    salario = fields.Number(required=True)
    
class CreateRegisterMedicoSchema(BaseSchema, Schema):
    salario = fields.Number(required=True)
    tp = fields.Str(required=True)
    rethus = fields.Str(required=True)
    secretaria_salud = fields.Str(required=True)

class CreateRegisterPacienteSchema(BaseSchema, Schema):
    empresa = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    cargo = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    fecha_ingreso = fields.Date(required=True)
    tiempo_cargo = fields.Str(required=True)
    telefono_empresa = fields.Str(required=True, validate=validate.Length(min=1, max=45))

class CreateRegisterEmpresaSchema(Schema):
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    nit = fields.Str(required=True, validate=validate.Length(min=1, max=10))
    telefono = fields.Str(required=True, validate=validate.Length(min=1, max=15))
    correo = fields.Str(required=True, validate=validate.Email())
    direccion = fields.Str(required=True, validate=validate.Length(min=1, max=100))
