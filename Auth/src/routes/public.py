from src.controllers.register_controller import RegisterPacienteController,\
                                                RegisterMedicoController,\
                                                RegisterEmpleadoController,\
                                                RegisterEmpresaController
from src.controllers.login_controller import LoginController
from src.controllers.querys_controller import PacienteController

version = "/api/v01"
register_base = f"{version}/register"

register: dict = {
    "paciente": f"{register_base}/paciente", "paciente_controller": RegisterPacienteController.as_view("paciente"),
    "medico": f"{register_base}/medico", "medico_controller": RegisterMedicoController.as_view("medico"),
    "empleado": f"{register_base}/empleado", "empleado_controller": RegisterEmpleadoController.as_view("empleado"),
    "empresa": f"{register_base}/empresa", "empresa_controller": RegisterEmpresaController.as_view("empresa")
}

# Controladores y rutas de inicio de sesion.
auth: dict = {
    "login": f"{version}/login", "login_controller": LoginController.as_view("login"),
}

querys = {
    "query_paciente": "/paciente", "query_paciente_controller": PacienteController.as_view("query_paciente")
}
