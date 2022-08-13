import json
from flask import Response
from db.editar_atividade import editar_atividade as service


def editar_atividade(id=None):
    resultado = service(id=id)
    if not resultado:
        return Response(
            response=json.dumps({"message": "Atividade não existe"}), status=404
        )
    return {
        "id": resultado.id,
        "nome": resultado.nome,
        "pessoa_id": resultado.pessoa_id,
        "status": resultado.status,
    }
