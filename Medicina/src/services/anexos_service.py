import requests
from src.config import URLS

class AnexosService():

    SINO = []
    REFERENCIA = []
    APROBACION = []
    ANTECEDENTES_FAMILIARES = []
    EQUIPOS_UTILIZADOS = []
    PATOLOGICOS = []
    ETS = []
    NRO_VACUNA = []
    FISICO = []
    BIOLOGICO = []
    QUIMICO = []
    SEGURIDAD = []
    BIOMECANICO = []
    PSICOSOCIAL = []
    NORMALIDAD = []
    CONCEPTO = []
    MOTIVO = []
    REMITIDO = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.SINO = data.get("sino")
        self.REFERENCIA = data.get("referencia")
        self.APROBACION = data.get("aprobacion")
        self.ANTECEDENTES_FAMILIARES = data.get("antecedentesFamiliares")
        self.EQUIPOS_UTILIZADOS = data.get("equiposUtilizados")
        self.PATOLOGICOS = data.get("patologicos")
        self.ETS = data.get("ets")
        self.NRO_VACUNA = data.get("nroVacuna")
        self.FISICO = data.get("fisico")
        self.BIOLOGICO = data.get("biologico")
        self.QUIMICO = data.get("quimico")
        self.SEGURIDAD = data.get("seguridad")
        self.BIOMECANICO = data.get("biomecanico")
        self.PSICOSOCIAL = data.get("psicosocial")
        self.NORMALIDAD = data.get("normalidad")
        self.CONCEPTO = data.get("concepto")
        self.MOTIVO = data.get("motivo")
        self.REMITIDO = data.get("remitido")