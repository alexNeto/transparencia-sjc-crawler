from sqlalchemy import Table, Column, Integer, String, Sequence
from transparencia_api.commons.database_communication import DatabaseCommunication


class CargoRepository:

    def __init__(self):
        self.db = DatabaseCommunication().connect()
        self.cargo_reposirtory = \
            Table('cargo', self.db.meta,
                  Column('cargo_id', Integer, Sequence('cargo_id_seq'), primary_key=True),
                  Column('cargo', String)
                  )
