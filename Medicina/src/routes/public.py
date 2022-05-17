from src.controllers.historia_medica_controller import HistoriaMedicaController

version = "/api/v01"

routes: dict = {
    # Registra o actualiza una historia médica.
    "historia_medica": f"{version}/historia_medica", "historia_medica_controller": HistoriaMedicaController.as_view("historia_medica"),
}
