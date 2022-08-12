from .model import Pessoas


def consultar_pessoas(nome=None, id=None):
    if id and not nome:
        return Pessoas.query.filter_by(id=id).first()
    elif nome and not id:
        return Pessoas.query.filter_by(nome=nome).first()
    else:
        return Pessoas.query.all()
