from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_database_updater import \
    RemuneracaoCamaraDatabaseUpdater
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler
from transparencia_api.cargo.repository.cargo_repository import CargoRepository
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_repository import \
    SalarioCamaraMunicipalRepository
from transparencia_api.funcionario_publico.repository.funcionario_publico_repository import FucionarioPublicoRepository


class RemuneracaoCamaraModel:

    def __init__(self):
        self.crawler_bd = RemuneracaoCamaraDatabaseUpdater()
        self.data_set = RemuneracaoCamaraCrawler()
        self.cargo = CargoRepository()
        self.salario_camara_municipal = SalarioCamaraMunicipalRepository()
        self.funcionario_publico = FucionarioPublicoRepository()
        self.date = None
        self.data = None

    def split_data_set(self):
        splited_data = self.data_set.get_data().strip(' ').strip('\n').split('\n\n\n')
        dados_individuais = []
        for individuo in splited_data:
            dados_individuais.append(individuo.split('\n'))
        self.data = dados_individuais

    def set_data(self):
        self.date = self.data_set.get_date()

    def set_cargo(self, data):
        self.cargo.cargo = data[1]

    def set_salario_camara_municipal(self, data):
        self.salario_camara_municipal.salario_liquido = data[2]
        self.salario_camara_municipal.salario_base = data[3]
        self.salario_camara_municipal.abono = data[4]
        self.salario_camara_municipal.beneficios = data[5]
        self.salario_camara_municipal.gratificacoes = data[6]
        self.salario_camara_municipal.plano_carreira = data[7]
        self.salario_camara_municipal.abatimento_de_teto = data[8]
        self.salario_camara_municipal.adiantamento_salarial = data[9]
        self.salario_camara_municipal.decimo_terceiro = data[10]
        self.salario_camara_municipal.descontos = data[11]
        self.salario_camara_municipal.ferias = data[12]
        self.salario_camara_municipal.salario_bruto = data[13]

    def set_funcionario_publico(self, data, date_id, cargo_id, dado_salario_id):
        self.funcionario_publico.date_id = date_id
        self.funcionario_publico.cargo_id = cargo_id
        self.funcionario_publico.dado_salario_id = dado_salario_id
        self.funcionario_publico.nome = data[0]

    def update_database(self):
        for item in self.data:
            self.set_salario_camara_municipal(item)
            remuneracao_id = self.crawler_bd.create_dados_remuneracao(self.salario_camara_municipal)
            self.set_cargo(item)
            cargo_id = self.crawler_bd.create_dados_cargos(self.cargo)

