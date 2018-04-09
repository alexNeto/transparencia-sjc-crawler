from sqlalchemy import Table, Column, Integer, String, ForeignKey, Sequence
from transparencia_api.commons.database_communication import DatabaseCommunication


class FucionarioPublicoRepository:

    def __init__(self):
        self.__cargo_id = None
        self.__dado_salario_id = None
        self.__date_id = None
        self.__nome = None

    @property
    def cargo_id(self):
        return self.__cargo_id

    @cargo_id.setter
    def cargo_id(self, value):
        self.__cargo_id = value

    @property
    def dado_salario_id(self):
        return self.__dado_salario_id

    @dado_salario_id.setter
    def dado_salario_id(self, value):
        self.__dado_salario_id = value

    @property
    def data_id(self):
        return self.data_id

    @data_id.setter
    def data_id(self, value):
        self.data_id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
