from .model import Atividades


def inserir_atividades(nome, pessoa_id):
    pessoa = Atividades(nome=nome, pessoa_id=pessoa_id)
    pessoa.save()
    return pessoa
