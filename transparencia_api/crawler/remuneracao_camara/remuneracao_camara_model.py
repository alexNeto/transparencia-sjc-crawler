from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_database_updater import \
    RemuneracaoCamaraDatabaseUpdater
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler
from transparencia_api.cargo.repository.cargo_repository import CargoRepository
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_repository import \
    SalarioCamaraMunicipalRepository
from transparencia_api.funcionario_publico.repository.funcionario_publico_repository import FucionarioPublicoRepository


class RemuneracaoCamaraModel:

    def __init__(self):
        self.__crawler_bd = RemuneracaoCamaraDatabaseUpdater()
        self.__data_set = RemuneracaoCamaraCrawler()
        self.__cargo = CargoRepository()
        self.__salario_camara_municipal = SalarioCamaraMunicipalRepository()
        self.__funcionario_publico = FucionarioPublicoRepository()
        self.__date = None
        self.__data = None

    def split_data_set(self):
        splited_data = self.__data_set.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))
        self.__data = dados_individuais

    def set_date(self):
        self.__date = self.__data_set.get_date()

    def set_cargo(self, data):
        self.__cargo.cargo = data[1]

    def set_salario_camara_municipal(self, data):
        self.__salario_camara_municipal.salario_liquido = data[2]
        self.__salario_camara_municipal.salario_base = data[3]
        self.__salario_camara_municipal.abono = data[4]
        self.__salario_camara_municipal.beneficios = data[5]
        self.__salario_camara_municipal.gratificacoes = data[6]
        self.__salario_camara_municipal.plano_carreira = data[7]
        self.__salario_camara_municipal.abatimento_de_teto = data[8]
        self.__salario_camara_municipal.adiantamento_salarial = data[9]
        self.__salario_camara_municipal.decimo_terceiro = data[10]
        self.__salario_camara_municipal.descontos = data[11]
        self.__salario_camara_municipal.ferias = data[12]
        self.__salario_camara_municipal.salario_bruto = data[13]

    def set_funcionario_publico(self, data, date_id, cargo_id, dado_salario_id):
        self.__funcionario_publico.date_id = date_id
        self.__funcionario_publico.cargo_id = cargo_id
        self.__funcionario_publico.dado_salario_id = dado_salario_id
        self.__funcionario_publico.nome = data[0]

    def update_database(self):
        self.split_data_set()
        self.set_date()
        for item in self.__data:
            self.set_salario_camara_municipal(item)
            dado_salario_id = self.__crawler_bd.create_dados_remuneracao(self.__salario_camara_municipal)
            self.set_cargo(item)
            cargo_id = self.__crawler_bd.create_dados_cargos(self.cargo)
            date_id = self.__crawler_bd.create_date(self.__date)
            self.set_funcionario_publico(item, date_id, cargo_id, dado_salario_id)
            self.__crawler_bd.create_dados_funcionario(self.__funcionario_publico)
        return self.__data
