from sqlalchemy import Column, Numeric, Sequence, Integer, String, ForeignKey

from transparencia_api.commons.database_communication import get_base

base = get_base()


class SalarioCamaraMunicipalTable(base):
    __tablename__ = 'salario_camara_municipal'

    salario_camara_mmunicipal_id = Column('salario_camara_municipal_id', Integer,
                                          Sequence('salario_camara_municipal_id_seq'), primary_key=True)
    salario_base = Column('salario_base', Numeric)
    plano_carreira = Column('plano_carreira', Numeric)
    gratificacao = Column('gratificacao', Numeric)
    beneficio = Column('beneficio', Numeric)
    abono = Column('abono', Numeric)
    adiantamento_salarial = Column('adiantamento_salarial', Numeric)
    ferias = Column('ferias', Numeric)
    decimo_terceiro = Column('decimo_terceiro', Numeric)
    abatimento_teto = Column('abatimento_teto', Numeric)
    descontos = Column('descontos', Numeric)
    salario_bruto = Column('salario_bruto', Numeric)
    salario_liquido = Column('salario_liquido', Numeric)


class CargoTable(base):
    __tablename__ = 'cargo'

    cargo_id = Column('cargo_id', Integer, Sequence('cargo_id_seq'), primary_key=True)
    cargo = Column('cargo', String)


class DateTable(base):
    __tablename__ = 'date'

    date_id = Column('date_id', Integer, Sequence('date_id_seq'), primary_key=True)
    date = Column('date', String)


class FuncionarioPublicoTable(base):
    __tablename__ = 'funcionario_publico'

    funcionario_publico_id = Column('funcionario_publico_id', Integer, Sequence('funcionario_publico_id_seq'),
                                    primary_key=True)
    cargo_id = Column('cargo_id', Integer, ForeignKey('cargo.cargo_id'))
    salario_camara_municipal_id = Column('salario_camara_municipal_id', Integer,
                                         ForeignKey('salario_camara_municipal.salario_camara_municipal_id'))
    date_id = Column('date_id', Integer, ForeignKey('date.date_id'))
    nome = Column('nome', String)
