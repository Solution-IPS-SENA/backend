from src.controllers.historia_psicologia_controller import HistoriaPsicologiaController

version = "/api/v01"

routes: dict = {
    # Registra o actualiza una historia médica.
    "historia_psicologia": f"{version}/historia_psicologia", "historia_psicologia_controller": HistoriaPsicologiaController.as_view("historia_psicologia"),
}
