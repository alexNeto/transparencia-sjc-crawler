from flask import Flask
from flask_restful import Resource, Api
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_controller import RemuneracaoCamaraCotroller
from transparencia_api.salario_camara_municipal.controller.salario_camara_municipal_controller import \
    SalarioCamaraMunicipalController


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
        return ""


app_instance = App()

app = app_instance.app
api = app_instance.api

# root
api.add_resource(Index, '/')

# salario camara municipal
api.add_resource(SalarioCamaraMunicipalController, '/salario_camara_municipal')

###########################
# Tarefas administrativas #
###########################
api.add_resource(RemuneracaoCamaraCotroller, '/update/data_base/remuneracao/camara_municipal')

if __name__ == '__main__':
    app.run(debug=True)
