from sqlalchemy.exc import IntegrityError
from bcrypt import hashpw, gensalt
from src.models.empleado_model import Empleado
from src.utils.instances import db

class EmpleadoService():
    
    def add(self, content):
        try:
            db.session.add(
                Empleado(
                    documento = content.get('documento'),
                    tipo_documento = content.get('tipo_documento'),
                    nombres = content.get('nombres'),
                    apellidos = content.get('apellidos'),
                    fecha_nacimiento = content.get('fecha_nacimiento'),
                    lugar_nacimiento = content.get('lugar_nacimiento'),
                    nacionalidad = content.get('nacionalidad'),
                    genero = content.get('genero'),
                    direccion = content.get('direccion'),
                    telefono = content.get("telefono"),
                    salario = content.get('salario'),
                    arl = content.get('arl'),
                    eps = content.get('eps'),
                    afp = content.get('afp'),
                    correo = content.get('correo'),
                    password = bytes.decode(hashpw(bytes(content.get('password'), encoding='utf8'), gensalt()), encoding='utf-8'),
                    rol = content.get('rol'),
                    foto = content.get('foto')
                )
            )
            db.session.commit()

            return (
                {
                    "response": "Empleado creado correctamente"
                },
                201
            )

        except IntegrityError as e:
            db.session.rollback()
            return (
                {
                    "response": "El documento y/o el correo ya se encuentran registrados."
                },
                409
            )
        
        except Exception as e:
            db.session.rollback()
            return (
                {
                    "response": str(e)
                },
                400
            )
