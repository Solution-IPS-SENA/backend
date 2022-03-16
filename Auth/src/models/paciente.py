from src.utils.db import db
from datetime import datetime

class Paciente(db.Model):
    documento = db.Column(db.String(20), primary_key=True)
    tipoDocumento = db.Column(db.String(2), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    edad = db.Column(db.Integer, nullable=False)
    nacionalidad = db.Column(db.String(3), nullable=False)
    lugarNacimiento = db.Column(db.String(3), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    celular = db.Column(db.String(30), nullable=False)
    empresa = db.Column(db.String(45), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    cargo = db.Column(db.String(20), nullable=False)

    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
