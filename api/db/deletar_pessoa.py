from .model import Pessoas


def deletar_pessoa(id):
    pessoa = Pessoas.query.filter_by(id=id).first()
    if not pessoa:
        return None
    pessoa.delete()
    return pessoa
