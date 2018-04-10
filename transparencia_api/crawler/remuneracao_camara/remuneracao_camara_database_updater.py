from sqlalchemy import Table, Column, Integer, Sequence, Numeric, String, ForeignKey
from transparencia_api.commons.database_communication import DatabaseCommunication


class RemuneracaoCamaraDatabaseUpdater:
    def __init__(self):
        self.db = DatabaseCommunication().connect()

        self.salario_camara_municipal = \
            Table('salario_camara_municipal', self.db.meta,
                  Column('salario_camara_municipal_id', Integer, Sequence('salario_camara_municipal_id_seq'),
                         primary_key=True),
                  Column('salario_base', Numeric),
                  Column('plano_carreira', Numeric),
                  Column('gratificacoes', Numeric),
                  Column('beneficios', Numeric),
                  Column('abono', Numeric),
                  Column('adiantamento_salarial', Numeric),
                  Column('ferias', Numeric),
                  Column('decimo_terceiro', Numeric),
                  Column('abatimento_de_teto', Numeric),
                  Column('descontos', Numeric),
                  Column('salario_bruto', Numeric),
                  Column('salario_liquido', Numeric)
                  )

        self.cargo_reposirtory = \
            Table('cargo', self.db.meta,
                  Column('cargo_id', Integer, Sequence('cargo_id_seq'), primary_key=True),
                  Column('cargo', String)
                  )

        self.data = \
            Table('date', self.db.meta,
                  Column('date_id', Integer, primary_key=True),
                  Column('date', String))

        self.funcionario_publico = \
            Table('funcionario_publico', self.db.meta,
                  Column('funcionario_publico_id', Integer, Sequence('funcionario_publico_id_seq'), primary_key=True),
                  Column('cargo_id', Integer, ForeignKey('cargo.cargo_id')),
                  Column('dado_salario_id', Integer, ForeignKey('dado_salario.dado_salario_id')),
                  Column('date_id', Integer, ForeignKey('date.date_id')),
                  Column('nome', String)
                  )

    def create_dados_remuneracao(self, remuneracao_field):
        remuneracao_clause = self.salario_camara_municipal \
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
        result = self.db.execute(remuneracao_clause)
        return result.inserted_primary_key

    def create_dados_cargos(self, cargo_field):
        cargo_clause = self.cargo_reposirtory \
            .insert().values(cargo=cargo_field.cargo)
        result = self.db.execute(cargo_clause)
        return result.inserted_primary_key

    def create_dados_funcionario(self, funcionario_field):
        funcionario_clause = self.funcionario_publico \
            .insert().values(cargo_id=funcionario_field.cargo_id,
                             dado_salario_id=funcionario_field.dado_salario,
                             date_id=funcionario_field.data_id,
                             nome=funcionario_field.nome)
        result = self.db.execute(funcionario_clause)
        return result.inserted_primary_key

    def create_date(self, date):
        data_clause = self.funcionario_publico \
            .insert().values(date=date.data)
        result = self.db.execute(data_clause)
        return result.inserted_primary_key
