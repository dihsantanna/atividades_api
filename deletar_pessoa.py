from model import Pessoas


def deletar_pessoa(id):
    pessoa = Pessoas.query.filter_by(id=id).first()
    if not pessoa:
        print(f"ID {id} não encontrado(a).")
        return

    pessoa.delete()
    print(f"{pessoa.nome} foi removido(a) com sucesso!")


if __name__ == "__main__":
    print("Digite o ID da pessoa a ser deletada:")
    id = input("ID: ")
    while not id or not id.isdigit():
        print("Por favor, digite um ID válido.")
        id = input("ID: ")

    deletar_pessoa(int(id))
