from .model import Atividades


def editar_pessoa(body, id, nome):
    pessoa = None
    if id:
        pessoa = Atividades.query.filter_by(id=id).first()
    if nome:
        pessoa = Atividades.query.filter_by(nome=nome).first()
    if pessoa:
        pessoa.nome = body["nome"] if "nome" in body else pessoa.nome
        pessoa.idade = body["idade"] if "idade" in body else pessoa.idade
        pessoa.save()

    return pessoa
