from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry

from summary import engine

Register = registry()

test_user_table = Table(
    'test_users',
    Register.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25), nullable=False),
    Column('age', Integer)
)


class TestUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Register.map_imperatively(TestUser, test_user_table)

Register.metadata.create_all(bind=engine)
