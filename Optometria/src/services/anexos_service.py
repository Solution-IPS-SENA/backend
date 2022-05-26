import requests
from src.config import URLS

class AnexosService():

    SINO = []
    TIEMPO = []
    AGUDEZA_VISUAL = []
    LENSOMETRIA = []
    NORMALIDAD = []
    APROBACION = []
    REMITIDO = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.SINO = data.get("sino")
        self.TIEMPO = data.get("tiempo")
        self.AGUDEZA_VISUAL = data.get("agudezaVisual")
        self.LENSOMETRIA = data.get("lensometria")
        self.NORMALIDAD = data.get("normalidad")
        self.APROBACION = data.get("aprobacion")
        self.REMITIDO = data.get("remitido")