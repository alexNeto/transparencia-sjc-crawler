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

    def prepare_dto(self, data):
        return {
            "nome": data[0],
            "cargo": data[1],
            "salario_base": to_float(data[2]),
            "plano_carreira": to_float(data[3]),
            "gratificacao": to_float(data[4]),
            "beneficio": to_float(data[5]),
            "abono": to_float(data[6]),
            "adiantamento": to_float(data[7]),
            "ferias": to_float(data[8]),
            "decimo_terceiro": to_float(data[9]),
            "abatimento": to_float(data[10]),
            "descontos": to_float(data[11]),
            "salario_bruto": to_float(data[12]),
            "salario_liquido": to_float(data[13])
        }

    def get_data(self):
        self.split_data_set()
        data_tratada = []
        for item in self.__data:
            if item[1] not in self.__cargos:
                self.__cargos.append(item[1])
            data_tratada.append(self.prepare_dto(item))
        return data_tratada

    def get_cargos(self):
        return self.__cargos

    def get_dados_raspados(self):
        return {
            "date": self.get_date(),
            "cargos": self.get_cargos(),
            "funcionario": self.get_data()
        }
