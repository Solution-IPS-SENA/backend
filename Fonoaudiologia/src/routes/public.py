from src.controllers.historia_fonoaudiologia_controller import HistoriaFonoaudiologiaController

version = "/api/v01"

routes: dict = {
    # Registra o actualiza una historia médica.
    "historia_fonoaudiologia": f"{version}/historia_fonoaudiologia", "historia_fonoaudiologia_controller": HistoriaFonoaudiologiaController.as_view("historia_medica"),
}
