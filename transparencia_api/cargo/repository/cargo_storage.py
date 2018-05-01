from transparencia_api.commons.database_communication import DatabaseCommunication, CargoTable, session


class CargoStorage:
    def __init__(self):
        self.__db = DatabaseCommunication()
        self.__db.connect()
        self.__cargo_table = CargoTable

    def create_dados_cargos(self, cargo_field):
        session.add(cargo_field)
        session.commit()

    def retrieve_dados_cargos(self):
        select_statement = self.__cargo_table.select()
        return self.__db.connection.execute(select_statement)
