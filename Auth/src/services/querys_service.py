from src.models.paciente_model import Paciente

class QuerysService:
    def obtenerPaciente(self, tipoDoc, doc):
        paciente = Paciente.query.filter_by(tipo_documento=tipoDoc, documento=doc).first()
        if not paciente:
            return ({
                "response": "El paciente no existe."
            },  200)
        return ({
            "response": paciente.to_dict()
        }, 200)