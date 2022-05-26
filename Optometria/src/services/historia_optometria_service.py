from src.models.historia_optometria_model import HistoriaOptometria
from src.utils.instances import db
from sqlalchemy import select, desc
from src.utils.functions import get_datetime

class HistoriaOptometriaService():

    def buscar_num_historia(self, doc):
        stmt = select(
            HistoriaOptometria.numero_historia
            ).where(
                HistoriaOptometria.documento_paciente == doc
            ).order_by(
                desc(HistoriaOptometria.numero_historia)
            )
        historias = db.session.execute(stmt).fetchall()
        if historias:
            return historias[0][0]
        return 0

    def create(self, content):
        doc = content.get("documento_paciente")
        data = dict(
            documento_paciente=doc,
            estado=content.get("estado"),
            ant_def_refra=content.get("ant_def_refra"),
            ant_def_cx=content.get("ant_def_cx"),
            ant_estra=content.get("ant_estra"),
            ant_pato=content.get("ant_pato"),
            ant_tto=content.get("ant_tto"),
            ant_hiper=content.get("ant_hiper"),
            ant_diab=content.get("ant_diab"),
            ant_desor=content.get("ant_desor"),
            ant_acc=content.get("ant_acc"),
            ant_trau=content.get("ant_trau"),
            ant_obs=content.get("ant_obs"),
            ant_ocu_exp_vide=content.get("ant_ocu_exp_vide"),
            ant_ocu_acc=content.get("ant_ocu_acc"),
            ant_ocu_temp=content.get("ant_ocu_temp"),
            ant_ocu_mate=content.get("ant_ocu_mate"),
            ant_ocu_ra_no_io=content.get("ant_ocu_ra_no_io"),
            ant_ocu_ra_io=content.get("ant_ocu_ra_io"),
            ant_ocu_exp_quim=content.get("ant_ocu_exp_quim"),
            ant_ocu_exp_solv=content.get("ant_ocu_exp_solv"),
            ant_ocu_obs=content.get("ant_ocu_obs"),
            sis_mal_lej=content.get("sis_mal_lej"),
            sis_mal_cer=content.get("sis_mal_cer"),
            sis_cel=content.get("sis_cel"),
            sis_hiper=content.get("sis_hiper"),
            sis_vis_dob=content.get("sis_vis_dob"),
            sis_vert=content.get("sis_vert"),
            sis_lagri=content.get("sis_lagri"),
            sis_mare=content.get("sis_mare"),
            sis_secr=content.get("sis_secr"),
            sis_rese=content.get("sis_rese"),
            sis_otro=content.get("sis_otro"),
            agu_cer_sc1=content.get("agu_cer_sc1"),
            agu_cer_sc2=content.get("agu_cer_sc2"),
            agu_cer_sc3=content.get("agu_cer_sc3"),
            agu_cer_cc1=content.get("agu_cer_cc1"),
            agu_cer_cc2=content.get("agu_cer_cc2"),
            agu_cer_cc3=content.get("agu_cer_cc3"),
            agu_lej_sc1=content.get("agu_lej_sc1"),
            agu_lej_sc2=content.get("agu_lej_sc2"),
            agu_lej_sc3=content.get("agu_lej_sc3"),
            agu_lej_cc1=content.get("agu_lej_cc1"),
            agu_lej_cc2=content.get("agu_lej_cc2"),
            agu_lej_cc3=content.get("agu_lej_cc3"),
            agu_len_pre_od1=content.get("agu_len_pre_od1"),
            agu_len_pre_od2=content.get("agu_len_pre_od2"),
            agu_len_pre_oi1=content.get("agu_len_pre_oi1"),
            agu_len_pre_oi2=content.get("agu_len_pre_oi2"),
            agu_len_tiem=content.get("agu_len_tiem"),
            hal_ext_od=content.get("hal_ext_od"),
            hal_mot_od=content.get("hal_mot_od"),
            hal_ofta_od=content.get("hal_ofta_od"),
            hal_camp_od=content.get("hal_camp_od"),
            hal_est_od=content.get("hal_est_od"),
            hal_crom_od=content.get("hal_crom_od"),
            hal_ext_oi=content.get("hal_ext_oi"),
            hal_mot_oi=content.get("hal_mot_oi"),
            hal_ofta_oi=content.get("hal_ofta_oi"),
            hal_camp_oi=content.get("hal_camp_oi"),
            hal_est_oi=content.get("hal_est_oi"),
            hal_crom_oi=content.get("hal_crom_oi"),
            hal_obs=content.get("hal_obs"),
            cie_concep_desc=content.get("cie_concep_desc"),
            cie_concep_reco=content.get("cie_concep_reco"),
            cie_concep_aplaz=content.get("cie_concep_aplaz"),
            cie_concep_reco_mot=content.get("cie_concep_reco_mot"),
            cie_obs=content.get("cie_obs"),
            cie_concep_fin=content.get("cie_concep_fin")
        )
        num_historia = self.buscar_num_historia(doc)
        abierta = HistoriaOptometria.query.filter_by(numero_historia=num_historia).first()
        if abierta:
            if abierta.estado:
                return self.update(content)
        try:
            data["numero_historia"] = num_historia + 1
            historia = HistoriaOptometria(**data)
            db.session.add(historia)
            db.session.commit()
            return ({
                "response": "Historia de optometría creada correctamente."
            }, 201)

        except Exception as e:
            db.session.rollback()
            return ({
                "response": str(e),
            }, 400)

    def get(self, doc):
        historias = HistoriaOptometria.query.filter_by(documento_paciente=doc).all()
        data = [{x.to_dict().get("documento_paciente") + "-" + str(x.to_dict().get("numero_historia")):x.to_dict()} for x in historias]
        return ({
            "response": {
                "historias_optometria": data
            }
        }, 200)
    
    def update(self, content):
        doc = content.get("documento_paciente")
        num_historia = self.buscar_num_historia(doc)
        historia = HistoriaOptometria.query.filter_by(documento_paciente=doc, numero_historia=num_historia).first()

        if not historia:
            return ({
                "response": "No existe una historia de optometría con ese documento."
            }, 406)

        if not historia.estado:
            return ({
                "response": "La historia de optometría ha sido cerrada y no se puede modificar"
            }, 401)

        historia.estado = content.get("estado")
        historia.ant_def_refra = content.get("ant_def_refra")
        historia.ant_def_cx = content.get("ant_def_cx")
        historia.ant_estra = content.get("ant_estra")
        historia.ant_pato = content.get("ant_pato")
        historia.ant_tto = content.get("ant_tto")
        historia.ant_hiper = content.get("ant_hiper")
        historia.ant_diab = content.get("ant_diab")
        historia.ant_desor = content.get("ant_desor")
        historia.ant_acc = content.get("ant_acc")
        historia.ant_trau = content.get("ant_trau")
        historia.ant_obs = content.get("ant_obs")
        historia.ant_ocu_exp_vide = content.get("ant_ocu_exp_vide")
        historia.ant_ocu_acc = content.get("ant_ocu_acc")
        historia.ant_ocu_temp = content.get("ant_ocu_temp")
        historia.ant_ocu_mate = content.get("ant_ocu_mate")
        historia.ant_ocu_ra_no_io = content.get("ant_ocu_ra_no_io")
        historia.ant_ocu_ra_io = content.get("ant_ocu_ra_io")
        historia.ant_ocu_exp_quim = content.get("ant_ocu_exp_quim")
        historia.ant_ocu_exp_solv = content.get("ant_ocu_exp_solv")
        historia.ant_ocu_obs = content.get("ant_ocu_obs")
        historia.sis_mal_lej = content.get("sis_mal_lej")
        historia.sis_mal_cer = content.get("sis_mal_cer")
        historia.sis_cel = content.get("sis_cel")
        historia.sis_hiper = content.get("sis_hiper")
        historia.sis_vis_dob = content.get("sis_vis_dob")
        historia.sis_vert = content.get("sis_vert")
        historia.sis_lagri = content.get("sis_lagri")
        historia.sis_mare = content.get("sis_mare")
        historia.sis_secr = content.get("sis_secr")
        historia.sis_rese = content.get("sis_rese")
        historia.sis_otro = content.get("sis_otro")
        historia.agu_cer_sc1 = content.get("agu_cer_sc1")
        historia.agu_cer_sc2 = content.get("agu_cer_sc2")
        historia.agu_cer_sc3 = content.get("agu_cer_sc3")
        historia.agu_cer_cc1 = content.get("agu_cer_cc1")
        historia.agu_cer_cc2 = content.get("agu_cer_cc2")
        historia.agu_cer_cc3 = content.get("agu_cer_cc3")
        historia.agu_lej_sc1 = content.get("agu_lej_sc1")
        historia.agu_lej_sc2 = content.get("agu_lej_sc2")
        historia.agu_lej_sc3 = content.get("agu_lej_sc3")
        historia.agu_lej_cc1 = content.get("agu_lej_cc1")
        historia.agu_lej_cc2 = content.get("agu_lej_cc2")
        historia.agu_lej_cc3 = content.get("agu_lej_cc3")
        historia.agu_len_pre_od1 = content.get("agu_len_pre_od1")
        historia.agu_len_pre_od2 = content.get("agu_len_pre_od2")
        historia.agu_len_pre_oi1 = content.get("agu_len_pre_oi1")
        historia.agu_len_pre_oi2 = content.get("agu_len_pre_oi2")
        historia.agu_len_tiem = content.get("agu_len_tiem")
        historia.hal_ext_od = content.get("hal_ext_od")
        historia.hal_mot_od = content.get("hal_mot_od")
        historia.hal_ofta_od = content.get("hal_ofta_od")
        historia.hal_camp_od = content.get("hal_camp_od")
        historia.hal_est_od = content.get("hal_est_od")
        historia.hal_crom_od = content.get("hal_crom_od")
        historia.hal_ext_oi = content.get("hal_ext_oi")
        historia.hal_mot_oi = content.get("hal_mot_oi")
        historia.hal_ofta_oi = content.get("hal_ofta_oi")
        historia.hal_camp_oi = content.get("hal_camp_oi")
        historia.hal_est_oi = content.get("hal_est_oi")
        historia.hal_crom_oi = content.get("hal_crom_oi")
        historia.hal_obs = content.get("hal_obs")
        historia.cie_concep_desc = content.get("cie_concep_desc")
        historia.cie_concep_reco = content.get("cie_concep_reco")
        historia.cie_concep_aplaz = content.get("cie_concep_aplaz")
        historia.cie_concep_reco_mot = content.get("cie_concep_reco_mot")
        historia.cie_obs = content.get("cie_obs")
        historia.cie_concep_fin = content.get("cie_concep_fin")
        historia.fecha_cierre = get_datetime()
        db.session.commit()
        return ({
            "response": "La historia médica se ha actualizado"
        }, 200)