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
        
    def dados(self):
        coluna = []
        for salario in self.linhas():
            linha = []
            for cargo in self.banco.separa_cargos():
                linha.append(self.banco.pega_salario(cargo, salario))
            coluna.append(linha)
        return coluna
        #print(len(coluna))
        #print(len(self.banco.separa_cargos()))
        #print(len(self.linhas()))
    
    def plota(self):
        """
        Método para plotar o gráfico de acordo com os dados coletados
        """
        data = self.dados()
        columns = self.banco.separa_cargos()
        rows =  self.linhas()

        values = np.arange(0, 1000, 100)
        value_increment = 100

        # Get some pastel shades for the colors
        colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
        n_rows = len(data)

        index = np.arange(len(columns)) + 0.3
        bar_width = 0.4

        # Initialize the vertical-offset for the stacked bar chart.
        y_offset = np.zeros(len(columns))

        # Plot bars and create text labels for the table
        cell_text = []
        for row in range(n_rows):
            plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
            y_offset = y_offset + data[row]
            cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
        # Reverse colors and text labels to display the last value at the top.
        colors = colors[::-1]
        cell_text.reverse()

        # Add a table at the bottom of the axes
        the_table = plt.table(cellText=cell_text,
                              rowLabels=rows,
                              rowColours=colors,
                              colLabels=columns,
                              loc='bottom')

        # Adjust layout to make room for the table:
        plt.subplots_adjust(left=0.2, bottom=0.2)

        plt.ylabel("Loss in ${0}'s".format(value_increment))
        plt.yticks(values * value_increment, ['%d' % val for val in values])
        plt.xticks([])
        plt.title('Loss by Disaster')

        plt.show()
