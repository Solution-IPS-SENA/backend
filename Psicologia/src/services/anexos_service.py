import requests
from src.config import URLS

class AnexosService():

    SINO = []
    ADECUACION = []
    REMITIDO = []
    APROBACION = []
    CONCEPTO = []
    MOTIVO = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.SINO = data.get("sino")
        self.ADECUACION = data.get("adecuacion")
        self.REMITIDO = data.get("remitido")
        self.APROBACION = data.get("aprobacion")
        self.CONCEPTO = data.get("concepto")
        self.MOTIVO = data.get("motivo")