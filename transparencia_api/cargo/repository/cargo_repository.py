class CargoRepository:

    def __init__(self):
        self.__cargo = None

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, value):
        self.__cargo = value
