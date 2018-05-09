import unittest

from transparencia_api.commons import number_utils


class NumberUnitTest(unittest.TestCase):
    def testa_se_converte_para_float(self):
        self.assertEqual(1000.50, number_utils.to_float("1.000,50"))

    def testa_se_converte_string_com_numeros(self):
        self.assertEqual(1000.0, number_utils.to_float("1000"))
