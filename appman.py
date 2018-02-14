
from bancodedados import Banco
from titulos import *


class AppMan:
    '''
    Classe para gerenciar todas as ações do programa
    '''

    def __init__(self):
        self.banco = Banco()

    def atualiza_raspagem(self):
        """
        Atualiza o json criado pelo banco de dados
        """
        self.banco.raspatudo()

    def menu(self):
        '''
        Método para mostrar um menu de todos os cargos 
        '''
        cargos = []
        for i, cargo in enumerate(self.banco.separa_cargos()):
            menu = "{0} - {1}\n".format(i + 1, cargo)
            cargos.append(menu)
        cargos.append("{0} - {1}\n".format(-1, "Sair"))
        return "".join(cargos)

    def dados(self, cargo):
        '''
        Pega os dados salariais de determinado cargo
        '''
        coluna = []
        for salario in linhas():
            linha = []
            linha.append(self.banco.pega_salario(cargo, salario))
            coluna.append(linha)
        return coluna
