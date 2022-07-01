from marshmallow import Schema, fields
from marshmallow import validate
from src.models.anexos import anexos as a

def validar_fecha(fecha):
    fecha = fecha.split("-")
    try:
        anio = True if len(fecha[0]) == 4 and int(fecha[0]) > 1800 and int(fecha[0]) < 2023 else False
        mes = True if len(fecha[1]) == 2 and int(fecha[1]) > 0 and int(fecha[1]) < 13 else False
        dia = True if len(fecha[2]) == 2 and int(fecha[2]) > 0 and int(fecha[2]) < 32 else False
        return True if anio and mes and dia else False

    except:
        return False

class HistoriaLaboratorioSchema(Schema):
    documento_paciente = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    hema = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    glice = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    colestot = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    coleshdl = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    colesldl = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    trigli = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    parcori = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    culori = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    copro = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    frotsisfar = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    cultifar = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    koh = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    tsh = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    creat = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    funchep = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    protinc = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    pt = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    ptt = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    aciuri = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    antigpros = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    gasarte = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    vdrl = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    gravi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    otro = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    obser1_lab = fields.Str(required=True, validate=validate.Length(max=500))
    obser2_lab = fields.Str(required=True, validate=validate.Length(max=500))
