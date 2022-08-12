from flask import Flask, request
from flask_restful import Resource, Api

from consultar_pessoa import consultar_pessoas
from inserir_pessoa import inserir_pessoa
from editar_pessoa import editar_pessoa
from deletar_pessoa import deletar_pessoa

app = Flask(__name__)
api = Api(app)


class Pessoas(Resource):
    def get(self):
        nome = request.args.get("nome", type=str)
        id = request.args.get("id", type=int)

        resultado = consultar_pessoas(nome=nome, id=id)
        return resultado

    def post(self):
        body = request.json
        resultado = inserir_pessoa(body=body)
        return resultado

    def put(self):
        nome = request.args.get("nome", type=str)
        id = request.args.get("id", type=int)
        body = request.json
        print(body)
        resultado = editar_pessoa(body=body, id=id, nome=nome)
        return resultado

    def delete(self, id):
        return deletar_pessoa(id=id)


api.add_resource(Pessoas, "/pessoas//<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
