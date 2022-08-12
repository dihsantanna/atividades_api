import json
from flask import Response
from db.inserir_atividades import inserir_atividades as service


def inserir_atividade(body, pessoa_id):
    if not "nome" in body:
        return Response(
            response=json.dumps({"message": "Campo 'nome' é obrigatório."}), status=400
        )

    if not pessoa_id:
        return Response(
            response=json.dumps({"message": "Adicione um 'personId' valido."}),
            status=400,
        )

    resultado = service(nome=body["nome"], pessoa_id=pessoa_id)

    if not resultado:
        return Response(
            response=json.dumps(
                {"message": "Não foi possível inserir uma nova atividade."}
            ),
            status=500,
        )
    else:
        return Response(
            response=json.dumps(
                {
                    "id": resultado.id,
                    "nome": resultado.nome,
                    "pessoa_id": resultado.pessoa_id,
                }
            ),
            status=201,
        )
