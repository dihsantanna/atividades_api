from .model import Atividades


def inserir_pessoa(nome, idade):
    pessoa = Atividades(nome=nome, idade=idade)
    pessoa.save()
    return pessoa
