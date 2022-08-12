import json
from flask import Response
from db.inserir_pessoa import inserir_pessoa as service


def inserir_pessoa(body):

    if not body["nome"] or not body["idade"]:
        return Response(
            response=json.dumps({"message": "Preencha todos os campos"}), status=400
        )

    resultado = service(nome=body["nome"], idade=body["idade"])

    if not resultado:
        return Response(
            response=json.dumps({"message": "Não foi possível inserir a nova pessoa."}),
            status=500,
        )
    else:
        return Response(
            response=json.dumps(
                {
                    "id": resultado.id,
                    "nome": resultado.nome,
                    "idade": resultado.idade,
                }
            ),
            status=201,
        )
