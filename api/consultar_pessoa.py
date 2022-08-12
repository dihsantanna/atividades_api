import json
from flask import Response
from db.consultar_pessoas import consultar_pessoas as service


def consultar_pessoas(nome=None, id=None):
    resultado = service(nome=nome, id=id)
    if not resultado:
        return Response(
            response=json.dumps({"message": "Pessoa não encontrada"}), status=404
        )
    elif type(resultado) is list:
        return [
            {"id": pessoa.id, "nome": pessoa.nome, "idade": pessoa.idade}
            for pessoa in resultado
        ]
    else:
        return {
            "id": resultado.id,
            "nome": resultado.nome,
            "idade": resultado.idade,
        }
