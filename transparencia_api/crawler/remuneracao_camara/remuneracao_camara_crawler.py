from urllib.request import urlopen
from bs4 import BeautifulSoup


class RemuneracaoCamaraCrawler:
    def __init__(self):
        self.html = urlopen(
            "http://portal.camarasjc.sp.gov.br:8080/"
            "cmsjc/websis/portal_transparencia/financeiro/contas_publicas/"
            "index.php?consulta=../lei_acesso/lai_remuneracoes")
        self.target = BeautifulSoup(self.html, "html.parser")

    def get_data(self):
        return self.target.find("tbody").getText()

    def get_date(self):
        data = self.target.find("h5").getText()
        data = data[20:]
        return data
