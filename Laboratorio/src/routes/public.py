from src.controllers.historia_laboratorio_controller import HistoriaLaboratorioController 

version = "/api/v01"

routes: dict = {
    # Registra o actualiza una historia médica.
    "historia_laboratorio": f"{version}/historia_laboratorio", "historia_laboratorio_controller": HistoriaLaboratorioController.as_view("historia_laboratorio"),
}
