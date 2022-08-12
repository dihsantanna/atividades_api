import json
from flask import Response
from db.deletar_pessoa import deletar_pessoa as service


def deletar_pessoa(id):
    if not id:
        return Response(json.dumps({"message": "ID deve ser informado"}), status=400)

    resultado = service(id=id)
    if not resultado:
        return Response(
            response=json.dumps({"message": "Pessoa não encontrada"}), status=404
        )
    else:
        return Response(
            response=json.dumps(
                {"message": f"{resultado.nome} foi removido(a) com sucesso!"}
            ),
            status=200,
        )
