import requests
from src.config import URLS

class AnexosService():

    SINO = []
    REFERENCIA = []
    APROBACION = []
    ANTECEDENTES_FAMILIARES = []
    EQUIPOS_UTILIZADOS = []
    REMITIDO = []
    LARSEN = []
    HZ = []
    WEBER = []
    CONDUCTO = []
    MEMBRANA = []
    AGUDEZA_VISUAL = []
    TIEMPO = []
    LENSOMETRIA = []
    PATOLOGICOS = []
    ETS = []
    NRO_VACUNA = []
    ADECUACION = []
    CARGA = []
    MEDIO_AMBIENTE = []
    RIESGOS_LABORALES = []
    FISICO = []
    BIOLOGICO = []
    QUIMICO = []
    SEGURIDAD = []
    BIOMECANICO = []
    PSICOSOCIAL = []
    SERVICIOS = []
    NORMALIDAD = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.SINO = data.get("sino")
        self.REFERENCIA = data.get("referencia")
        self.APROBACION = data.get("aprobacion")
        self.ANTECEDENTES_FAMILIARES = data.get("antecedentesFamiliares")
        self.EQUIPOS_UTILIZADOS = data.get("equiposUtilizados")
        self.REMITIDO = data.get("remitido")
        self.LARSEN = data.get("larsen")
        self.HZ = data.get("hz")
        self.WEBER = data.get("weber")
        self.CONDUCTO = data.get("conducto")
        self.MEMBRANA = data.get("membrana")
        self.AGUDEZA_VISUAL = data.get("agudezaVisual")
        self.TIEMPO = data.get("tiempo")
        self.LENSOMETRIA = data.get("lensometria")
        self.PATOLOGICOS = data.get("patologicos")
        self.ETS = data.get("ets")
        self.NRO_VACUNA = data.get("nroVacuna")
        self.ADECUACION = data.get("adecuacion")
        self.CARGA = data.get("carga")
        self.MEDIO_AMBIENTE = data.get("medioAmbiente")
        self.RIESGOS_LABORALES = data.get("riesgosLaborales")
        self.FISICO = data.get("fisico")
        self.BIOLOGICO = data.get("biologico")
        self.QUIMICO = data.get("quimico")
        self.SEGURIDAD = data.get("seguridad")
        self.BIOMECANICO = data.get("biomecanico")
        self.PSICOSOCIAL = data.get("psicosocial")
        self.SERVICIOS = data.get("servicios")
        self.NORMALIDAD = data.get("normalidad")
        print(self.PAISES)

        self.PAISES = [x.get("iso") for x in data.get("paises")]
        self.INSTITUCION = data.get("institucion")
        self.FACTURA = data.get("factura")
        self.VALOR_FACTURA = data.get("valorFactura")
        self.GENERO = data.get("genero")
        self.LUGAR_DE_NACIMIENTO = data.get("lugarDeNacimiento")
        self.TIPO_DE_DOCUMENTO = data.get("tipoDeDocumento")
        self.EPS = data.get("eps")
        self.ARL = data.get("arl")
        self.AFP = data.get("afp")