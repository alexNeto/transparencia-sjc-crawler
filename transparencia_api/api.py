from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_controller import RemuneracaoCamaraCotroller


class App:
    def __init__(self):
        self.__app = Flask(__name__)
        self.__api = Api(self.__app)

    @property
    def app(self):
        return self.__app

    @property
    def api(self):
        return self.__api


class Index(Resource):
    @classmethod
    def get(cls):
        return {"date": {"mes": 1,
                         "ano": 2018
                         },
                "cargos": ["a", "b", "c"],
                "funcionario": [{
                    "nome": 'ABEL YOSHINOBU TAIRA',
                    "cargo": 'ANALISTA TEC.LEG-DESIGNER GRAFICO',
                    "salario_base": 5021.76,
                    "plano_carreira": 150.65,
                    "gratificacao": 1044.35,
                    "beneficio": 374.00,
                    "abono": 0.00,
                    "adiantamento": 0.00,
                    "ferias": 0.00,
                    "decimo_terceiro": 0.00,
                    "abatimento": 0.00,
                    "descontos": 2702.60,
                    "salario_bruto": 6590.76,
                    "salario_liquido": 3888.16
                }]
                }


app_instance = App()

app = app_instance.app
api = app_instance.api
CORS(app)

# root
api.add_resource(Index, '/')

# salario camara municipal
api.add_resource(RemuneracaoCamaraCotroller, '/salario_camara_municipal', '/salario_camara_municipal/<string:date>')

if __name__ == '__main__':
    app.run(debug=True)
