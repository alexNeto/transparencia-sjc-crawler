import json

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
        valor = []
        data = self.acessa_json()
        for key in data:
            if key == "0":
                continue
            if data[key]["Cargo"] not in valor:
                valor.append(data[key]["Cargo"]) 
        return valor
        
    def acessa_json(self):
        """
        Método opara acessar o json salvo
        """
        with open(self.nome_arquivo()) as data_file:  
            data = json.load(data_file)

        return data

    def pega_salario(self, nome_cargo, tipo_salario):
        """
        Método para pegar o salario de determinado cargo e 
        formatá-lo para float
        retorna a média deles
        """
        acomulador_salario = 0
        contador_salario = 0
        data = self.acessa_json()
        for key in data:
            if key == "0":
                continue
            if data[key]["Cargo"] == nome_cargo:
                salario = data[key][tipo_salario]
                salario = salario.replace(".", "")
                salario = salario.replace(",", ".")
                acomulador_salario += float(salario)
                contador_salario += 1
        if contador_salario == 0:
            return 0
        else:
            return acomulador_salario / contador_salario * 100
     
        
        
        
