from sqlalchemy import Column, Integer
from sqlalchemy.orm import declared_attr, DeclarativeBase


class Base(DeclarativeBase):
    __mapper_args__ = {'eager_defaults': True}

    @declared_attr
    def __tablename__(cls):
        return f"astra_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)
