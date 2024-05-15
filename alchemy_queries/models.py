from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from alchemy_queries import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)

    addresses = relationship('Address', order_by='Address.id', back_populates='user')


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(Text, nullable=False)

    user = relationship('User', back_populates='addresses')


Base.metadata.create_all(engine)
