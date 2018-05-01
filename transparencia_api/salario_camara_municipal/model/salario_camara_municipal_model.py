from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_model import RemuneracaoCamaraModel
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_storage import \
    SalarioCamaraMunicipalStorage


class SalarioCamaraMunicipalModel:

    def __init__(self):
        self.__data = RemuneracaoCamaraCrawler()
        self.__remuneracao_camara_model = RemuneracaoCamaraModel()
        self.__salario_camara_municipal_storage = SalarioCamaraMunicipalStorage()

    def get_date(self):
        return {'data': self.data.get_date()}

    def get_data(self):
        dados_remuneracao = self.__salario_camara_municipal_storage.retrieve_dados_remuneracao()
        if dados_remuneracao is None:
            dados_remuneracao = self.__remuneracao_camara_model.update_database()
        return dados_remuneracao
