import json
from flask import Response
from db.consultar_atividades import consultar_atividades as service


def consultar_atividades(id=None, pessoa_id=None):
    resultado = service(id=id, pessoa_id=pessoa_id)
    if not resultado:
        return Response(
            response=json.dumps({"message": "Atividade não encontrada"}), status=404
        )
    elif type(resultado) is list:
        return [
            {
                "id": atividade.id,
                "nome": atividade.nome,
                "pessoa_id": atividade.pessoa_id,
                "status": atividade.status,
            }
            for atividade in resultado
        ]
    else:
        return {
            "id": resultado.id,
            "nome": resultado.nome,
            "pessoa_id": resultado.pessoa_id,
            "status": resultado.status,
        }
