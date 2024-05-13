from sqlalchemy import Column, Integer, String, Text, ForeignKey
from test_alchemy import Base, engine

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    surname = Column(String(30), nullable=True)
    age = Column(Integer)
    email = Column(String(75), unique=True)

    address = relationship(
        'Address',
        back_populates='holder',
        uselist=False
    )


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'))
    description = Column(Text)
    city = Column(String(20))
    post_code = Column(Integer, nullable=False, default=11111)

    holder = relationship('User', back_populates='address')


Base.metadata.create_all(engine)
