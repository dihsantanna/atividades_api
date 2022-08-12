from model import Pessoas


def inserir_pessoa(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    print({"id": pessoa.id, "nome": pessoa.nome, "idade": pessoa.idade})


if __name__ == "__main__":
    print("Para inserir uma pessoa, digite:")
    inserir_pessoa(input("Nome: "), int(input("Idade: ")))
    print("Pessoa inserida com sucesso!")
