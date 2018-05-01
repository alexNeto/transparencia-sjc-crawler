from transparencia_api.commons.number_utils import to_float
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler


class RemuneracaoCamaraModel:
    def __init__(self):
        self.__data_set = RemuneracaoCamaraCrawler()
        self.__date = None
        self.__data = None

    def split_data_set(self):
        splited_data = self.__data_set.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))
        self.__data = dados_individuais
        return "done"

    def get_date(self):
        return self.__data_set.get_date()

    def convert_string_to_float(self, data):
        data[2] = to_float(data[2])
        data[3] = to_float(data[3])
        data[4] = to_float(data[4])
        data[5] = to_float(data[5])
        data[6] = to_float(data[6])
        data[7] = to_float(data[7])
        data[8] = to_float(data[8])
        data[9] = to_float(data[9])
        data[10] = to_float(data[10])
        data[11] = to_float(data[11])
        data[12] = to_float(data[12])
        data[13] = to_float(data[13])
        return data

    def get_data(self):
        self.split_data_set()
        dataTratada = []
        for item in self.__data:
            dataTratada.append(self.convert_string_to_float(item))
        return dataTratada

    def get_dados_raspados(self):
        return {
            "date": self.get_date(),
            "info": self.get_data()
        }
