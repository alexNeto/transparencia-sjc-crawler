import unittest

from transparencia_api.commons.date_utils import converte_mes


class NumberUnitTest(unittest.TestCase):
    def converte_corretamente(self):
        self.assertTrue(1, converte_mes('Janeiro'))

    def converte_incorretamente(self):
        self.assertTrue(0, converte_mes("may"))
