from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Headers(Resource):
    def get(self, type):
        if type == 'salarystuff':
            return salary_stuff()
        elif type == 'role':
            return role()
        elif type == 'cityname':
            return city_name()

def salary_stuff():
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
    return {"salary_stuff": linhas}

def role():
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

def city_name():
    return "São José dos Campos"

