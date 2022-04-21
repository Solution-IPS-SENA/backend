# Controladores y rutas de registro.
from src.controllers.register_paciente import RegisterPacienteController
from src.controllers.register_medico import RegisterMedicoController
from src.controllers.register_empleado import RegisterEmpleadoController

version = "/api/v01"
register_base = f"{version}/register"

register: dict = {
    "paciente":f"{register_base}/paciente", "paciente_controller": RegisterPacienteController.as_view("paciente"),
    "medico":f"{register_base}/medico", "medico_controller": RegisterMedicoController.as_view("medico"),
    "empleado":f"{register_base}/empleado", "empleado_controller": RegisterEmpleadoController.as_view("empleado")
}

# Controladores y rutas de inicio de sesion.
from src.controllers.login_controller import LoginController

auth: dict = {
    "login": f"{version}/login", "login_controller": LoginController.as_view("login"),
}
