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
        self.banco.separa_cargos()

