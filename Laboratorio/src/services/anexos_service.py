import requests
from src.config import URLS

class AnexosService():

    NORMALIDAD = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.NORMALIDAD = data.get("normalidad")