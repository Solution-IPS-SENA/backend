import requests
import src.models.anexos as a
from src.config import URLS

class AnexosService():

    NORMALIDAD = []
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
    FACTURA = []
    VALOR_FACTURA = []
    PATOLOGICOS = []
    ETS = []
    NRO_VACUNA = []
    ADECUACION = []
    CARGA = []
    MEDIO_AMBIENTE = []
    INSTITUCION = []
    RIESGOS_LABORALES = []
    FISICO = []
    BIOLOGICO = []
    QUIMICO = []
    SEGURIDAD = []
    BIOMECANICO = []
    PSICOSOCIAL = []

    def __init__(self):
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        self.NORMALIDAD = data.get("normalidad")
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
        self.FACTURA = data.get("factura")
        self.VALOR_FACTURA = data.get("valorFactura")
        self.PATOLOGICOS = data.get("patologicos")
        self.ETS = data.get("ets")
        self.NRO_VACUNA = data.get("nroVacuna")
        self.ADECUACION = data.get("adecuacion")
        self.CARGA = data.get("carga")
        self.MEDIO_AMBIENTE = data.get("medioAmbiente")
        self.INSTITUCION = data.get("institucion")
        self.RIESGOS_LABORALES = data.get("riesgosLaborales")
        self.FISICO = data.get("fisico")
        self.BIOLOGICO = data.get("biologico")
        self.QUIMICO = data.get("quimico")
        self.SEGURIDAD = data.get("seguridad")
        self.BIOMECANICO = data.get("biomecanico")
        self.PSICOSOCIAL = data.get("psicosocial")
