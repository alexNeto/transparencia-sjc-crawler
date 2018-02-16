from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Titulos(Resource):
    def post(self):
        return "titulos"




def linhas():
    linhas = ["Salário Base",
              "Plano de Carreira",
              "Gratificações",
              "Benefícios",
              "Abono",
              "Adiantamento Salarial",
              "Férias",
              "Décimo Terceiro",
              "Abatimento",
              "Descontos",
              "Salário Bruto",
              "Salário Líquido"]
    return linhas


def cabecalho():
    titulo = ["Nome do Servidor",
              "Cargo",
              "Salário Base",
              "Plano de Carreira",
              "Gratificações",
              "Benefícios",
              "Abono",
              "Adiantamento Salarial",
              "Férias",
              "Décimo Terceiro",
              "Abatimento",
              "Descontos",
              "Salário Bruto",
              "Salário Líquido"]
    return titulo


