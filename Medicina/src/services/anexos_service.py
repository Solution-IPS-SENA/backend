import requests
import src.models.anexos as a
from src.config import URLS

class AnexosService():
    
    def get():
        req = requests.get(URLS.ANEXOS)
        data = req.json()
        return data

    def rellenarAnexos():
        data = AnexosService.get()
        a.NORMALDAD = data.get("normalidad")
        a.SINO = data.get("sino")
        a.REFERENCIA = data.get("referencia")
        a.APROBACION = data.get("aprobacion")
        a.ANTECEDENTES_FAMILIARES = data.get("antecedentesFamiliares")
        a.EQUIPOS_UTILIZADOS = data.get("equiposUtilizados")
        a.REMITIDO = data.get("remitido")
        a.LARSEN = data.get("larsen")
        a.HZ = data.get("hz")
        a.WEBER = data.get("weber")
        a.CONDUCTO = data.get("conducto")
        a.MEMBRANA = data.get("membrana")
        a.AGUDEZA_VISUAL = data.get("agudezaVisual")
        a.TIEMPO = data.get("tiempo")
        a.LENSOMETRIA = data.get("lensometria")
        a.FACTURA = data.get("factura")
        a.VALOR_FACTURA = data.get("valorFactura")
        a.PATOLOGICOS = data.get("patologicos")
        a.ETS = data.get("ets")
        a.NRO_VACUNA = data.get("nroVacuna")
        
        print(
            a.NORMALDAD,
            a.SINO,
            a.REFERENCIA,
            a.APROBACION,
            a.ANTECEDENTES_FAMILIARES,
            a.EQUIPOS_UTILIZADOS,
            a.REMITIDO,
            a.LARSEN,
            a.HZ,
            a.WEBER,
            a.CONDUCTO,
            a.MEMBRANA,
            a.AGUDEZA_VISUAL,
            a.TIEMPO,
            a.LENSOMETRIA,
            a.FACTURA,
            a.VALOR_FACTURA,
            a.PATOLOGICOS,
            a.ETS,
            a.NRO_VACUNA,
        )
