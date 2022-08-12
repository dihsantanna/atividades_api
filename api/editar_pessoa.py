import json
from flask import Response
from db.editar_pessoa import editar_pessoa as service


def editar_pessoa(body, id=None, nome=None):
    if not body:
        return Response(
            json.dumps({"message": "Nenhum parâmetro informado"}), status=400
        )

    resultado = service(body=body, id=id, nome=nome)
    if not resultado:
        return Response(
            response=json.dumps({"message": "Pessoa não encontrada"}), status=404
        )
    else:
        return {
            "id": resultado.id,
            "nome": resultado.nome,
            "idade": resultado.idade,
        }
