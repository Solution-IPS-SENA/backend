from src.controllers.historia_optometria_controller import HistoriaOptometriaController

version = "/api/v01"

routes: dict = {
    # Registra o actualiza una historia médica.
    "historia_optometria": f"{version}/historia_optometria", "historia_optometria_controller": HistoriaOptometriaController.as_view("historia_optometria"),
}
