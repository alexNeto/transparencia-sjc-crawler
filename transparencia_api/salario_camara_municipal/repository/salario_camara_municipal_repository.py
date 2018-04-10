class SalarioCamaraMunicipalRepository:

    def __init__(self):
        self.__salario_base = None
        self.__plano_carreira = None
        self.__gratificacoes = None
        self.__beneficios = None
        self.__abono = None
        self.__adiantamento_salarial = None
        self.__ferias = None
        self.__decimo_terceiro = None
        self.__abatimento_de_teto = None
        self.__descontos = None
        self.__salario_bruto = None
        self.__salario_liquido = None

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, value):
        self.__salario_base = value

    @property
    def plano_carreira(self):
        return self.__plano_carreira

    @plano_carreira.setter
    def plano_carreira(self, value):
        self.__plano_carreira = value

    @property
    def gratificacoes(self):
        return self.__gratificacoes

    @gratificacoes.setter
    def gratificacoes(self, value):
        self.__gratificacoes = value

    @property
    def beneficios(self):
        return self.__beneficios

    @beneficios.setter
    def beneficios(self, value):
        self.__beneficios = value

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, value):
        self.__abono = value

    @property
    def adiantamento_salarial(self):
        return self.__adiantamento_salarial

    @adiantamento_salarial.setter
    def adiantamento_salarial(self, value):
        self.__adiantamento_salarial = value

    @property
    def ferias(self):
        return self.__ferias

    @ferias.setter
    def ferias(self, value):
        self.__ferias = value

    @property
    def decimo_terceiro(self):
        return self.__decimo_terceiro

    @decimo_terceiro.setter
    def decimo_terceiro(self, value):
        self.__decimo_terceiro = value

    @property
    def abatimento_de_teto(self):
        return self.__abatimento_de_teto

    @abatimento_de_teto.setter
    def abatimento_de_teto(self, value):
        self.__abatimento_de_teto = value

    @property
    def descontos(self):
        return self.__descontos

    @descontos.setter
    def descontos(self, value):
        self.__descontos = value

    @property
    def salario_bruto(self):
        return self.__salario_bruto

    @salario_bruto.setter
    def salario_bruto(self, value):
        self.__salario_bruto = value

    @property
    def salario_liquido(self):
        return self.__salario_liquido

    @salario_liquido.setter
    def salario_liquido(self, value):
        self.__salario_liquido = value
