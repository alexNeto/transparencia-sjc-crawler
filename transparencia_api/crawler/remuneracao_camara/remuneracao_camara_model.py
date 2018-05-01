from transparencia_api.cargo.repository.cargo_repository import CargoRepository
from transparencia_api.cargo.repository.cargo_storage import CargoStorage
from transparencia_api.commons.number_utils import to_float
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler
from transparencia_api.funcionario_publico.repository.funcionario_publico_repository import FucionarioPublicoRepository
from transparencia_api.funcionario_publico.repository.funcionario_publico_sotage import FuncionarioPublicoStorage
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_repository import \
    SalarioCamaraMunicipalRepository
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_storage import \
    SalarioCamaraMunicipalStorage


class RemuneracaoCamaraModel:
    def __init__(self):
        self.__data_set = RemuneracaoCamaraCrawler()
        # Cargo
        self.__cargo = CargoRepository()
        self.__cargo_storage = CargoStorage()
        # Salario e data
        self.__salario_camara_municipal = SalarioCamaraMunicipalRepository()
        self.__salario_camara_municipal_storage = SalarioCamaraMunicipalStorage()
        # Funcionario
        self.__funcionario_publico = FucionarioPublicoRepository()
        self.__funcionario_publico_storage = FuncionarioPublicoStorage()
        self.__date = None
        self.__data = None

    def split_data_set(self):
        splited_data = self.__data_set.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))
        self.__data = dados_individuais
        return "done"

    def set_date(self):
        self.__date = self.__data_set.get_date()
        return "done"

    def set_cargo(self, data):
        self.__cargo.cargo = data[1]
        return "done"

    def set_salario_camara_municipal(self, data):
        self.__salario_camara_municipal.salario_base = to_float(data[2])
        self.__salario_camara_municipal.plano_carreira = to_float(data[3])
        self.__salario_camara_municipal.gratificacoes = to_float(data[4])
        self.__salario_camara_municipal.beneficios = to_float(data[5])
        self.__salario_camara_municipal.abono = to_float(data[6])
        self.__salario_camara_municipal.adiantamento_salarial = to_float(data[7])
        self.__salario_camara_municipal.ferias = to_float(data[8])
        self.__salario_camara_municipal.decimo_terceiro = to_float(data[9])
        self.__salario_camara_municipal.abatimento_de_teto = to_float(data[10])
        self.__salario_camara_municipal.descontos = to_float(data[11])
        self.__salario_camara_municipal.salario_bruto = to_float(data[12])
        self.__salario_camara_municipal.salario_liquido = to_float(data[13])
        return "done"

    def set_funcionario_publico(self, data, ids):
        self.__funcionario_publico.date_id = ids[0]
        self.__funcionario_publico.cargo_id = ids[1]
        self.__funcionario_publico.dado_salario_id = ids[2]
        self.__funcionario_publico.nome = data[0]
        return "done"

    def update_database(self):
        self.split_data_set()
        self.set_date()
        for item in self.__data:
            self.set_salario_camara_municipal(item)
            dado_salario_id = self.__salario_camara_municipal_storage.create_dados_remuneracao(
                self.__salario_camara_municipal)
            self.set_cargo(item)
            cargo_id = self.__cargo_storage.create_dados_cargos(self.__cargo)
            date_id = self.__salario_camara_municipal_storage.create_date(self.__date)
            self.set_funcionario_publico(item, [date_id, cargo_id, dado_salario_id])
            self.__funcionario_publico_storage.create_dados_funcionario(self.__funcionario_publico)
        return self.__data
