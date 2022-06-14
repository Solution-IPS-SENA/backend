from src.utils.instances import db
from src.models.anexos import anexos
from src.utils.functions import get_datetime

class HistoriaLaboratorio(db.Model):
    __tablename__ = 'laboratorio'

    general_id = db.Column(db.Integer, primary_key=True)
    numero_historia = db.Column(db.Integer, default=1)
    documento_paciente = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True) # Estado abierto = True
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=get_datetime())
    fecha_cierre = db.Column(db.DateTime, default=get_datetime())
    hema = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    glice = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    colestot = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    coleshdl = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    colesldl = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    trigli = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    parcori = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    culori = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    copro = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    frotsisfar = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    cultifar = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    koh = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    tsh = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    creat = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    funchep = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    protinc = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    pt = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    ptt = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    aciuri = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    antigpros = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    gasarte = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    vdrl = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    gravi = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    otro = db.Column(db.String(10), nullable=False, default=anexos.NORMALIDAD[0])
    obser1_lab = db.Column(db.String(500), nullable=False, default="")
    obser2_lab = db.Column(db.String(500), nullable=False, default="")


    def __init__(
            self, documento_paciente, numero_historia, estado, hema,
            glice, colestot,coleshdl, colesldl, trigli, parcori, culori,
            copro, frotsisfar, cultifar, koh, tsh, creat, funchep, protinc,
            pt, ptt, aciuri, antigpros, gasarte, vdrl, gravi, otro,
            obser1_lab, obser2_lab
        ):
        self.estado = estado
        self.numero_historia = numero_historia
        self.documento_paciente = documento_paciente
        self.hema = hema
        self.glice = glice
        self.colestot = colestot
        self.coleshdl = coleshdl
        self.colesldl = colesldl
        self.trigli = trigli
        self.parcori = parcori
        self.culori = culori
        self.copro = copro
        self.frotsisfar = frotsisfar
        self.cultifar = cultifar
        self.koh = koh
        self.tsh = tsh
        self.creat = creat
        self.funchep = funchep
        self.protinc = protinc
        self.pt = pt
        self.ptt = ptt
        self.aciuri = aciuri
        self.antigpros = antigpros
        self.gasarte = gasarte
        self.vdrl = vdrl
        self.gravi = gravi
        self.otro = otro
        self.obser1_lab = obser1_lab
        self.obser2_lab = obser2_lab


    def to_dict(self):
        return dict(
            numero_historia=self.numero_historia,
            documento_paciente=self.documento_paciente,
            estado=self.estado,
            fecha_creacion=str(self.fecha_creacion),
            fecha_cierre=str(self.fecha_cierre),
            hema=self.hema,
            glice=self.glice,
            colestot=self.colestot,
            coleshdl=self.coleshdl,
            colesldl=self.colesldl,
            trigli=self.trigli,
            parcori=self.parcori,
            culori=self.culori,
            copro=self.copro,
            frotsisfar=self.frotsisfar,
            cultifar=self.cultifar,
            koh=self.koh,
            tsh=self.tsh,
            creat=self.creat,
            funchep=self.funchep,
            protinc=self.protinc,
            pt=self.pt,
            ptt=self.ptt,
            aciuri=self.aciuri,
            antigpros=self.antigpros,
            gasarte=self.gasarte,
            vdrl=self.vdrl,
            gravi=self.gravi,
            otro=self.otro,
            obser1_lab=self.obser1_lab,
            obser2_lab=self.obser2_lab
        )