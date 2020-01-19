from flask import Flask
from flask_restful import Resource, Api

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_model import RemuneracaoCamaraModel

app = Flask(__name__)
api = Api(app)


class RemuneracaoCamaraCotroller(Resource):

    def __init__(self):
        self.remuneracao_camara_municial = RemuneracaoCamaraModel()

    def get(self, date=None):
        return self.remuneracao_camara_municial.get_dados_raspados(date)
