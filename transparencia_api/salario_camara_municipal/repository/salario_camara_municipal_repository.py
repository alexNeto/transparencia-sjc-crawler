from sqlalchemy import Table, Column, Integer, Sequence, Numeric
from transparencia_api.commons.database_communication import DatabaseCommunication


class SalarioCamaraMunicipalRepository:

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
