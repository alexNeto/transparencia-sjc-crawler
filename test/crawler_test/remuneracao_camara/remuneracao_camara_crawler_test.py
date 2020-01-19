import unittest

from transparencia_api.commons.date_utils import month_year
from transparencia_api.crawler.remuneracao_camara.remuneracao_camara_crawler import RemuneracaoCamaraCrawler


class CargoStorageTest(unittest.TestCase):
    def setUp(self):
        self.__remuneracao_camara_crawler = RemuneracaoCamaraCrawler()

    def testa_se_raspa_dados(self):
        self.__remuneracao_camara_crawler.make_request(month_year())
        self.assertTrue(self.__remuneracao_camara_crawler.get_data() is not None)

    def testa_se_raspa_data(self):
        self.__remuneracao_camara_crawler.make_request(month_year())
        self.assertTrue(self.__remuneracao_camara_crawler.get_date() is not None)
