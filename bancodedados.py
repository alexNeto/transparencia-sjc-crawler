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
            if key == "0":
                continue
            if data[key]["Cargo"] not in cargos:
                cargos.append(data[key]["Cargo"])
        
        return cargos

    def salario_base(self, nome_cargo):
        
    def plano_carreira(self, nome_caro):
        
    def gratificacao(self, nome_cargo):
        
    def beneficios(self, nome_cargo):
        
    def abono(self, nome_cargo):
        
    def adiantamento_salarial(self, nome_cargo):
        
    def ferias(self, nome_cargo):
        
    def decimo_terceiro(self, nome_cargo):
        
    def abatimento(self, nome_cargo):
        
    def descontos(self, nome_cargo):
    
    def salario_bruto(self, nome_cargo):
    
    def salario_liquido(self, nome_cargo):
        
    def paga_salario(self, nome_cargo):
        """
        returna dados do salario de acordo com o cargo 
        desejado
        """
         with open(self.nome_arquivo()) as data_file:  
            data = json.load(data_file)
        salario = []


