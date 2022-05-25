from src.utils.instances import db
from src.models.anexos import anexos
from src.utils.functions import get_datetime

class HistoriaFonoaudiologia(db.Model):
    __tablename__ = 'fonoaudiologia'

    ant_ext_mano = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_ambi = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_poli = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_mili = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_mext = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_per = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_otal = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_acuf = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_oto = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_cir = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_equi = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_comu = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_fami = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_cong = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_ext_otot = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_EPA1 = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_EPA2 = db.Column(db.String(2), nullable=False, default=anexos.SINO)
    ant_EPA3 = db.Column(db.String(2), nullable=False, default=anexos.SINO)



    def __init__(self):
        pass

    def to_dict(self):
        return dict(
            
        )