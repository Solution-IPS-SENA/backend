from src.utils.instances import db
from src.utils.functions import time

class Empresa(db.Model):

    __tablename__ = 'empresas'

    nit = db.Column(db.String(100), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    correo = db.Column(db.String(150), nullable=False, unique=True)
    direccion = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default="EMPRESA")
    join_at = db.Column(db.DateTime, nullable=False, default=time())
    last_login = db.Column(db.DateTime, nullable=False, default=time())

    def __init__(
            self, nit, nombre,  telefono, correo, direccion
        ):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion


    def __str__(self):
        return f"""Empresa:
    nit = {self.nit}
    nombre = {self.nombre}
    telefono = {self.telefono}
    correo = {self.correo}
    direccion = {self.direccion}
    """
