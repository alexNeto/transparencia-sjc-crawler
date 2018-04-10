import sqlalchemy


class DatabaseCommunication:
    """
    Classe par criar comunicação com banco de dados
    Apenas 1 conecção para o projeto
    """

    class __DatabaseCommunication:
        def __init__(self):
            self.__user = "transparencia"
            self.__password = "postgres123"
            self.__database = "transparencia_development"
            self.__host = "localhost"
            self.__port = 5432

        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self):
        if not DatabaseCommunication.instance:
            DatabaseCommunication.instance = DatabaseCommunication.__DatabaseCommunication()
        self.__connection = None
        self.__meta = None

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def connect(self):
        url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
        url = url.format(self.__user, self.__password, self.__host, self.__port, self.__database)
        self.__connection = sqlalchemy.create_engine(url)
        self.__meta = sqlalchemy.MetaData(bind=self.__connection, reflect=True)

    @property
    def connection(self):
        return self.__connection

    @property
    def meta(self):
        return self.__meta
