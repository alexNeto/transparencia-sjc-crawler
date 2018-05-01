import unittest

from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler


class CargoStorageTest(unittest.TestCase):
    def setUp(self):
        self.__remuneracao_camara_crawler = RemuneracaoCamaraCrawler()

    def testa_se_raspa_dados(self):
        self.assertTrue(self.__remuneracao_camara_crawler.get_data() is not None)

    def testa_se_raspa_data(self):
        self.assertTrue(self.__remuneracao_camara_crawler.get_date() is not None)