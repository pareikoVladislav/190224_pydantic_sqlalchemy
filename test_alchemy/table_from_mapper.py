from sqlalchemy import (
    Table,
    Column,
    Integer,
    String
)

from sqlalchemy.orm import registry

from test_alchemy import engine


Register = registry()


products_table = Table(
    'products',
    Register.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(15)),
    Column('description', String(125), nullable=True),
    Column('price', Integer)
)


class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


Register.map_imperatively(Product, products_table)

Register.metadata.create_all(engine)

