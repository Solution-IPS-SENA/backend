import requests
from src.config import URLS

class AnexosService():

    SINO = []
    HZ = []
    WEBER = []
    CONDUCTO = []
    MEMBRANA = []
    REMITIDO = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.SINO = data.get("sino")
        self.HZ = data.get("hz")
        self.WEBER = data.get("weber")
        self.CONDUCTO = data.get("conducto")
        self.MEMBRANA = data.get("membrana")
        self.REMITIDO = data.get("remitido")