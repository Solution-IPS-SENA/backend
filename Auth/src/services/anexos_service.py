import requests
from src.config import URLS

class AnexosService():

    PAISES = []
    GENERO = []
    LUGAR_DE_NACIMIENTO = []
    TIPO_DOCUMENTO = []
    EPS = []
    ARL = []
    AFP = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.PAISES = [x.get("iso") for x in data.get("paises")]
        self.GENERO = data.get("genero")
        self.LUGAR_DE_NACIMIENTO = data.get("lugarDeNacimiento")
        self.TIPO_DOCUMENTO = [x.get("abreviacion") for x in data.get("tipoDocumento")]
        self.EPS = data.get("eps")
        self.ARL = data.get("arl")
        self.AFP = data.get("afp")