from src.models.historia_laboratorio_model import HistoriaLaboratorio
from src.utils.instances import db
from sqlalchemy import select, desc
from src.utils.functions import get_datetime

class HistoriaLaboratorioService():

    def buscar_num_historia(self, doc):
        stmt = select(
            HistoriaLaboratorio.numero_historia
            ).where(
                HistoriaLaboratorio.documento_paciente == doc
            ).order_by(
                desc(HistoriaLaboratorio.numero_historia)
            )
        historias = db.session.execute(stmt).fetchall()
        if historias:
            return historias[0][0]
        return 0

    def create(self, content):
        doc = content.get("documento_paciente")
        data = dict(
            documento_paciente=doc,
            hema = content.get("hema"),
            glice = content.get("glice"),
            colestot = content.get("colestot"),
            coleshdl = content.get("coleshdl"),
            colesldl = content.get("colesldl"),
            trigli = content.get("trigli"),
            parcori = content.get("parcori"),
            culori = content.get("culori"),
            copro = content.get("copro"),
            frotsisfar = content.get("frotsisfar"),
            cultifar = content.get("cultifar"),
            koh = content.get("koh"),
            tsh = content.get("tsh"),
            creat = content.get("creat"),
            funchep = content.get("funchep"),
            protinc = content.get("protinc"),
            pt = content.get("pt"),
            ptt = content.get("ptt"),
            aciuri = content.get("aciuri"),
            antigpros = content.get("antigpros"),
            gasarte = content.get("gasarte"),
            vdrl = content.get("vdrl"),
            gravi = content.get("gravi"),
            otro = content.get("otro"),
            obser1_lab = content.get("obser1_lab"),
            obser2_lab = content.get("obser2_lab"),
        )
        num_historia = self.buscar_num_historia(doc)
        abierta = HistoriaLaboratorio.query.filter_by(numero_historia=num_historia).first()
        if abierta:
            if abierta.estado:
                return self.update(content)
        try:
            data["numero_historia"] = num_historia + 1
            historia = HistoriaLaboratorio(**data)
            db.session.add(historia)
            db.session.commit()
            return ({
                "response": "Historia de laboratorio creada correctamente."
            }, 201)

        except Exception as e:
            db.session.rollback()
            return ({
                "response": str(e),
            }, 400)

    def get(self, doc):
        historias = HistoriaLaboratorio.query.filter_by(documento_paciente=doc).all()
        data = [{x.to_dict().get("documento_paciente") + "-" + str(x.to_dict().get("numero_historia")):x.to_dict()} for x in historias]
        return ({
            "response": {
                "historias_clinicas": data
            }
        }, 200)
    
    def update(self, content):
        doc = content.get("documento_paciente")
        num_historia = self.buscar_num_historia(doc)
        historia = HistoriaLaboratorio.query.filter_by(documento_paciente=doc, numero_historia=num_historia).first()
        
        if not historia:
            return ({
                "response": "No existe una historia de laboratorio con ese documento."
            }, 406)

        if not historia.estado:
            return ({
                "response": "La historia de laboratorio ha sido cerrada y no se puede modificar"
            }, 401)

        historia.estado = content.get("estado")
        historia.documento_paciente = content.get("documento_paciente")
        historia.hema = content.get("hema")
        historia.glice = content.get("glice")
        historia.colestot = content.get("colestot")
        historia.coleshdl = content.get("coleshdl")
        historia.colesldl = content.get("colesldl")
        historia.trigli = content.get("trigli")
        historia.parcori = content.get("parcori")
        historia.culori = content.get("culori")
        historia.copro = content.get("copro")
        historia.frotsisfar = content.get("frotsisfar")
        historia.cultifar = content.get("cultifar")
        historia.koh = content.get("koh")
        historia.tsh = content.get("tsh")
        historia.creat = content.get("creat")
        historia.funchep = content.get("funchep")
        historia.protinc = content.get("protinc")
        historia.pt = content.get("pt")
        historia.ptt = content.get("ptt")
        historia.aciuri = content.get("aciuri")
        historia.antigpros = content.get("antigpros")
        historia.gasarte = content.get("gasarte")
        historia.vdrl = content.get("vdrl")
        historia.gravi = content.get("gravi")
        historia.otro = content.get("otro")
        historia.obser1_lab = content.get("obser1_lab")
        historia.obser2_lab = content.get("obser2_lab")
        historia.fecha_cierre = get_datetime()
        db.session.commit()
        return ({
            "response": "La historia de laboratorio se ha actualizado"
        }, 200)