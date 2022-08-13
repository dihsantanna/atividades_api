from .model import Atividades


def inserir_atividades(nome, pessoa_id):
    atividade = Atividades(nome=nome, pessoa_id=pessoa_id).first()
    if not atividade:
        return None
    atividade.save()
    return atividade
