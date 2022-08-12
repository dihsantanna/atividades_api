from .model import Atividades


def deletar_pessoa(id):
    pessoa = Atividades.query.filter_by(id=id).first()
    if not pessoa:
        return None
    pessoa.delete()
    return pessoa


if __name__ == "__main__":
    print("Digite o ID da pessoa a ser deletada:")
    id = input("ID: ")
    while not id or not id.isdigit():
        print("Por favor, digite um ID válido.")
        id = input("ID: ")

    deletar_pessoa(int(id))
