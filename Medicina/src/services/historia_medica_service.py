from src.models.historia_medica_model import HistoriaMedica
from src.utils.instances import db, rd
from sqlalchemy.exc import IntegrityError

class HistoriaMedicaService():

    def create(self, content):
        doc = content.get("documento_paciente")
        data = dict(
            documento_paciente=doc,
            ant_padre_card = content.get("ant_padre_card"),
            ant_madre_card = content.get("ant_madre_card"),
            ant_padre_cong = content.get("ant_padre_cong"),
            ant_madre_cong = content.get("ant_madre_cong"),
            ant_per_pato = content.get("ant_per_pato"),
            ant_per_qui = content.get("ant_per_qui"),
            ant_per_trau = content.get("ant_per_trau"),
            ant_per_toxi = content.get("ant_per_toxi"),
            ant_per_alergi = content.get("ant_per_alergi"),
            ant_per_ets = content.get("ant_per_ets"),
            ant_per_obs1 = content.get("ant_per_obs1"),
            ant_per_gin_fup = content.get("ant_per_gin_fup"),
            ant_per_gin_fum = content.get("ant_per_gin_fum"),
            ant_per_gin_plan = content.get("ant_per_gin_plan"),
            ant_per_gin_dism = content.get("ant_per_gin_dism"),
            ant_per_gin_disp = content.get("ant_per_gin_disp"),
            ant_per_gin_mam = content.get("ant_per_gin_mam"),
            ant_per_gin_mens = content.get("ant_per_gin_mens"),
            ant_per_obs2 = content.get("ant_per_obs2"),
            inm_hep_a = content.get("inm_hep_a"),
            inm_hep_b = content.get("inm_hep_b"),
            inm_trip = content.get("inm_trip"),
            inm_teta = content.get("inm_teta"),
            inm_mala = content.get("inm_mala"),
            inm_amar = content.get("inm_amar"),
            inm_tifo = content.get("inm_tifo"),
            inm_cov = content.get("inm_cov"),
            mani_ali = content.get("mani_ali"),
            inm_obs = content.get("inm_obs"),
            hab_ciga = content.get("hab_ciga"),
            hab_alco = content.get("hab_alco"),
            hab_drog = content.get("hab_drog"),
            hab_dep = content.get("hab_dep"),
            hab_les = content.get("hab_les"),
            hab_obs = content.get("hab_obs"),
            sis_derma = content.get("sis_derma"),
            sis_ost_musc = content.get("sis_ost_musc"),
            sis_ost_arti = content.get("sis_ost_arti"),
            sis_geni = content.get("sis_geni"),
            sis_meta = content.get("sis_meta"),
            sis_neur = content.get("sis_neur"),
            sis_carf = content.get("sis_carf"),
            sis_endo = content.get("sis_endo"),
            sis_uro = content.get("sis_uro"),
            sis_gatro = content.get("sis_gatro"),
            sis_orl = content.get("sis_orl"),
            rie_exp_fis_1 = content.get("rie_exp_fis_1"),
            rie_exp_fis_2 = content.get("rie_exp_fis_2"),
            rie_exp_fis_3 = content.get("rie_exp_fis_3"),
            rie_exp_fis_4 = content.get("rie_exp_fis_4"),
            rie_exp_bio_1 = content.get("rie_exp_bio_1"),
            rie_exp_bio_2 = content.get("rie_exp_bio_2"),
            rie_exp_bio_3 = content.get("rie_exp_bio_3"),
            rie_exp_bio_4 = content.get("rie_exp_bio_4"),
            rie_exp_quim_1 = content.get("rie_exp_quim_1"),
            rie_exp_quim_2 = content.get("rie_exp_quim_2"),
            rie_exp_quim_3 = content.get("rie_exp_quim_3"),
            rie_exp_quim_4 = content.get("rie_exp_quim_4"),
            rie_exp_seg_1 = content.get("rie_exp_seg_1"),
            rie_exp_seg_2 = content.get("rie_exp_seg_2"),
            rie_exp_seg_3 = content.get("rie_exp_seg_3"),
            rie_exp_seg_4 = content.get("rie_exp_seg_4"),
            rie_exp_biom_1 = content.get("rie_exp_biom_1"),
            rie_exp_biom_2 = content.get("rie_exp_biom_2"),
            rie_exp_biom_3 = content.get("rie_exp_biom_3"),
            rie_exp_biom_4 = content.get("rie_exp_biom_4"),
            rie_exp_psico_1 = content.get("rie_exp_psico_1"),
            rie_exp_psico_2 = content.get("rie_exp_psico_2"),
            rie_exp_psico_3 = content.get("rie_exp_psico_3"),
            rie_exp_psico_4 = content.get("rie_exp_psico_4"),
            rie_exp_obs = content.get("rie_exp_obs"),
            rie_ant_fis_1 = content.get("rie_ant_fis_1"),
            rie_ant_fis_2 = content.get("rie_ant_fis_2"),
            rie_ant_fis_3 = content.get("rie_ant_fis_3"),
            rie_ant_fis_4 = content.get("rie_ant_fis_4"),
            rie_ant_bio_1 = content.get("rie_ant_bio_1"),
            rie_ant_bio_2 = content.get("rie_ant_bio_2"),
            rie_ant_bio_3 = content.get("rie_ant_bio_3"),
            rie_ant_bio_4 = content.get("rie_ant_bio_4"),
            rie_ant_quim_1 = content.get("rie_ant_quim_1"),
            rie_ant_quim_2 = content.get("rie_ant_quim_2"),
            rie_ant_quim_3 = content.get("rie_ant_quim_3"),
            rie_ant_quim_4 = content.get("rie_ant_quim_4"),
            rie_ant_seg_1 = content.get("rie_ant_seg_1"),
            rie_ant_seg_2 = content.get("rie_ant_seg_2"),
            rie_ant_seg_3 = content.get("rie_ant_seg_3"),
            rie_ant_seg_4 = content.get("rie_ant_seg_4"),
            rie_ant_biom_1 = content.get("rie_ant_biom_1"),
            rie_ant_biom_2 = content.get("rie_ant_biom_2"),
            rie_ant_biom_3 = content.get("rie_ant_biom_3"),
            rie_ant_biom_4 = content.get("rie_ant_biom_4"),
            rie_ant_psico_1 = content.get("rie_ant_psico_1"),
            rie_ant_psico_2 = content.get("rie_ant_psico_2"),
            rie_ant_psico_3 = content.get("rie_ant_psico_3"),
            rie_ant_psico_4 = content.get("rie_ant_psico_4"),
            rie_ant_obs = content.get("rie_ant_obs"),
            ocu_equi = content.get("ocu_equi"),
            ocu_acti = content.get("ocu_acti"),
            ocu_acc_emp1 = content.get("ocu_acc_emp1"),
            ocu_acc_diag1 = content.get("ocu_acc_diag1"),
            ocu_acc_emp2 = content.get("ocu_acc_emp2"),
            ocu_acc_diag2 = content.get("ocu_acc_diag2"),
            ocu_obs = content.get("ocu_obs"),
            cie_concep_desc = content.get("cie_concep_desc"),
            cie_concep_reco = content.get("cie_concep_reco"),
            cie_concep_aplaz = content.get("cie_concep_aplaz"),
            cie_concep_aplaza = content.get("cie_concep_aplaza"),
            cie_concep_reco_mot = content.get("cie_concep_reco_mot"),
            cie_obs = content.get("cie_obs"),
            cie_concep_fin = content.get("cie_concep_fin")
        )
        encontrado = rd.hgetall(f"documento_paciente:{doc}")
        if encontrado:
            return self.update(content)  
        try:
            historia = HistoriaMedica(**data)
            db.session.add(
                historia
            )
            db.session.commit()
            rd.hmset(f"documento_paciente:{doc}", historia.to_dict())
            return ({
                "response": "Historia médica creada correctamente."
            }, 201)
            
        except Exception as e:
            db.session.rollback()
            return ({
                "response": str(e),
            }, 400)

    def get(self, doc):
        historia = rd.hgetall(f"documento_paciente:{doc}")
        if historia:
            historia["estado"] = bool(int(historia["estado"]))
            historia["cie_concep_aplaza"] = bool(int(historia["cie_concep_aplaza"]))
        return ({
            "response": historia
        }, 200)
    
    def update(self, content):
        historia = HistoriaMedica.query.filter_by(documento_paciente=content.get("documento_paciente")).first()
        
        if not historia:
            return ({
                "response": "No existe una historia médica con ese documento."
            }, 406)

        if not historia.estado:
            return ({
                "response": "La historia médica ha sido cerrada y no se puede modificar"
            }, 401)

        historia.estado = content.get("estado")
        historia.ant_padre_card = content.get("ant_padre_card")
        historia.ant_madre_card = content.get("ant_madre_card")
        historia.ant_padre_cong = content.get("ant_padre_cong")
        historia.ant_madre_cong = content.get("ant_madre_cong")
        historia.ant_per_pato = content.get("ant_per_pato")
        historia.ant_per_qui = content.get("ant_per_qui")
        historia.ant_per_trau = content.get("ant_per_trau")
        historia.ant_per_toxi = content.get("ant_per_toxi")
        historia.ant_per_alergi = content.get("ant_per_alergi")
        historia.ant_per_ets = content.get("ant_per_ets")
        historia.ant_per_obs1 = content.get("ant_per_obs1")
        historia.ant_per_gin_fup = content.get("ant_per_gin_fup")
        historia.ant_per_gin_fum = content.get("ant_per_gin_fum")
        historia.ant_per_gin_plan = content.get("ant_per_gin_plan")
        historia.ant_per_gin_dism = content.get("ant_per_gin_dism")
        historia.ant_per_gin_disp = content.get("ant_per_gin_disp")
        historia.ant_per_gin_mam = content.get("ant_per_gin_mam")
        historia.ant_per_gin_mens = content.get("ant_per_gin_mens")
        historia.ant_per_obs2 = content.get("ant_per_obs2")
        historia.inm_hep_a = content.get("inm_hep_a")
        historia.inm_hep_b = content.get("inm_hep_b")
        historia.inm_trip = content.get("inm_trip")
        historia.inm_teta = content.get("inm_teta")
        historia.inm_mala = content.get("inm_mala")
        historia.inm_amar = content.get("inm_amar")
        historia.inm_tifo = content.get("inm_tifo")
        historia.inm_cov = content.get("inm_cov")
        historia.mani_ali = content.get("mani_ali")
        historia.inm_obs = content.get("inm_obs")
        historia.hab_ciga = content.get("hab_ciga")
        historia.hab_alco = content.get("hab_alco")
        historia.hab_drog = content.get("hab_drog")
        historia.hab_dep = content.get("hab_dep")
        historia.hab_les = content.get("hab_les")
        historia.hab_obs = content.get("hab_obs")
        historia.sis_derma = content.get("sis_derma")
        historia.sis_ost_musc = content.get("sis_ost_musc")
        historia.sis_ost_arti = content.get("sis_ost_arti")
        historia.sis_geni = content.get("sis_geni")
        historia.sis_meta = content.get("sis_meta")
        historia.sis_neur = content.get("sis_neur")
        historia.sis_carf = content.get("sis_carf")
        historia.sis_endo = content.get("sis_endo")
        historia.sis_uro = content.get("sis_uro")
        historia.sis_gatro = content.get("sis_gatro")
        historia.sis_orl = content.get("sis_orl")
        historia.rie_exp_fis_1 = content.get("rie_exp_fis_1")
        historia.rie_exp_fis_2 = content.get("rie_exp_fis_2")
        historia.rie_exp_fis_3 = content.get("rie_exp_fis_3")
        historia.rie_exp_fis_4 = content.get("rie_exp_fis_4")
        historia.rie_exp_bio_1 = content.get("rie_exp_bio_1")
        historia.rie_exp_bio_2 = content.get("rie_exp_bio_2")
        historia.rie_exp_bio_3 = content.get("rie_exp_bio_3")
        historia.rie_exp_bio_4 = content.get("rie_exp_bio_4")
        historia.rie_exp_quim_1 = content.get("rie_exp_quim_1")
        historia.rie_exp_quim_2 = content.get("rie_exp_quim_2")
        historia.rie_exp_quim_3 = content.get("rie_exp_quim_3")
        historia.rie_exp_quim_4 = content.get("rie_exp_quim_4")
        historia.rie_exp_seg_1 = content.get("rie_exp_seg_1")
        historia.rie_exp_seg_2 = content.get("rie_exp_seg_2")
        historia.rie_exp_seg_3 = content.get("rie_exp_seg_3")
        historia.rie_exp_seg_4 = content.get("rie_exp_seg_4")
        historia.rie_exp_biom_1 = content.get("rie_exp_biom_1")
        historia.rie_exp_biom_2 = content.get("rie_exp_biom_2")
        historia.rie_exp_biom_3 = content.get("rie_exp_biom_3")
        historia.rie_exp_biom_4 = content.get("rie_exp_biom_4")
        historia.rie_exp_psico_1 = content.get("rie_exp_psico_1")
        historia.rie_exp_psico_2 = content.get("rie_exp_psico_2")
        historia.rie_exp_psico_3 = content.get("rie_exp_psico_3")
        historia.rie_exp_psico_4 = content.get("rie_exp_psico_4")
        historia.rie_exp_obs = content.get("rie_exp_obs")
        historia.rie_ant_fis_1 = content.get("rie_ant_fis_1")
        historia.rie_ant_fis_2 = content.get("rie_ant_fis_2")
        historia.rie_ant_fis_3 = content.get("rie_ant_fis_3")
        historia.rie_ant_fis_4 = content.get("rie_ant_fis_4")
        historia.rie_ant_bio_1 = content.get("rie_ant_bio_1")
        historia.rie_ant_bio_2 = content.get("rie_ant_bio_2")
        historia.rie_ant_bio_3 = content.get("rie_ant_bio_3")
        historia.rie_ant_bio_4 = content.get("rie_ant_bio_4")
        historia.rie_ant_quim_1 = content.get("rie_ant_quim_1")
        historia.rie_ant_quim_2 = content.get("rie_ant_quim_2")
        historia.rie_ant_quim_3 = content.get("rie_ant_quim_3")
        historia.rie_ant_quim_4 = content.get("rie_ant_quim_4")
        historia.rie_ant_seg_1 = content.get("rie_ant_seg_1")
        historia.rie_ant_seg_2 = content.get("rie_ant_seg_2")
        historia.rie_ant_seg_3 = content.get("rie_ant_seg_3")
        historia.rie_ant_seg_4 = content.get("rie_ant_seg_4")
        historia.rie_ant_biom_1 = content.get("rie_ant_biom_1")
        historia.rie_ant_biom_2 = content.get("rie_ant_biom_2")
        historia.rie_ant_biom_3 = content.get("rie_ant_biom_3")
        historia.rie_ant_biom_4 = content.get("rie_ant_biom_4")
        historia.rie_ant_psico_1 = content.get("rie_ant_psico_1")
        historia.rie_ant_psico_2 = content.get("rie_ant_psico_2")
        historia.rie_ant_psico_3 = content.get("rie_ant_psico_3")
        historia.rie_ant_psico_4 = content.get("rie_ant_psico_4")
        historia.rie_ant_obs = content.get("rie_ant_obs")
        historia.ocu_equi = content.get("ocu_equi")
        historia.ocu_acti = content.get("ocu_acti")
        historia.ocu_acc_emp1 = content.get("ocu_acc_emp1")
        historia.ocu_acc_diag1 = content.get("ocu_acc_diag1")
        historia.ocu_acc_emp2 = content.get("ocu_acc_emp2")
        historia.ocu_acc_diag2 = content.get("ocu_acc_diag2")
        historia.ocu_obs = content.get("ocu_obs")
        historia.cie_concep_desc = content.get("cie_concep_desc")
        historia.cie_concep_reco = content.get("cie_concep_reco")
        historia.cie_concep_aplaz = content.get("cie_concep_aplaz")
        historia.cie_concep_aplaza = content.get("cie_concep_aplaza")
        historia.cie_concep_reco_mot = content.get("cie_concep_reco_mot")
        historia.cie_obs = content.get("cie_obs")
        historia.cie_concep_fin = content.get("cie_concep_fin")
        db.session.commit()
        return ({
            "response": "La historia médica se ha actualizada"
        }, 200)