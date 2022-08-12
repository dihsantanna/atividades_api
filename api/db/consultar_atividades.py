from .model import Atividades


def consultar_atividades(id=None, pessoa_id=None):
    if id:
        return Atividades.query.filter_by(id=id).first()
    elif pessoa_id:
        return Atividades.query.filter_by(pessoa_id=pessoa_id).all()
    else:
        return Atividades.query.all()
