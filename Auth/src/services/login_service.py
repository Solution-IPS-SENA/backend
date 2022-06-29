from src.models.paciente_model import Paciente
from src.models.empleado_model import Empleado
from src.models.empresa_model import Empresa
from src.models.medico_model import Medico
from src.utils.functions import time
from src.utils.instances import db
from src.config import KEYS
from bcrypt import checkpw
import jwt

class LoginService():

    def login(self, content):
        tipos_usuario = [
            Medico, 
            Empleado, 
            Paciente,
            Empresa
        ]
        usuario_encontrado = False

        for i in range(len(tipos_usuario)):
            usuario = tipos_usuario[i].query.filter_by(correo=content.get('correo')).first()
            if usuario is not None:
                usuario_encontrado = True
                break;
        
        if not usuario_encontrado:
            return (
                {
                    "response": "El usuario no está registrado."
                },
                409 
            )
            
        db_pass = bytes(usuario.password, 'utf8')
        pass_bytes = bytes(content.get("password"), 'utf8')
        
        if not checkpw(pass_bytes, db_pass):
            return (
                {
                "response": "La contraseña es incorrecta."
                },
                406
            )

        usuario.last_login = time()
        db.session.commit()

        token = jwt.encode(
                {
                    "correo": usuario.correo,
                    "documento": usuario.documento,
                    "rol": usuario.rol
                }, KEYS.JWT, "HS256")

        return (
            {
                "response": "Inicio de sesión satisfactorio",
                "token": f"Bearer {token}"
            },
            200
        )
