from .model import Pessoas


def inserir_pessoa(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    return pessoa
