from flask import Flask
from flask_restful import Resource, Api

from transparencia_api.commons.database_communication import DatabaseCommunication
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_controller import RemuneracaoCamaraCotroller
from transparencia_api.salario_camara_municipal.controller.salario_camara_municipal_controller import \
    SalarioCamaraMunicipalController

app = Flask(__name__)
api = Api(app)
db = DatabaseCommunication().connect()


class Index(Resource):
    @classmethod
    def get(cls):
        return ""


# root
api.add_resource(Index, '/')

# salario camara municipal
api.add_resource(SalarioCamaraMunicipalController, '/salario_camara_municipal')


###########################
# Tarefas administrativas #
###########################
api.add_resource(RemuneracaoCamaraCotroller, '/update/data/base/remuneracao/camara/municipal')

if __name__ == '__main__':
    app.run(debug=True)
