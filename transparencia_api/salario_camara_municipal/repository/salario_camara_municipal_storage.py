from sqlalchemy import inspect, select

from transparencia_api.commons.database_communication import DatabaseCommunication, SalarioCamaraMunicipalTable, \
    DateTable, session


class SalarioCamaraMunicipalStorage:
    def __init__(self):
        self.__db = DatabaseCommunication()
        self.__db.connect()
        self.__date_table = DateTable

    def create_dados_remuneracao(self, remuneracao_field):
        session.add(remuneracao_field)
        session.commit()
        return "done"

    def retrieve_dados_remuneracao(self):
        s = select([SalarioCamaraMunicipalTable])
        results = self.__db.connection.execute(s)
        for result in results:
            print(result)
        return None

    # Date
    def create_date(self, date):
        session.add(date)
        session.commit()
        return "done"

    def retrieve_dados_date(self):
        select_statement = self.__date_table.select()
        return self.__db.connection.execute(select_statement)
