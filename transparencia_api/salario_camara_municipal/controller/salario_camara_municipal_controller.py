from flask import Flask
from flask_restful import Resource, Api

from transparencia_api.salario_camara_municipal.model.salario_camara_municipal_model import SalarioCamaraMunicipalModel

app = Flask(__name__)
api = Api(app)


class SalarioCamaraMunicipalController(Resource):

    def __init__(self):
        self.salario_camara_municipal = SalarioCamaraMunicipalModel()

    def get(self):
        return self.salario_camara_municipal.get_data()

