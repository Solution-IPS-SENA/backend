from src.utils.instances import db
from src.models.anexos import anexos
from src.utils.functions import get_datetime

class HistoriaMedica(db.Model):
    __tablename__ = 'historia_medica'

    general_id = db.Column(db.Integer, primary_key=True)
    numero_historia = db.Column(db.Integer, default=1)
    documento_paciente = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True) # Estado abierto = True
    ant_padre_card = db.Column(db.String(50), nullable=False, default=anexos.ANTECEDENTES_FAMILIARES[0])
    ant_madre_card = db.Column(db.String(50), nullable=False, default=anexos.ANTECEDENTES_FAMILIARES[0])
    ant_padre_cong = db.Column(db.String(50), nullable=False, default=anexos.ANTECEDENTES_FAMILIARES[0])
    ant_madre_cong = db.Column(db.String(50), nullable=False, default=anexos.ANTECEDENTES_FAMILIARES[0])
    ant_per_pato = db.Column(db.String(10), nullable=False, default=anexos.PATOLOGICOS[0])
    ant_per_qui = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    ant_per_trau = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    ant_per_toxi = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    ant_per_alergi = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    ant_per_ets = db.Column(db.String(100), nullable=False, default=anexos.ETS[0])
    ant_per_obs1 = db.Column(db.String(500), nullable=False, default="")
    ant_per_gin_fup = db.Column(db.String(10), nullable=False, default="0000-00-00")
    ant_per_gin_fum = db.Column(db.String(10), nullable=False, default="0000-00-00")
    ant_per_gin_plan = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_per_gin_dism = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_per_gin_disp = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_per_gin_mam = db.Column(db.String(10), nullable=False, default="0000-00-00")
    ant_per_gin_mens = db.Column(db.String(7), nullable=False, default=anexos.NORMALIDAD[0])
    ant_per_obs2 = db.Column(db.String(500), nullable=False, default="")
    inm_hep_a = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_hep_b = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_trip = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_teta = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_mala = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_amar = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_tifo = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    inm_cov = db.Column(db.String(8), nullable=False, default=anexos.NRO_VACUNA[0])
    mani_ali = db.Column(db.String(10), nullable=False, default="0000-00-00")
    inm_obs = db.Column(db.String(500), nullable=False, default="")
    hab_ciga = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    hab_alco = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    hab_drog = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    hab_dep = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    hab_les = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])    
    hab_obs = db.Column(db.String(500), nullable=False, default="")
    sis_derma = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_ost_musc = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_ost_arti = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_geni = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_meta = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_neur = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_carf = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_endo = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_uro = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_gatro = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    sis_orl = db.Column(db.String(10), nullable=False, default=anexos.REFERENCIA[0])
    rie_exp_fis_1 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_exp_fis_2 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_exp_fis_3 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_exp_fis_4 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_exp_bio_1 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_exp_bio_2 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_exp_bio_3 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_exp_bio_4 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_exp_quim_1 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_exp_quim_2 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_exp_quim_3 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_exp_quim_4 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_exp_seg_1 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_exp_seg_2 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_exp_seg_3 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_exp_seg_4 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_exp_biom_1 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_exp_biom_2 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_exp_biom_3 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_exp_biom_4 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_exp_psico_1 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_exp_psico_2 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_exp_psico_3 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_exp_psico_4 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_exp_obs = db.Column(db.String(500), nullable=False, default="")
    rie_ant_fis_1 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_ant_fis_2 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_ant_fis_3 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_ant_fis_4 = db.Column(db.String(10), nullable=False, default=anexos.FISICO[0])
    rie_ant_bio_1 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_ant_bio_2 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_ant_bio_3 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_ant_bio_4 = db.Column(db.String(10), nullable=False, default=anexos.BIOLOGICO[0])
    rie_ant_quim_1 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_ant_quim_2 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_ant_quim_3 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_ant_quim_4 = db.Column(db.String(10), nullable=False, default=anexos.QUIMICO[0])
    rie_ant_seg_1 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_ant_seg_2 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_ant_seg_3 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_ant_seg_4 = db.Column(db.String(10), nullable=False, default=anexos.SEGURIDAD[0])
    rie_ant_biom_1 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_ant_biom_2 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_ant_biom_3 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_ant_biom_4 = db.Column(db.String(10), nullable=False, default=anexos.BIOMECANICO[0])
    rie_ant_psico_1 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_ant_psico_2 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_ant_psico_3 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_ant_psico_4 = db.Column(db.String(10), nullable=False, default=anexos.PSICOSOCIAL[0])
    rie_ant_obs = db.Column(db.String(500), nullable=False, default="")
    ocu_equi = db.Column(db.String(22), nullable=False, default=anexos.EQUIPOS_UTILIZADOS[0])
    ocu_acti = db.Column(db.String(100), nullable=False, default="")
    ocu_acc_emp1 = db.Column(db.String(100), nullable=False, default="")
    ocu_acc_diag1 = db.Column(db.String(500), nullable=False, default="")
    ocu_acc_emp2 = db.Column(db.String(100), nullable=False, default="")
    ocu_acc_diag2 = db.Column(db.String(500), nullable=False, default="")
    ocu_obs = db.Column(db.String(500), nullable=False, default="")
    cie_concep_desc = db.Column(db.String(500), nullable=False, default="")
    cie_concep_reco = db.Column(db.String(300), nullable=False, default="")
    cie_concep_aplaz = db.Column(db.String(300), nullable=False, default="")
    cie_concep_reco_mot = db.Column(db.String(20), nullable=False, default="")
    cie_obs = db.Column(db.String(500), nullable=False, default="")
    cie_concep_fin = db.Column(db.String(12), nullable=False, default=anexos.APROBACION[0])
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=get_datetime())
    fecha_cierre = db.Column(db.DateTime, default=get_datetime())

    def __init__(
            self, documento_paciente, ant_padre_card, ant_madre_card,
            ant_padre_cong, ant_madre_cong, ant_per_pato,
            ant_per_qui, ant_per_trau, ant_per_toxi, ant_per_alergi,
            ant_per_ets, ant_per_obs1, ant_per_gin_fup, ant_per_gin_fum,
            ant_per_gin_plan, ant_per_gin_dism, ant_per_gin_disp,
            ant_per_gin_mam, ant_per_gin_mens, ant_per_obs2, inm_hep_a, 
            inm_hep_b, inm_trip, inm_teta, inm_mala, inm_amar,
            inm_tifo, inm_cov, mani_ali, inm_obs, hab_ciga, hab_alco,
            hab_drog, hab_dep, hab_les, hab_obs, sis_derma, sis_ost_musc,
            sis_ost_arti, sis_geni, sis_meta, sis_neur, sis_carf, sis_endo,
            sis_uro, sis_gatro, sis_orl, rie_exp_fis_1, rie_exp_fis_2,
            rie_exp_fis_3, rie_exp_fis_4, rie_exp_bio_1, rie_exp_bio_2,
            rie_exp_bio_3, rie_exp_bio_4, rie_exp_quim_1, rie_exp_quim_2,
            rie_exp_quim_3, rie_exp_quim_4, rie_exp_seg_1, rie_exp_seg_2,
            rie_exp_seg_3, rie_exp_seg_4, rie_exp_biom_1, rie_exp_biom_2,
            rie_exp_biom_3, rie_exp_biom_4, rie_exp_psico_1, rie_exp_psico_2,
            rie_exp_psico_3, rie_exp_psico_4, rie_exp_obs, rie_ant_fis_1,
            rie_ant_fis_2, rie_ant_fis_3, rie_ant_fis_4, rie_ant_bio_1,
            rie_ant_bio_2, rie_ant_bio_3, rie_ant_bio_4, rie_ant_quim_1,
            rie_ant_quim_2, rie_ant_quim_3, rie_ant_quim_4, rie_ant_seg_1,
            rie_ant_seg_2, rie_ant_seg_3, rie_ant_seg_4, rie_ant_biom_1,
            rie_ant_biom_2, rie_ant_biom_3, rie_ant_biom_4, rie_ant_psico_1,
            rie_ant_psico_2, rie_ant_psico_3, rie_ant_psico_4, rie_ant_obs,
            ocu_equi, ocu_acti, ocu_acc_emp1, ocu_acc_diag1, ocu_acc_emp2,
            ocu_acc_diag2, ocu_obs, cie_concep_desc, cie_concep_reco,
            cie_concep_aplaz, cie_concep_aplaza, cie_concep_reco_mot,
            cie_obs, cie_concep_fin, numero_historia=False
        ):
        if numero_historia:
            self.numero_historia = numero_historia
        self.documento_paciente = documento_paciente
        self.ant_padre_card = ant_padre_card
        self.ant_madre_card = ant_madre_card
        self.ant_padre_cong = ant_padre_cong
        self.ant_madre_cong = ant_madre_cong
        self.ant_per_pato = ant_per_pato
        self.ant_per_qui = ant_per_qui
        self.ant_per_trau = ant_per_trau
        self.ant_per_toxi = ant_per_toxi
        self.ant_per_alergi = ant_per_alergi
        self.ant_per_ets = ant_per_ets
        self.ant_per_obs1 = ant_per_obs1
        self.ant_per_gin_fup = ant_per_gin_fup
        self.ant_per_gin_fum = ant_per_gin_fum
        self.ant_per_gin_plan = ant_per_gin_plan
        self.ant_per_gin_dism = ant_per_gin_dism
        self.ant_per_gin_disp = ant_per_gin_disp
        self.ant_per_gin_mam = ant_per_gin_mam
        self.ant_per_gin_mens = ant_per_gin_mens
        self.ant_per_obs2 = ant_per_obs2
        self.inm_hep_a = inm_hep_a
        self.inm_hep_b = inm_hep_b
        self.inm_trip = inm_trip
        self.inm_teta = inm_teta
        self.inm_mala = inm_mala
        self.inm_amar = inm_amar
        self.inm_tifo = inm_tifo
        self.inm_cov = inm_cov
        self.mani_ali = mani_ali
        self.inm_obs = inm_obs
        self.hab_ciga = hab_ciga
        self.hab_alco = hab_alco
        self.hab_drog = hab_drog
        self.hab_dep = hab_dep
        self.hab_les = hab_les
        self.hab_obs = hab_obs
        self.sis_derma = sis_derma
        self.sis_ost_musc = sis_ost_musc
        self.sis_ost_arti = sis_ost_arti
        self.sis_geni = sis_geni
        self.sis_meta = sis_meta
        self.sis_neur = sis_neur
        self.sis_carf = sis_carf
        self.sis_endo = sis_endo
        self.sis_uro = sis_uro
        self.sis_gatro = sis_gatro
        self.sis_orl = sis_orl
        self.rie_exp_fis_1 = rie_exp_fis_1
        self.rie_exp_fis_2 = rie_exp_fis_2
        self.rie_exp_fis_3 = rie_exp_fis_3
        self.rie_exp_fis_4 = rie_exp_fis_4
        self.rie_exp_bio_1 = rie_exp_bio_1
        self.rie_exp_bio_2 = rie_exp_bio_2
        self.rie_exp_bio_3 = rie_exp_bio_3
        self.rie_exp_bio_4 = rie_exp_bio_4
        self.rie_exp_quim_1 = rie_exp_quim_1
        self.rie_exp_quim_2 = rie_exp_quim_2
        self.rie_exp_quim_3 = rie_exp_quim_3
        self.rie_exp_quim_4 = rie_exp_quim_4
        self.rie_exp_seg_1 = rie_exp_seg_1
        self.rie_exp_seg_2 = rie_exp_seg_2
        self.rie_exp_seg_3 = rie_exp_seg_3
        self.rie_exp_seg_4 = rie_exp_seg_4
        self.rie_exp_biom_1 = rie_exp_biom_1
        self.rie_exp_biom_2 = rie_exp_biom_2
        self.rie_exp_biom_3 = rie_exp_biom_3
        self.rie_exp_biom_4 = rie_exp_biom_4
        self.rie_exp_psico_1 = rie_exp_psico_1
        self.rie_exp_psico_2 = rie_exp_psico_2
        self.rie_exp_psico_3 = rie_exp_psico_3
        self.rie_exp_psico_4 = rie_exp_psico_4
        self.rie_exp_obs = rie_exp_obs
        self.rie_ant_fis_1 = rie_ant_fis_1
        self.rie_ant_fis_2 = rie_ant_fis_2
        self.rie_ant_fis_3 = rie_ant_fis_3
        self.rie_ant_fis_4 = rie_ant_fis_4
        self.rie_ant_bio_1 = rie_ant_bio_1
        self.rie_ant_bio_2 = rie_ant_bio_2
        self.rie_ant_bio_3 = rie_ant_bio_3
        self.rie_ant_bio_4 = rie_ant_bio_4
        self.rie_ant_quim_1 = rie_ant_quim_1
        self.rie_ant_quim_2 = rie_ant_quim_2
        self.rie_ant_quim_3 = rie_ant_quim_3
        self.rie_ant_quim_4 = rie_ant_quim_4
        self.rie_ant_seg_1 = rie_ant_seg_1
        self.rie_ant_seg_2 = rie_ant_seg_2
        self.rie_ant_seg_3 = rie_ant_seg_3
        self.rie_ant_seg_4 = rie_ant_seg_4
        self.rie_ant_biom_1 = rie_ant_biom_1
        self.rie_ant_biom_2 = rie_ant_biom_2
        self.rie_ant_biom_3 = rie_ant_biom_3
        self.rie_ant_biom_4 = rie_ant_biom_4
        self.rie_ant_psico_1 = rie_ant_psico_1
        self.rie_ant_psico_2 = rie_ant_psico_2
        self.rie_ant_psico_3 = rie_ant_psico_3
        self.rie_ant_psico_4 = rie_ant_psico_4
        self.rie_ant_obs = rie_ant_obs
        self.ocu_equi = ocu_equi
        self.ocu_acti = ocu_acti
        self.ocu_acc_emp1 = ocu_acc_emp1
        self.ocu_acc_diag1 = ocu_acc_diag1
        self.ocu_acc_emp2 = ocu_acc_emp2
        self.ocu_acc_diag2 = ocu_acc_diag2
        self.ocu_obs = ocu_obs
        self.cie_concep_desc = cie_concep_desc
        self.cie_concep_reco = cie_concep_reco
        self.cie_concep_aplaz = cie_concep_aplaz
        self.cie_concep_aplaza = cie_concep_aplaza
        self.cie_concep_reco_mot = cie_concep_reco_mot
        self.cie_obs = cie_obs
        self.cie_concep_fin = cie_concep_fin


    def to_dict(self):
        return dict(
            numero_historia=self.numero_historia,
            documento_paciente=self.documento_paciente,
            estado=self.estado,
            ant_padre_card=self.ant_padre_card,
            ant_madre_card=self.ant_madre_card,
            ant_padre_cong=self.ant_padre_cong,
            ant_madre_cong=self.ant_madre_cong,
            ant_per_pato=self.ant_per_pato,
            ant_per_qui=self.ant_per_qui,
            ant_per_trau=self.ant_per_trau,
            ant_per_toxi=self.ant_per_toxi,
            ant_per_alergi=self.ant_per_alergi,
            ant_per_ets=self.ant_per_ets,
            ant_per_obs1=self.ant_per_obs1,
            ant_per_gin_fup=self.ant_per_gin_fup,
            ant_per_gin_fum=self.ant_per_gin_fum,
            ant_per_gin_plan=self.ant_per_gin_plan,
            ant_per_gin_dism=self.ant_per_gin_dism,
            ant_per_gin_disp=self.ant_per_gin_disp,
            ant_per_gin_mam=self.ant_per_gin_mam,
            ant_per_gin_mens=self.ant_per_gin_mens,
            ant_per_obs2=self.ant_per_obs2,
            inm_hep_a=self.inm_hep_a,
            inm_hep_b=self.inm_hep_b,
            inm_trip=self.inm_trip,
            inm_teta=self.inm_teta,
            inm_mala=self.inm_mala,
            inm_amar=self.inm_amar,
            inm_tifo=self.inm_tifo,
            inm_cov=self.inm_cov,
            mani_ali=self.mani_ali,
            inm_obs=self.inm_obs,
            hab_ciga=self.hab_ciga,
            hab_alco=self.hab_alco,
            hab_drog=self.hab_drog,
            hab_dep=self.hab_dep,
            hab_les=self.hab_les,
            hab_obs=self.hab_obs,
            sis_derma=self.sis_derma,
            sis_ost_musc=self.sis_ost_musc,
            sis_ost_arti=self.sis_ost_arti,
            sis_geni=self.sis_geni,
            sis_meta=self.sis_meta,
            sis_neur=self.sis_neur,
            sis_carf=self.sis_carf,
            sis_endo=self.sis_endo,
            sis_uro=self.sis_uro,
            sis_gatro=self.sis_gatro,
            sis_orl=self.sis_orl,
            rie_exp_fis_1=self.rie_exp_fis_1,
            rie_exp_fis_2=self.rie_exp_fis_2,
            rie_exp_fis_3=self.rie_exp_fis_3,
            rie_exp_fis_4=self.rie_exp_fis_4,
            rie_exp_bio_1=self.rie_exp_bio_1,
            rie_exp_bio_2=self.rie_exp_bio_2,
            rie_exp_bio_3=self.rie_exp_bio_3,
            rie_exp_bio_4=self.rie_exp_bio_4,
            rie_exp_quim_1=self.rie_exp_quim_1,
            rie_exp_quim_2=self.rie_exp_quim_2,
            rie_exp_quim_3=self.rie_exp_quim_3,
            rie_exp_quim_4=self.rie_exp_quim_4,
            rie_exp_seg_1=self.rie_exp_seg_1,
            rie_exp_seg_2=self.rie_exp_seg_2,
            rie_exp_seg_3=self.rie_exp_seg_3,
            rie_exp_seg_4=self.rie_exp_seg_4,
            rie_exp_biom_1=self.rie_exp_biom_1,
            rie_exp_biom_2=self.rie_exp_biom_2,
            rie_exp_biom_3=self.rie_exp_biom_3,
            rie_exp_biom_4=self.rie_exp_biom_4,
            rie_exp_psico_1=self.rie_exp_psico_1,
            rie_exp_psico_2=self.rie_exp_psico_2,
            rie_exp_psico_3=self.rie_exp_psico_3,
            rie_exp_psico_4=self.rie_exp_psico_4,
            rie_exp_obs=self.rie_exp_obs,
            rie_ant_fis_1=self.rie_ant_fis_1,
            rie_ant_fis_2=self.rie_ant_fis_2,
            rie_ant_fis_3=self.rie_ant_fis_3,
            rie_ant_fis_4=self.rie_ant_fis_4,
            rie_ant_bio_1=self.rie_ant_bio_1,
            rie_ant_bio_2=self.rie_ant_bio_2,
            rie_ant_bio_3=self.rie_ant_bio_3,
            rie_ant_bio_4=self.rie_ant_bio_4,
            rie_ant_quim_1=self.rie_ant_quim_1,
            rie_ant_quim_2=self.rie_ant_quim_2,
            rie_ant_quim_3=self.rie_ant_quim_3,
            rie_ant_quim_4=self.rie_ant_quim_4,
            rie_ant_seg_1=self.rie_ant_seg_1,
            rie_ant_seg_2=self.rie_ant_seg_2,
            rie_ant_seg_3=self.rie_ant_seg_3,
            rie_ant_seg_4=self.rie_ant_seg_4,
            rie_ant_biom_1=self.rie_ant_biom_1,
            rie_ant_biom_2=self.rie_ant_biom_2,
            rie_ant_biom_3=self.rie_ant_biom_3,
            rie_ant_biom_4=self.rie_ant_biom_4,
            rie_ant_psico_1=self.rie_ant_psico_1,
            rie_ant_psico_2=self.rie_ant_psico_2,
            rie_ant_psico_3=self.rie_ant_psico_3,
            rie_ant_psico_4=self.rie_ant_psico_4,
            rie_ant_obs=self.rie_ant_obs,
            ocu_equi=self.ocu_equi,
            ocu_acti=self.ocu_acti,
            ocu_acc_emp1=self.ocu_acc_emp1,
            ocu_acc_diag1=self.ocu_acc_diag1,
            ocu_acc_emp2=self.ocu_acc_emp2,
            ocu_acc_diag2=self.ocu_acc_diag2,
            ocu_obs=self.ocu_obs,
            cie_concep_desc=self.cie_concep_desc,
            cie_concep_reco=self.cie_concep_reco,
            cie_concep_aplaz=self.cie_concep_aplaz,
            cie_concep_aplaza=self.cie_concep_aplaza,
            cie_concep_reco_mot=self.cie_concep_reco_mot,
            cie_obs=self.cie_obs,
            cie_concep_fin=self.cie_concep_fin,
            fecha_creacion=str(self.fecha_creacion),
            fecha_cierre=str(self.fecha_cierre)
        )