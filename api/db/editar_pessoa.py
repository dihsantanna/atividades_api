from model import Pessoas


def editar_pessoa(id, nome, idade):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.nome = nome or pessoa.nome
    pessoa.idade = idade or pessoa.idade
    pessoa.save()
    print(
        {
            "nome": pessoa.nome,
            "idade": pessoa.idade,
        }
    )


if __name__ == "__main__":
    print("Caso não queira alterar algum campo, deixe o campo em branco.")
    print("Digite os dados da pessoa a ser editada:")
    id = input("ID: ")

    while not id or not id.isdigit():
        print("Por favor, digite um ID válido.")
        id = input("ID: ")

    editar_pessoa(int(id), input("Nome: "), int(input("Idade: ")))
    print("Pessoa editada com sucesso!")
