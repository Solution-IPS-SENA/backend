from marshmallow import Schema, fields
from marshmallow import validate
from src.models.anexos import anexos as a

class HistoriaOptometriaSchema(Schema):
    estado = fields.Bool(required=True)
    documento_paciente = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    ant_def_refra = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_def_cx = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_estra = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_pato = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_tto = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_hiper = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_diab = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_desor = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_acc = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_trau = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_exp_vide = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_acc = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_temp = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_mate = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_ra_no_io = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_ra_io = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_exp_quim = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_exp_solv = fields.Str(required=True, validate=lambda x: x in a.SINO)
    ant_ocu_obs = fields.Str(required=True, validate=validate.Length(max=500))
    sis_mal_lej = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_mal_cer = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_cel = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_hiper = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_vis_dob = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_vert = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_lagri = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_mare = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_secr = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_rese = fields.Str(required=True, validate=lambda x: x in a.SINO)
    sis_otro = fields.Str(required=True, validate=validate.Length(max=500))
    agu_cer_sc1 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_cer_sc2 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_cer_sc3 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_cer_cc1 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_cer_cc2 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_cer_cc3 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_sc1 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_sc2 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_sc3 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_cc1 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_cc2 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_lej_cc3 = fields.Str(required=True, validate=lambda x: x in a.AGUDEZA_VISUAL)
    agu_len_pre_od1 = fields.Str(required=True, validate=lambda x: x in a.SINO)
    agu_len_pre_od2 = fields.Str(required=True, validate=lambda x: x in a.LENSOMETRIA)
    agu_len_pre_oi1 = fields.Str(required=True, validate=lambda x: x in a.SINO)
    agu_len_pre_oi2 = fields.Str(required=True, validate=lambda x: x in a.LENSOMETRIA)
    agu_len_tiem = fields.Str(required=True, validate=lambda x: x in a.TIEMPO)
    hal_ext_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_mot_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_ofta_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_camp_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_est_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_crom_od = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_ext_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_mot_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_ofta_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_camp_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_est_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_crom_oi = fields.Str(required=True, validate=lambda x: x in a.NORMALIDAD)
    hal_obs = fields.Str(required=True, validate=validate.Length(max=500))
    cie_concep_reco = fields.Str(required=True, validate=validate.Length(max=500))
    histo_famili = fields.Str(required=True, validate=validate.Length(max=500))
    ant_obs = fields.Str(required=True, validate=validate.Length(max=500))
    cie_concep_reco_mot = fields.Str(required=True, validate=lambda x: x in a.REMITIDO)
    cie_obs = fields.Str(required=True, validate=validate.Length(max=500))
    concepto = fields.Str(required=True, validate=lambda x: x in a.CONCEPTO)
    motivo = fields.Str(required=True, validate=lambda x: x in a.MOTIVO)