from transparencia_api.commons.database_communication import DatabaseCommunication
from transparencia_api.commons.database_defenition import SalarioCamaraMunicipalTable, DateTable


class SalarioCamaraMunicipalStorage:
    def __init__(self):
        self.__db = DatabaseCommunication()
        self.__db.connect()
        self.salario_camara_municipal_table = SalarioCamaraMunicipalTable
        self.date_table = DateTable

    def create_dados_remuneracao(self, remuneracao_field):
        remuneracao_clause = self.salario_camara_municipal_table \
            .insert().values(salario_base=remuneracao_field.salario_base,
                             plano_carreira=remuneracao_field.plano_carreira,
                             gratificacoes=remuneracao_field.gratificacoes,
                             beneficios=remuneracao_field.beneficios,
                             abono=remuneracao_field.abono,
                             adiantamento_salarial=remuneracao_field.adiantamento_salarial,
                             ferias=remuneracao_field.ferias,
                             decimo_terceiro=remuneracao_field.decimo_terceiro,
                             abatimento_de_teto=remuneracao_field.abatimento_de_teto,
                             descontos=remuneracao_field.descontos,
                             salario_bruto=remuneracao_field.salario_bruto,
                             salario_liquido=remuneracao_field.salario_liquido)
        result = self.__db.connection.execute(remuneracao_clause)
        return result.inserted_primary_key

    def create_date(self, date):
        data_clause = self.date_table \
            .insert().values(date=date.data)
        result = self.__db.connection.execute(data_clause)
        return result.inserted_primary_key
