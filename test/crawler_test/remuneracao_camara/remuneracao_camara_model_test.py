import types
import unittest

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_model import RemuneracaoCamaraModel


class RemuneracaoCamaraModelTest(unittest.TestCase):
    def setUp(self):
        self.remuneracaoModel = RemuneracaoCamaraModel()
        self.dado = ["ABEL YOSHINOBU TAIRA", "ANALISTA TEC.LEG-DESIGNER GRAFICO", "5.021,76", "150,65", "1.044.35",
                     "0.00", "0.00", "0.00", "0.00", "0,00", "2.702,60", "6.590,76", "3.888,16", "0.00"]

    def testa_se_separa_dados_raspados(self):
        self.assertTrue(self.remuneracaoModel.split_data_set().__len__() > 100)

    def testa_se_raspa_data(self):
        data_seprada = self.remuneracaoModel.get_date()
        self.assertEqual(2, data_seprada.__len__())

    def testa_se_converte_de_string_para_float(self):
        print(self.remuneracaoModel.prepare_dto(self.dado))
        self.assertEqual(0.00, self.remuneracaoModel.prepare_dto(self.dado)["ferias"])

    def testa_se_pega_e_converte_dados_raspados(self):
        self.assertTrue(isinstance(self.remuneracaoModel.get_data(), list))

    def testa_se_returna_formato_correto(self):
        dados = self.remuneracaoModel.get_dados_raspados()
        date = dados["date"]
        cargos = dados["cargos"]
        funcionarios = dados["funcionario"]
        self.assertTrue(date and cargos and funcionarios)
