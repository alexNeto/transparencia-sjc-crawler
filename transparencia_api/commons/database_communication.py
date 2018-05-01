from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from transparencia_api.commons.database_defenition import SalarioCamaraMunicipalTable, CargoTable, DateTable, \
    FuncionarioPublicoTable


class DatabaseCommunication:
    def __init__(self):
        #############################################
        # Sobre o banco #############################
        #############################################
        self.__user = "transparencia"
        self.__password = "postgres123"
        self.__database = "transparencia_development"
        self.__host = "localhost"
        self.__port = 5432
        #############################################
        self.__connection = None
        # self.__meta = None
        self.__url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
        self.__Session = None
        self.__session = None
        self.__base = None

    def connect(self):
        self.__define_data_base()

    def __define_data_base(self):
        self.__url = self.__url.format(self.__user, self.__password, self.__host, self.__port, self.__database)
        self.__connection = create_engine(self.__url)

    @property
    def connection(self):
        return self.__connection


db = DatabaseCommunication()
db.connect()

base = declarative_base()


def get_base():
    return base


salario_camara_municipal_table = SalarioCamaraMunicipalTable
cargo_table = CargoTable
date_table = DateTable
funcionario_publico_table = FuncionarioPublicoTable

Session = sessionmaker(db.connection)
session = Session()

base.metadata.create_all(db.connection)
