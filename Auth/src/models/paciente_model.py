from src.utils.instances import db
from src.utils.functions import time

class Paciente(db.Model):

    __tablename__ = 'pacientes'

    documento = db.Column(db.String(12), primary_key=True)
    tipo_documento = db.Column(db.String(2), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    lugar_nacimiento = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(3), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    tiempo_cargo = db.Column(db.String(100), nullable=False)
    arl = db.Column(db.String(100), nullable=False)
    eps = db.Column(db.String(100), nullable=False)
    afp = db.Column(db.String(100), nullable=False)
    telefono_empresa = db.Column(db.String(45), nullable=False)
    correo = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default="PACIENTE")
    foto = db.Column(db.String(150), nullable=True)
    join_at = db.Column(db.DateTime, nullable=False, default=time())
    last_login = db.Column(db.DateTime, nullable=False, default=time())

    def __init__(
            self, documento, tipo_documento, nombres,  apellidos,
            fecha_nacimiento, lugar_nacimiento, nacionalidad, 
            genero, direccion, telefono, empresa, cargo, fecha_ingreso,
            tiempo_cargo, arl, eps, afp, telefono_empresa, correo,
            password, foto = None
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
        self.foto = foto

    def to_dict(self):
        return dict(
            documento=self.documento,
            tipo_documento=self.tipo_documento,
            nombres=self.nombres,
            apellidos=self.apellidos,
            fecha_nacimiento=str(self.fecha_nacimiento),
            lugar_nacimiento=self.lugar_nacimiento,
            nacionalidad=self.nacionalidad,
            genero=self.genero,
            direccion=self.direccion,
            telefono=self.telefono,
            empresa=self.empresa,
            cargo=self.cargo,
            fecha_ingreso=str(self.fecha_ingreso),
            tiempo_cargo=self.tiempo_cargo,
            arl=self.arl,
            eps=self.eps,
            afp=self.afp,
            telefono_empresa=self.telefono_empresa,
            correo=self.correo,
            password=self.password,
            foto=self.foto
        )
