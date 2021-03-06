from marshmallow import Schema, fields, validate
from src.models.anexos import anexos as a
from src.config import APP

def validar_fecha(fecha):
    fecha = fecha.split("-")
    try:
        anio = True if len(fecha[0]) == 4 and int(fecha[0]) > 1800 and int(fecha[0]) < 2023 else False
        mes = True if len(fecha[1]) == 2 and int(fecha[1]) > 0 and int(fecha[1]) < 13 else False
        dia = True if len(fecha[2]) == 2 and int(fecha[2]) > 0 and int(fecha[2]) < 32 else False
        return True if anio and mes and dia else False

    except:
        return False

class HistoriaMedicaSchema(Schema):
    estado = fields.Bool(required=True)
    documento_paciente = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    ant_padre_card = fields.Str(required=True, validate=lambda x: x in a.PATOLOGICOS)
    ant_madre_card = fields.Str(required=True, validate=lambda x: x in a.PATOLOGICOS)
    ant_padre_cong = fields.Str(required=True, validate=lambda x: x in a.PATOLOGICOS)
    ant_madre_cong = fields.Str(required=True, validate=lambda x: x in a.PATOLOGICOS)
    ant_per_pato = fields.Str(required=True, validate=lambda x: x in a.PATOLOGICOS)
    ant_per_qui = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    ant_per_trau = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    ant_per_toxi = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    ant_per_alergi = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    farmacologicos = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    transfusionales = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    ant_per_ets = fields.Str(required=True, validate=lambda x: x in a.ETS)
    ant_per_obs1 = fields.Str(required=True, validate=validate.Length(max=500))
    ant_per_gin_fup = fields.Str(required=True, validate=lambda x: validar_fecha(x))
    ant_per_gin_fum = fields.Str(required=True, validate=lambda x: validar_fecha(x))
    ant_per_gin_plan = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_per_gin_dism = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_per_gin_disp = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_per_gin_mam = fields.Str(required=True, validate=lambda x: validar_fecha(x))
    ant_per_gin_mens = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    ant_per_obs2 = fields.Str(required=True, validate=validate.Length(max=500))
    inm_hep_a = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_hep_b = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_trip = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_teta = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_mala = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_amar = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_tifo = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    inm_cov = fields.Str(required=True, validate=lambda x: x in a.NRO_VACUNA)
    mani_ali = fields.Str(required=True, validate=lambda x: validar_fecha(x))
    inm_obs = fields.Str(required=True, validate=validate.Length(max=500))
    hab_ciga = fields.Str(required=True, validate=lambda x: x in a.SINO)
    hab_alco = fields.Str(required=True, validate=lambda x: x in a.SINO)
    hab_drog = fields.Str(required=True, validate=lambda x: x in a.SINO)
    hab_dep = fields.Str(required=True, validate=lambda x: x in a.SINO)
    hab_les = fields.Str(required=True, validate=lambda x: x in a.SINO)
    hab_obs = fields.Str(required=True, validate=validate.Length(max=500))
    sis_derma = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_ost_musc = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_ost_arti = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_geni = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_meta = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_neur = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_carf = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_endo = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_uro = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_gatro = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    sis_orl = fields.Str(required=True, validate=lambda x: x in a.REFERENCIA)
    rie_exp_fis_1 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_exp_fis_2 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_exp_fis_3 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_exp_fis_4 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_exp_bio_1 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_exp_bio_2 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_exp_bio_3 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_exp_bio_4 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_exp_quim_1 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_exp_quim_2 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_exp_quim_3 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_exp_quim_4 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_exp_seg_1 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_exp_seg_2 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_exp_seg_3 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_exp_seg_4 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_exp_biom_1 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_exp_biom_2 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_exp_biom_3 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_exp_biom_4 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_exp_psico_1 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_exp_psico_2 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_exp_psico_3 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_exp_psico_4 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_exp_obs = fields.Str(required=True, validate=validate.Length(max=500))
    rie_ant_fis_1 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_ant_fis_2 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_ant_fis_3 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_ant_fis_4 = fields.Str(required=True, validate=lambda x: x in a.FISICO)
    rie_ant_bio_1 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_ant_bio_2 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_ant_bio_3 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_ant_bio_4 = fields.Str(required=True, validate=lambda x: x in a.BIOLOGICO)
    rie_ant_quim_1 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_ant_quim_2 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_ant_quim_3 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_ant_quim_4 = fields.Str(required=True, validate=lambda x: x in a.QUIMICO)
    rie_ant_seg_1 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_ant_seg_2 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_ant_seg_3 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_ant_seg_4 = fields.Str(required=True, validate=lambda x: x in a.SEGURIDAD)
    rie_ant_biom_1 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_ant_biom_2 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_ant_biom_3 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_ant_biom_4 = fields.Str(required=True, validate=lambda x: x in a.BIOMECANICO)
    rie_ant_psico_1 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_ant_psico_2 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_ant_psico_3 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_ant_psico_4 = fields.Str(required=True, validate=lambda x: x in a.PSICOSOCIAL)
    rie_ant_obs = fields.Str(required=True, validate=validate.Length(max=500))
    ocu_equi = fields.Str(required=True, validate=lambda x: x in a.EQUIPOS_UTILIZADOS)
    ocu_acti = fields.Str(required=True, validate=validate.Length(max=100))
    ocu_acc_emp1 = fields.Str(required=True, validate=validate.Length(max=100))
    ocu_acc_diag1 = fields.Str(required=True, validate=validate.Length(max=500))
    ocu_acc_emp2 = fields.Str(required=True, validate=validate.Length(max=100))
    ocu_acc_diag2 = fields.Str(required=True, validate=validate.Length(max=500))
    histo_famili = fields.Str(required=True, validate=validate.Length(max=500))
    cie_concep_reco = fields.Str(required=True, validate=validate.Length(max=300))
    cie_concep_reco_mot = fields.Str(required=True, validate=lambda x: x in a.REMITIDO)
    cie_obs = fields.Str(required=True, validate=validate.Length(max=500))
    concepto = fields.Str(required=True, validate=lambda x: x in a.CONCEPTO)
    motivo = fields.Str(required=True, validate=lambda x: x in a.MOTIVO)
    select1Emp1 = fields.Str(required=False)
    select1Emp2 = fields.Str(required=False)
    select2Emp1 = fields.Str(required=False)
    select2Emp2 = fields.Str(required=False)
    select3Emp1 = fields.Str(required=False)
    select3Emp2 = fields.Str(required=False)