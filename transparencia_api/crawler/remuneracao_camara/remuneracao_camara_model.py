from transparencia_api.commons.number_utils import to_float
from transparencia_api.commons.date_utils import converte_mes
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler


class RemuneracaoCamaraModel:
    def __init__(self):
        self.__data_set = RemuneracaoCamaraCrawler()
        self.__date = None
        self.__data = None
        self.__cargos = []

    def split_data_set(self):
        splited_data = self.__data_set.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))
        self.__data = dados_individuais
        return dados_individuais

    def get_date(self):
        data_separada = self.__data_set.get_date().split(" ")
        return {
            "mes": converte_mes(data_separada[0]),
            "ano": int(data_separada[2])
        }

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
        data_tratada = []
        for item in self.__data:
            if item[1] not in self.__cargos:
                self.__cargos.append(item[1])
            data_tratada.append(self.convert_string_to_float(item))
        return data_tratada

    def get_cargos(self):
        return self.__cargos

    def get_dados_raspados(self):
        return {
            "date": self.get_date(),
            "cargos": self.get_cargos(),
            "funcionario": self.get_data()
        }
