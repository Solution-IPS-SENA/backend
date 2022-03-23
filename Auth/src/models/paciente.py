from src.utils.db import db
from datetime import datetime

class Paciente(db.Model):
    documento = db.Column(db.String(20), primary_key=True)
    tipo_documento = db.Column(db.String(2), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    lugar_nacimiento = db.Column(db.String(3), nullable=False)
    nacionalidad = db.Column(db.String(3), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    empresa = db.Column(db.String(45), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    tiempo_cargo = db.Column(db.String(100), nullable=False)
    arl = db.Column(db.String(45), nullable=False)
    eps = db.Column(db.String(45), nullable=False)
    afp = db.Column(db.String(45), nullable=False)
    telefono_empresa = db.Column(db.String(45), nullable=False)
    correo = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    foto = db.Column(db.String(150), nullable=True)
    join_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))

    def __init__(
        self, documento, tipo_documento, nombres,  apellidos,
        fecha_nacimiento, lugar_nacimiento, nacionalidad, 
        genero, direccion, telefono, empresa, cargo, fecha_ingreso,
        tiempo_cargo, arl, eps, afp, telefono_empresa, correo,
        password, rol, foto = None
        ):
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.nacionalidad = nacionalidad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.empresa = empresa
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.tiempo_cargo = tiempo_cargo
        self.arl = arl
        self.eps = eps
        self.afp = afp
        self.telefono_empresa = telefono_empresa
        self.correo = correo
        self.password = password
        self.rol = rol
        self.foto = foto
