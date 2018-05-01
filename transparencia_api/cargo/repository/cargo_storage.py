from transparencia_api.commons.database_communication import DatabaseCommunication
from transparencia_api.commons.database_defenition import CargoTable


class CargoStorage:
    def __init__(self):
        self.__db = DatabaseCommunication()
        self.__db.connect()
        self.__cargo_table = CargoTable

    def create_dados_cargos(self, cargo_field):
        cargo_clause = self.__cargo_table \
            .insert().values(cargo=cargo_field.cargo)
        result = self.__db.connection.execute(cargo_clause)
        return result.inserted_primary_key
