from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from consultar_pessoa import consultar_pessoas

app = Flask(__name__)
api = Api(app)


class Pessoas(Resource):
    def get(self):
        nome = request.args.get("nome", type=str)
        id = request.args.get("id", type=int)

        resultado = consultar_pessoas(nome=nome, id=id)
        return resultado


api.add_resource(Pessoas, "/pessoas/")

if __name__ == "__main__":
    app.run(debug=True)
