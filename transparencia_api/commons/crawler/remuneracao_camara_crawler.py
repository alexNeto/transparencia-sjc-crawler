from urllib.request import urlopen
from bs4 import BeautifulSoup


class RemuneracaoCamaraCrawler:
    def __init__(self):
        self.html = urlopen(
            "http://portal.camarasjc.sp.gov.br:8080/"
            "cmsjc/websis/portal_transparencia/financeiro/contas_publicas/"
            "index.php?consulta=../lei_acesso/lai_remuneracoes")
        self.target = BeautifulSoup(self.html, "html.parser")

    # def raspatodos(self):
    #     dados = {}
    #     titulo = cabecalho()
    #     j = 0
    #     for name in self.nameList:
    #         individual = {}
    #         i = 0
    #         for n in name:
    #             if "" not in n:
    #                 try:
    #                     individual[titulo[i]] = n.getText()
    #                     i += 1
    #                 except IndexError:
    #                     i += 1
    #                     continue
    #         dados[j] = individual
    #         j += 1
    #     return dados

    def get_data(self):
        return self.target.find("tbody").getText()

    def get_date(self):
        data = self.target.find("h5").getText()
        data = data[20:]
        return data