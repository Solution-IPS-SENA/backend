from sqlalchemy.exc import IntegrityError
from src.models.medico_model import Medico
from bcrypt import hashpw, gensalt
from src.utils.instances import db

class MedicoService():

    def add(self, content):
        try:
            db.session.add(
                Medico(
                    documento=content.get('documento'),
                    tipo_documento=content.get('tipo_documento'),
                    nombres=content.get('nombres'),
                    apellidos=content.get('apellidos'),
                    fecha_nacimiento=content.get('fecha_nacimiento'),
                    lugar_nacimiento=content.get('lugar_nacimiento'),
                    nacionalidad=content.get('nacionalidad'),
                    genero=content.get('genero'),
                    direccion=content.get('direccion'),
                    telefono=content.get('telefono'),
                    salario=content.get('salario'),
                    tp=content.get('tp'),
                    rethus=content.get('rethus'),
                    secretaria_salud=content.get('secretaria_salud'),
                    arl=content.get('arl'),
                    eps=content.get('eps'),
                    afp=content.get('afp'),
                    correo=content.get('correo'),
                    password=bytes.decode(hashpw(bytes(content.get('password'), encoding='utf8'), gensalt()), encoding='utf-8'),
                    foto=content.get('foto')
                )
            )
            db.session.commit()

            return (
                {
                    "response": "Médico creado correctamente"
                },
                201
            )

        except IntegrityError as e:
            db.session.rollback()
            return (
                {
                    "response": "El documento y/o el correo ya se encuentran registrados."
                },
                409)

        except Exception as e:
            db.session.rollback()
            return (
                {
                    "response": str(e)
                },
                400)
