from sqlalchemy.exc import IntegrityError
from bcrypt import hashpw, gensalt
from src.models.empresa_model import Empresa 
from src.utils.instances import db

class EmpresaService():
    
    def add(self, content):
        try:
            db.session.add(
                Empresa(
                    nit = content.get("nit"), 
                    nombre = content.get("nombre"), 
                    telefono = content.get("telefono"), 
                    correo = content.get("correo"), 
                    direccion = content.get("direccion")
                )
            )
            db.session.commit()

            return (
                {
                    "response": "Empresa creada correctamente"
                },
                201
            )

        except IntegrityError as e:
            db.session.rollback()
            return (
                {
                    "response": "El nit y/o el correo ya se encuentran registrados."
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
