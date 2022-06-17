import requests
from src.config import URLS

class AnexosService():

    NORMALIDAD = []
    CONCEPTO = []
    MOTIVO = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.NORMALIDAD = data.get("normalidad")
        self.CONCEPTO = data.get("concepto")
        self.MOTIVO = data.get("motivo")