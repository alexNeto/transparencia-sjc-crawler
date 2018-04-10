from flask import Flask
from flask_restful import Resource, Api

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_model import RemuneracaoCamaraModel

app = Flask(__name__)
api = Api(app)


class RemuneracaoCamaraCotroller(Resource):

    def __init__(self):
        self.remuneracao_camara_municial = RemuneracaoCamaraModel()

    def get(self):
        return self.remuneracao_camara_municial.split_data_set()
