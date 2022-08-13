from flask import Flask, request
from flask_restful import Resource, Api

from consultar_pessoa import consultar_pessoas
from inserir_pessoa import inserir_pessoa
from editar_pessoa import editar_pessoa
from deletar_pessoa import deletar_pessoa

from consultar_atividade import consultar_atividades
from inserir_atividade import inserir_atividade
from editar_atividade import editar_atividade

app = Flask(__name__)
api = Api(app)


class Pessoas(Resource):
    def get(self):
        nome = request.args.get("nome", type=str)

        resultado = consultar_pessoas(nome=nome)
        return resultado

    def post(self):
        body = request.json
        resultado = inserir_pessoa(body=body)
        return resultado

    def put(self):
        nome = request.args.get("nome", type=str)
        body = request.json
        resultado = editar_pessoa(body=body, id=id, nome=nome)
        return resultado


class Pessoa(Resource):
    def get(self, id):
        resultado = consultar_pessoas(id=id)
        return resultado

    def put(self, id):
        body = request.json
        resultado = editar_pessoa(body=body, id=id)
        return resultado

    def delete(self, id):
        return deletar_pessoa(id=id)


class Atividades(Resource):
    def get(self):
        pessoaId = request.args.get("pessoaId", type=int)
        resultado = consultar_atividades(pessoa_id=pessoaId)
        return resultado


class Atividade(Resource):
    def get(self, id):
        resultado = consultar_atividades(id=id)
        return resultado

    def post(self, id):
        body = request.json
        resultado = inserir_atividade(body=body, pessoa_id=id)
        return resultado

    def put(self, id):
        resultado = editar_atividade(id=id)
        return resultado


api.add_resource(Pessoas, "/pessoas/")
api.add_resource(Pessoa, "/pessoas/<int:id>")
api.add_resource(Atividades, "/atividades/")
api.add_resource(Atividade, "/atividades/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
