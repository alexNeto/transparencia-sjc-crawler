import unittest

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_model import RemuneracaoCamaraModel
from transparencia_api.salario_camara_municipal.repository.salario_camara_municipal_repository import \
    SalarioCamaraMunicipalRepository


class NumberUnitTest(unittest.TestCase):
    def setUp(self):
        self.remuneracao_camera_model = RemuneracaoCamaraModel()
        self.data = [
            'ABEL YOSHINOBU TAIRA',
            'ANALISTA TEC.LEG-DESIGNER GRAFICO',
            "5021.76",
            "150.65",
            "1044.35",
            "374.00",
            "0.00",
            "0.00",
            "0.00",
            "0.00",
            "0.00",
            "2702.60",
            "6590.76",
            "3888.16"
        ]

    def testa_se_set_date_nao_lanca_excecao(self):
        self.assertEqual("done", self.remuneracao_camera_model.set_date())
        return "done"

    def testa_se_set_cargo_nao_lanca_excecao(self):
        self.assertEqual("done", self.remuneracao_camera_model.set_cargo(self.data))

    def testa_se_set_salario_camara_municipal_nao_lanca_excecao(self):
        self.assertEqual("done", self.remuneracao_camera_model.set_salario_camara_municipal(self.data))

    def testa_se_set_funcionario_publico_nao_lanca_excecao(self):
        self.assertEqual("done", self.remuneracao_camera_model.set_funcionario_publico(self.data, 1, 1, 1))
