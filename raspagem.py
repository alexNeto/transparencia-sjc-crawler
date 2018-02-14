from urllib import urlopen
from bs4 import BeautifulSoup

from titulos import *


class Raspagem:
    def __init__(self):
        self.html = urlopen(
            "http://portal.camarasjc.sp.gov.br:8080/"
            "cmsjc/websis/portal_transparencia/financeiro/contas_publicas/"
            "index.php?consulta=../lei_acesso/lai_remuneracoes")
        self.bsObj = BeautifulSoup(self.html, "html.parser")
        self.nameList = self.bsObj.findAll("tr")
        self.data = self.bsObj.find("h5")

    def raspatodos(self):
        dados = {}
        titulo = cabecalho()
        j = 0
        for name in self.nameList:
            individual = {}
            i = 0
            for n in name:
                if "" not in n:
                    try:
                        individual[titulo[i]] = n.getText()
                        i += 1
                    except IndexError:
                        i += 1
                        continue
            dados[j] = individual
            j += 1
        return dados

    def pegadata(self):
        data = self.data.getText()
        data = data[20:]
        return data