from src.utils.instances import db
from src.models.anexos import anexos
from src.utils.functions import get_datetime

class HistoriaOptometria(db.Model):
    __tablename__ = 'optometria'

    general_id = db.Column(db.Integer, primary_key=True)
    numero_historia = db.Column(db.Integer, default=1)
    documento_paciente = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True) # Estado abierto = True
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=get_datetime())
    fecha_cierre = db.Column(db.DateTime, default=get_datetime())
    ant_def_refra = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_def_cx = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_estra = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_pato = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_tto = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_hiper = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_diab = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_desor = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_acc = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_trau = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_obs = db.Column(db.String(500), nullable=False, default="")
    ant_ocu_exp_vide = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_acc = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_temp = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_mate = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_ra_no_io = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_ra_io = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_exp_quim = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_exp_solv = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_ocu_obs = db.Column(db.Text(500), nullable=False, default="")
    sis_mal_lej = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_mal_cer = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_cel = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_hiper = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_vis_dob = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_vert = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_lagri = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_mare = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_secr = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_rese = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    sis_otro = db.Column(db.String(200), nullable=False, default="")
    agu_cer_sc1 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_cer_sc2 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_cer_sc3 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_cer_cc1 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_cer_cc2 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_cer_cc3 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_sc1 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_sc2 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_sc3 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_cc1 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_cc2 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_lej_cc3 = db.Column(db.String(6), nullable=False, default=anexos.AGUDEZA_VISUAL[0])
    agu_len_pre_od1 = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    agu_len_pre_od2 = db.Column(db.String(5), nullable=False, default=anexos.LENSOMETRIA[0])
    agu_len_pre_oi1 = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    agu_len_pre_oi2 = db.Column(db.String(5), nullable=False, default=anexos.LENSOMETRIA[0])
    agu_len_tiem = db.Column(db.String(15), nullable=False, default=anexos.TIEMPO[0])
    hal_ext_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_mot_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_ofta_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_camp_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_est_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_crom_od = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_ext_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_mot_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_ofta_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_camp_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_est_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_crom_oi = db.Column(db.String(8), nullable=False, default=anexos.NORMALIDAD[0])
    hal_obs = db.Column(db.Text(500), nullable=False, default="")
    motivo = db.Column(db.Text(500), nullable=False, default=anexos.MOTIVO[0])
    cie_concep_reco = db.Column(db.Text(300), nullable=False, default="")
    cie_concep_reco_mot = db.Column(db.String(30), nullable=False, default=anexos.REMITIDO[0])
    cie_obs = db.Column(db.Text(500), nullable=False, default="")
    concepto = db.Column(db.String(12), nullable=False, default=anexos.CONCEPTO[0])
    histo_famili = db.Column(db.Text(500), nullable=False, default="")

    def __init__(
            self, documento_paciente, estado, numero_historia, ant_def_refra, ant_def_cx,
            ant_estra, ant_pato, ant_tto, ant_hiper, ant_diab, ant_desor, 
            ant_acc, ant_trau, ant_obs, ant_ocu_exp_vide, ant_ocu_acc,
            ant_ocu_temp, ant_ocu_mate, ant_ocu_ra_no_io, ant_ocu_ra_io,
            ant_ocu_exp_quim, ant_ocu_exp_solv, ant_ocu_obs, sis_mal_lej, 
            sis_mal_cer, sis_cel, sis_hiper, sis_vis_dob, sis_vert, sis_lagri,
            sis_mare, sis_secr, sis_rese, sis_otro, agu_cer_sc1, agu_cer_sc2,
            agu_cer_sc3, agu_cer_cc1, agu_cer_cc2, agu_cer_cc3, agu_lej_sc1,
            agu_lej_sc2 ,agu_lej_sc3 ,agu_lej_cc1 ,agu_lej_cc2 ,agu_lej_cc3,
            agu_len_pre_od1, agu_len_pre_od2, agu_len_pre_oi1, agu_len_pre_oi2,
            agu_len_tiem, hal_ext_od, hal_mot_od, hal_ofta_od, hal_camp_od,
            hal_est_od, hal_crom_od, hal_ext_oi, hal_mot_oi, hal_ofta_oi, 
            hal_camp_oi, hal_est_oi, hal_crom_oi, hal_obs, motivo,
            cie_concep_reco, cie_concep_reco_mot, cie_obs,
            concepto
        ):
        self.estado = estado
        self.numero_historia = numero_historia
        self.documento_paciente = documento_paciente
        self.ant_def_refra = ant_def_refra
        self.ant_def_cx = ant_def_cx
        self.ant_estra = ant_estra
        self.ant_pato = ant_pato
        self.ant_tto = ant_tto
        self.ant_hiper = ant_hiper
        self.ant_diab = ant_diab
        self.ant_desor = ant_desor
        self.ant_acc = ant_acc
        self.ant_trau = ant_trau
        self.ant_obs = ant_obs
        self.ant_ocu_exp_vide = ant_ocu_exp_vide
        self.ant_ocu_acc = ant_ocu_acc
        self.ant_ocu_temp = ant_ocu_temp
        self.ant_ocu_mate = ant_ocu_mate
        self.ant_ocu_ra_no_io = ant_ocu_ra_no_io
        self.ant_ocu_ra_io = ant_ocu_ra_io
        self.ant_ocu_exp_quim = ant_ocu_exp_quim
        self.ant_ocu_exp_solv = ant_ocu_exp_solv
        self.ant_ocu_obs = ant_ocu_obs
        self.sis_mal_lej = sis_mal_lej
        self.sis_mal_cer = sis_mal_cer
        self.sis_cel = sis_cel
        self.sis_hiper = sis_hiper
        self.sis_vis_dob = sis_vis_dob
        self.sis_vert = sis_vert
        self.sis_lagri = sis_lagri
        self.sis_mare = sis_mare
        self.sis_secr = sis_secr
        self.sis_rese = sis_rese
        self.sis_otro = sis_otro
        self.agu_cer_sc1 = agu_cer_sc1
        self.agu_cer_sc2 = agu_cer_sc2
        self.agu_cer_sc3 = agu_cer_sc3
        self.agu_cer_cc1 = agu_cer_cc1
        self.agu_cer_cc2 = agu_cer_cc2
        self.agu_cer_cc3 = agu_cer_cc3
        self.agu_lej_sc1 = agu_lej_sc1
        self.agu_lej_sc2 = agu_lej_sc2
        self.agu_lej_sc3 = agu_lej_sc3
        self.agu_lej_cc1 = agu_lej_cc1
        self.agu_lej_cc2 = agu_lej_cc2
        self.agu_lej_cc3 = agu_lej_cc3
        self.agu_len_pre_od1 = agu_len_pre_od1
        self.agu_len_pre_od2 = agu_len_pre_od2
        self.agu_len_pre_oi1 = agu_len_pre_oi1
        self.agu_len_pre_oi2 = agu_len_pre_oi2
        self.agu_len_tiem = agu_len_tiem
        self.hal_ext_od = hal_ext_od
        self.hal_mot_od = hal_mot_od
        self.hal_ofta_od = hal_ofta_od
        self.hal_camp_od = hal_camp_od
        self.hal_est_od = hal_est_od
        self.hal_crom_od = hal_crom_od
        self.hal_ext_oi = hal_ext_oi
        self.hal_mot_oi = hal_mot_oi
        self.hal_ofta_oi = hal_ofta_oi
        self.hal_camp_oi = hal_camp_oi
        self.hal_est_oi = hal_est_oi
        self.hal_crom_oi = hal_crom_oi
        self.hal_obs = hal_obs
        self.motivo = motivo
        self.cie_concep_reco = cie_concep_reco
        self.cie_concep_reco_mot = cie_concep_reco_mot
        self.cie_obs = cie_obs
        self.concepto = concepto

    def to_dict(self):
        return dict(
            numero_historia=self.numero_historia,
            documento_paciente=self.documento_paciente,
            estado=self.estado,
            fecha_creacion=str(self.fecha_creacion),
            fecha_cierre=str(self.fecha_cierre),
            ant_def_refra=self.ant_def_refra,
            ant_def_cx=self.ant_def_cx,
            ant_estra=self.ant_estra,
            ant_pato=self.ant_pato,
            ant_tto=self.ant_tto,
            ant_hiper=self.ant_hiper,
            ant_diab=self.ant_diab,
            ant_desor=self.ant_desor,
            ant_acc=self.ant_acc,
            ant_trau=self.ant_trau,
            ant_obs=self.ant_obs,
            ant_ocu_exp_vide=self.ant_ocu_exp_vide,
            ant_ocu_acc=self.ant_ocu_acc,
            ant_ocu_temp=self.ant_ocu_temp,
            ant_ocu_mate=self.ant_ocu_mate,
            ant_ocu_ra_no_io=self.ant_ocu_ra_no_io,
            ant_ocu_ra_io=self.ant_ocu_ra_io,
            ant_ocu_exp_quim=self.ant_ocu_exp_quim,
            ant_ocu_exp_solv=self.ant_ocu_exp_solv,
            ant_ocu_obs=self.ant_ocu_obs,
            sis_mal_lej=self.sis_mal_lej,
            sis_mal_cer=self.sis_mal_cer,
            sis_cel=self.sis_cel,
            sis_hiper=self.sis_hiper,
            sis_vis_dob=self.sis_vis_dob,
            sis_vert=self.sis_vert,
            sis_lagri=self.sis_lagri,
            sis_mare=self.sis_mare,
            sis_secr=self.sis_secr,
            sis_rese=self.sis_rese,
            sis_otro=self.sis_otro,
            agu_cer_sc1=self.agu_cer_sc1,
            agu_cer_sc2=self.agu_cer_sc2,
            agu_cer_sc3=self.agu_cer_sc3,
            agu_cer_cc1=self.agu_cer_cc1,
            agu_cer_cc2=self.agu_cer_cc2,
            agu_cer_cc3=self.agu_cer_cc3,
            agu_lej_sc1=self.agu_lej_sc1,
            agu_lej_sc2=self.agu_lej_sc2,
            agu_lej_sc3=self.agu_lej_sc3,
            agu_lej_cc1=self.agu_lej_cc1,
            agu_lej_cc2=self.agu_lej_cc2,
            agu_lej_cc3=self.agu_lej_cc3,
            agu_len_pre_od1=self.agu_len_pre_od1,
            agu_len_pre_od2=self.agu_len_pre_od2,
            agu_len_pre_oi1=self.agu_len_pre_oi1,
            agu_len_pre_oi2=self.agu_len_pre_oi2,
            agu_len_tiem=self.agu_len_tiem,
            hal_ext_od=self.hal_ext_od,
            hal_mot_od=self.hal_mot_od,
            hal_ofta_od=self.hal_ofta_od,
            hal_camp_od=self.hal_camp_od,
            hal_est_od=self.hal_est_od,
            hal_crom_od=self.hal_crom_od,
            hal_ext_oi=self.hal_ext_oi,
            hal_mot_oi=self.hal_mot_oi,
            hal_ofta_oi=self.hal_ofta_oi,
            hal_camp_oi=self.hal_camp_oi,
            hal_est_oi=self.hal_est_oi,
            hal_crom_oi=self.hal_crom_oi,
            hal_obs=self.hal_obs,
            motivo=self.motivo,
            cie_concep_reco=self.cie_concep_reco,
            cie_concep_reco_mot=self.cie_concep_reco_mot,
            cie_obs=self.cie_obs,
            concepto=self.concepto
        )