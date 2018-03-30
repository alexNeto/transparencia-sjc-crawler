from sqlalchemy import Table, Column, Integer, String, ForeignKey, Sequence
from transparencia_api.commons.database_communication import DatabaseCommunication


class FucionarioPublicoRepository:

    def __init__(self):
        self.db = DatabaseCommunication().connect()

        self.funcionario_publico = \
            Table('funcionario_publico', self.db.meta,
                  Column('funcionario_publico_id', Integer, Sequence('funcionario_publico_id_seq'), primary_key=True),
                  Column('cargo_id', Integer, ForeignKey('cargo.cargo_id')),
                  Column('dado_salario', Integer, ForeignKey('dado_salario.dado_salario_id')),
                  Column('nome', String)
                  )
