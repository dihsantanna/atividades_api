from .model import Atividades


def consultar_pessoas(nome=None, id=None):
    if id and not nome:
        return Atividades.query.filter_by(id=id).first()
    elif nome and not id:
        return Atividades.query.filter_by(nome=nome).first()
    else:
        return Atividades.query.all()
