from src.utils.instances import db
from src.utils.functions import time

class Empleado(db.Model):

    __tablename__ = 'empleados'

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
    salario = db.Column(db.Numeric, nullable=False)
    arl = db.Column(db.String(45), nullable=False)
    eps = db.Column(db.String(45), nullable=False)
    afp = db.Column(db.String(45), nullable=False)
    correo = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default="EMPLEADO")
    foto = db.Column(db.String(150), nullable=True)
    join_at = db.Column(db.DateTime, nullable=False, default=time())
    last_login = db.Column(db.DateTime, nullable=False, default=time())

    def __init__(
            self, documento, tipo_documento, nombres,  apellidos,
            fecha_nacimiento, lugar_nacimiento, nacionalidad, 
            genero, direccion, telefono, salario, arl, eps, afp, 
            correo, password, foto = None
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
        self.salario = salario
        self.arl = arl
        self.eps = eps
        self.afp = afp
        self.correo = correo
        self.password = password
        self.foto = foto

    def __str__(self):
        return f"""EMPELADO:
    documento = {self.documento}
    tipo_documento = {self.tipo_documento}
    nombres = {self.nombres}
    apellidos = {self.apellidos}
    fecha_nacimiento = {self.fecha_nacimiento}
    lugar_nacimiento = {self.lugar_nacimiento}
    nacionalidad = {self.nacionalidad}
    genero = {self.genero}
    direccion = {self.direccion}
    salario = {self.salario}
    arl = {self.arl}
    eps = {self.eps}
    afp = {self.afp}
    correo = {self.correo}
    password = {self.password}
    foto = {self.foto}"""
