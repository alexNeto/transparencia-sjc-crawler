import datetime
import unittest

from transparencia_api.commons.date_utils import converte_mes, month_year


class NumberUnitTest(unittest.TestCase):
    def test_converte_corretamente(self):
        self.assertEqual(1, converte_mes('Janeiro'))

    def test_converte_incorretamente(self):
        self.assertEqual(0, converte_mes("may"))

    def test_parse_date(self):
        self.assertEqual('12/2019', month_year('12-2019'))

    def test_get_last_month(self):
        now = datetime.datetime.now()
        now = int(f"{now.month}{now.year}")
        self.assertLess(now, int(month_year().replace('/', '')))
