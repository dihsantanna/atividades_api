from model import Pessoas


def consultar_pessoas(nome=None):
    if nome:
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        if not pessoa:
            print(f"{nome} não foi encontrado(a).")
            return
        print({"id": pessoa.id, "nome": pessoa.nome, "idade": pessoa.idade})
    else:
        pessoas = Pessoas.query.all()
        print(
            [
                {"id": pessoa.id, "nome": pessoa.nome, "idade": pessoa.idade}
                for pessoa in pessoas
            ]
        )


if __name__ == "__main__":
    print(
        "Digite um nome para consultar uma pessoa, caso queira consultar todas as pessoas, deixe o nome em branco."
    )
    consultar_pessoas(input("Nome: "))
