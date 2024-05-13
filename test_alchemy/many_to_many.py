from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from test_alchemy import Base, engine


tags_association = Table(
    'tags_association',
    Base.metadata,
    Column(
        'product_id',
        Integer,
        ForeignKey('product.id')),
    Column(
        'tag_id',
        Integer,
        ForeignKey('tag.id')
    )
)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float)
    available = Column(Boolean)

    tags = relationship(
        "Tag",
        secondary=tags_association
    )


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)


Base.metadata.create_all(engine)
