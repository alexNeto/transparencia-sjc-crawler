import numpy as np
import matplotlib.pyplot as plt

from bancodedados import Banco


class AppMan:
    """
    Classe para gerenciar todas as ações do programa
    """

    def __init__(self):
        self.banco = Banco()

    def atualiza_raspagem(self):
        """
        Atualiza o json criado pelo banco de dados
        """
        self.banco.raspatudo()

    def linhas(self):
        """
        Método contém os dados sobre o salário
        """
        linhas = ["Salário Base",
                "Plano de Carreira",
                "Gratificações",
                "Benefícios",
                "Abono",
                "Adiantamento Salarial",
                "Férias",
                "Décimo Terceiro",
                "Abatimento",
                "Descontos",
                "Salário Bruto",
                "Salário Líquido"]
        return linhas
        
    def menu(self):
        """
        Método para mostrar um menu de todos os cargos 
        """
        cargos = []
        for i, cargo in enumerate(self.banco.separa_cargos()):
            menu = "{0} - {1}\n".format(i + 1, cargo)
            cargos.append(menu)
        cargos.append("{0} - {1}\n".format(-1, "Sair"))
        return "".join(cargos)

    def dados(self, cargo):
        """
        Pega os dados salariais de determinado cargo
        """       
        coluna = []
        for salario in self.linhas():
            linha = []
            linha.append(self.banco.pega_salario(cargo, salario))
            coluna.append(linha)
        return coluna
        
    def plota(self, cargo):
        """
        Método para plotar o gráfico de acordo com os dados coletados
        """
        cargos = self.banco.separa_cargos()
        cargos = cargos[cargo]

        data = self.dados(cargos)
        columns = [cargos]
        rows = self.linhas()

        values = np.arange(0, 200, 100)
        value_increment = 100

        colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
        n_rows = len(data)

        index = np.arange(len(columns)) + 0.3
        bar_width = 0.4

        y_offset = np.zeros(len(columns))

        cell_text = []
        for row in range(n_rows):
            plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
            y_offset = y_offset + data[row]
            cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
        colors = colors[::-1]
        cell_text.reverse()

        the_table = plt.table(cellText=cell_text,
                              rowLabels=rows,
                              rowColours=colors,
                              colLabels=columns,
                              loc='bottom')

        plt.subplots_adjust(left=0.2, bottom=0.2)

        plt.ylabel("Loss in ${0}'s".format(value_increment))
        plt.yticks(values * value_increment, ['%d' % val for val in values])
        plt.xticks([])
        plt.title('Loss by Disaster')

        plt.show()
