from transparencia_api.commons.database_communication import DatabaseCommunication
from transparencia_api.commons.database_defenition import FuncionarioPublicoTable


class FuncionarioPublicoStorage:
    def __init__(self):
        self.__db = DatabaseCommunication()
        self.__db.connect()
        self.__funcionario_publico_table = FuncionarioPublicoTable

    def create_dados_funcionario(self, funcionario_field):
        funcionario_clause = self.__funcionario_publico_table \
            .insert().values(cargo_id=funcionario_field.cargo_id,
                             dado_salario_id=funcionario_field.dado_salario,
                             date_id=funcionario_field.data_id,
                             nome=funcionario_field.nome)
        result = self.__db.connection.execute(funcionario_clause)
        return result.inserted_primary_key
