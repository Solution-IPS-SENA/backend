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
