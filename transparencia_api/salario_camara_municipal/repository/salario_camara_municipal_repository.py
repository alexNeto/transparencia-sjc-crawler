from sqlalchemy import Table, Column, Integer, Sequence, Numeric
from transparencia_api.commons.database_communication import DatabaseCommunication


class SalarioCamaraMunicipalRepository:

    def __init__(self):
        self.db = DatabaseCommunication().connect()

