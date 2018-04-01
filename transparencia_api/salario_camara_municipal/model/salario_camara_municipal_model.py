from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler


class SalarioCamaraMunicipalModel:

    def __init__(self):
        self.data = RemuneracaoCamaraCrawler()

    def get_date(self):
        return {'data': self.data.get_date()}

    def get_data(self):
        splited_data = self.data.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))

        return {'info': dados_individuais}
