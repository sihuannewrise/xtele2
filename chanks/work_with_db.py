from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declared_attr, declarative_base


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    pep8 = Pep(
        pep_number=8,
        name='Style Guide for Python Code',
        status='Active'
    )
    pep20 = Pep(
        pep_number=20,
        name='The Zen of Python',
        status='Active'
    )
    pep216 = Pep(
        pep_number=216,
        name='Docstring Format',
        status='Rejected'
    )

    session.add(pep8)
    session.add(pep20)
    session.add(pep216)
    session.commit()
