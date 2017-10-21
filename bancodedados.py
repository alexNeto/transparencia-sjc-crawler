import json

from pprint import pprint
from raspagem import Raspagem


class Banco:
    """
    Classe para gerenciar os dados raspados
    """
    def __init__(self):
        self.raspagem = Raspagem()
        self.data = ""

    def dataDeLeitura(self):
        """
        Pega a data em que os dados foram atualizados
        """
        self.data = self.raspagem.pegadata()
        self.data = self.data.split(" de ")
        self.data = "".join(self.data)
        self.data = self.data.lower()
        return self.data

    def nome_arquivo(self):
        """
        metodo para nomear o json de acordo com a data
        da raspagem
        """
        return "%s.json" % (self.dataDeLeitura())
 
    def raspatudo(self):
        """ 
        Inicialmente os dados raspados serão salvos em um 
        arquivo json, para facilitar futuras consultas
        """
        with open(self.nome_arquivo(), 'w') as outfile:
            json.dump(self.raspagem.raspatodos(), outfile)
    
    def separa_cargos(self):
        """
        Separa todos os cargos registrado na prefeitura
        """
        with open(self.nome_arquivo()) as data_file:  
            data = json.load(data_file)
        cargos = []
        for key in data:
            if data[key]["Cargo"] not in cargos:
                cargos.append(data[key]["Cargo"])
        
        print(cargos)

