from src.utils.instances import db
from src.models.anexos import anexos
from src.utils.functions import get_datetime

class HistoriaPsicologia(db.Model):
    __tablename__ = 'psicologia'

    general_id = db.Column(db.Integer, primary_key=True)
    numero_historia = db.Column(db.Integer, default=1)
    documento_paciente = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True) # Estado abierto = True
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=get_datetime())
    fecha_cierre = db.Column(db.DateTime, default=get_datetime())
    ant_tra = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_enf = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ant_sueño = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    obs_cond_pres = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_post = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_disc = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_tono = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_arti = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_orien_tiem = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_orien_esp = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    obs_cond_orien_perso = db.Column(db.String(12), nullable=False, default=anexos.ADECUACION[0])
    ries_emp_gest_org = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_carac_org = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_tare = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_grup = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_interf = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_jorna = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_cond = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_carga = db.Column(db.String(2), nullable=False, default=anexos.SINO[0])
    ries_emp_obs = db.Column(db.String(500), nullable=False, default="")
    histo_famili = db.Column(db.String(500), nullable=False, default="")
    cie_concep_desc = db.Column(db.String(500), nullable=False, default="")
    cie_concep_reco = db.Column(db.String(300), nullable=False, default="")
    cie_concep_aplaz = db.Column(db.String(300), nullable=False, default="")
    cie_concep_reco_mot = db.Column(db.String(30), nullable=False, default=anexos.REMITIDO[0])
    cie_obs = db.Column(db.String(500), nullable=False, default="")
    cie_concep_fin = db.Column(db.String(12), nullable=False, default=anexos.APROBACION[0])
    psicosensomotriz = db.Column(db.String(12), nullable=False, default=anexos.APROBACION[0])
    personalidad = db.Column(db.String(12), nullable=False, default=anexos.APROBACION[0])
    inteligencia = db.Column(db.String(12), nullable=False, default=anexos.APROBACION[0])

    def __init__(
            self, documento_paciente, estado, numero_historia, ant_tra,
            ant_enf, ant_sueño, obs_cond_pres, obs_cond_post, obs_cond_disc, 
            obs_cond_tono, obs_cond_arti, obs_cond_orien_tiem, obs_cond_orien_esp, 
            obs_cond_orien_perso, ries_emp_gest_org, ries_emp_carac_org, ries_emp_tare,
            ries_emp_grup, ries_emp_interf, ries_emp_jorna, ries_emp_cond, ries_emp_carga,
            ries_emp_obs, histo_famili, cie_concep_desc, cie_concep_reco, cie_concep_aplaz,
            cie_concep_reco_mot, cie_obs, cie_concep_fin, psicosensomotriz, personalidad,
            inteligencia
        ):
        self.estado = estado
        self.numero_historia = numero_historia
        self.documento_paciente = documento_paciente
        self.ant_tra = ant_tra
        self.ant_enf = ant_enf
        self.ant_sueño = ant_sueño
        self.obs_cond_pres = obs_cond_pres
        self.obs_cond_post = obs_cond_post
        self.obs_cond_disc = obs_cond_disc
        self.obs_cond_tono = obs_cond_tono
        self.obs_cond_arti = obs_cond_arti
        self.obs_cond_orien_tiem = obs_cond_orien_tiem
        self.obs_cond_orien_esp = obs_cond_orien_esp
        self.obs_cond_orien_perso = obs_cond_orien_perso
        self.ries_emp_gest_org = ries_emp_gest_org
        self.ries_emp_carac_org = ries_emp_carac_org
        self.ries_emp_tare = ries_emp_tare
        self.ries_emp_grup = ries_emp_grup
        self.ries_emp_interf = ries_emp_interf
        self.ries_emp_jorna = ries_emp_jorna
        self.ries_emp_cond = ries_emp_cond
        self.ries_emp_carga = ries_emp_carga
        self.ries_emp_obs = ries_emp_obs
        self.histo_famili = histo_famili
        self.cie_concep_desc = cie_concep_desc
        self.cie_concep_reco = cie_concep_reco
        self.cie_concep_aplaz = cie_concep_aplaz
        self.cie_concep_reco_mot = cie_concep_reco_mot
        self.cie_obs = cie_obs
        self.cie_concep_fin = cie_concep_fin
        self.psicosensomotriz = psicosensomotriz
        self.personalidad = personalidad
        self.inteligencia = inteligencia

    def to_dict(self):
        return dict(
            numero_historia=self.numero_historia,
            documento_paciente=self.documento_paciente,
            estado=self.estado,
            fecha_creacion=str(self.fecha_creacion),
            fecha_cierre=str(self.fecha_cierre),
            ant_tra=self.ant_tra,
            ant_enf=self.ant_enf,
            ant_sueño=self.ant_sueño,
            obs_cond_pres=self.obs_cond_pres,
            obs_cond_post=self.obs_cond_post,
            obs_cond_disc=self.obs_cond_disc,
            obs_cond_tono=self.obs_cond_tono,
            obs_cond_arti=self.obs_cond_arti,
            obs_cond_orien_tiem=self.obs_cond_orien_tiem,
            obs_cond_orien_esp=self.obs_cond_orien_esp,
            obs_cond_orien_perso=self.obs_cond_orien_perso,
            ries_emp_gest_org=self.ries_emp_gest_org,
            ries_emp_carac_org=self.ries_emp_carac_org,
            ries_emp_tare=self.ries_emp_tare,
            ries_emp_grup=self.ries_emp_grup,
            ries_emp_interf=self.ries_emp_interf,
            ries_emp_jorna=self.ries_emp_jorna,
            ries_emp_cond=self.ries_emp_cond,
            ries_emp_carga=self.ries_emp_carga,
            ries_emp_obs=self.ries_emp_obs,
            histo_famili=self.histo_famili,
            cie_concep_desc=self.cie_concep_desc,
            cie_concep_reco=self.cie_concep_reco,
            cie_concep_aplaz=self.cie_concep_aplaz,
            cie_concep_reco_mot=self.cie_concep_reco_mot,
            cie_obs=self.cie_obs,
            cie_concep_fin=self.cie_concep_fin,
            psicosensomotriz=self.psicosensomotriz,
            personalidad=self.personalidad,
            inteligencia=self.inteligencia,
        )