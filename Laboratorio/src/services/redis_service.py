from src.models.historia_laboratorio_model import HistoriaMedica 
from src.utils.instances import rd

class RedisService:

    @classmethod
    def backup_from_db(cls):
        historias_medicas = HistoriaMedica.query.all()
        for historia in historias_medicas:
            doc = historia.documento_paciente
            if rd.exists(f"documento_paciente:{doc}") == 0:
                rd.hmset(f"documento_paciente:{doc}", historia.to_dict())
