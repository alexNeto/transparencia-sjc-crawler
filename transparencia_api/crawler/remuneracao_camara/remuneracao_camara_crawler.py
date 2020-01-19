import requests
from bs4 import BeautifulSoup


class RemuneracaoCamaraCrawler:

    def __init__(self):
        self.target = ""

    def get_data(self):
        return self.target.find("tbody").getText()

    def get_date(self):
        data = self.target.find("h5").getText()
        data = data[20:]
        return data

    def make_request(self, date):
        response = requests.post(
            "http://portal.camarasjc.sp.gov.br:8080"
            "/cmsjc/websis/portal_transparencia/financeiro/contas_publicas/"
            "index.php?consulta=../lei_acesso/lai_remuneracoes",
            data={'competencia': date})

        self.target = BeautifulSoup(response.text, "html.parser")
