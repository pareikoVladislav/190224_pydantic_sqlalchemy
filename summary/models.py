from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    TIMESTAMP,
    ForeignKey,
    Boolean,
    func
)
from sqlalchemy.orm import (
    relationship
)

from summary import engine, Base


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(30))
    phone = Column(String(75))
    email = Column(String(75), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    repeat_password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    rating = Column(Float, default=0, nullable=False)
    deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, onupdate=func.current_timestamp())
    deleted_at = Column(TIMESTAMP, nullable=True)

    news = relationship('News', back_populates='user')
    comments = relationship('Comment', back_populates='user')


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    moderated = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, onupdate=func.current_timestamp())
    deleted_at = Column(TIMESTAMP, nullable=True)

    user = relationship('User', back_populates='news')
    comments = relationship('Comment', back_populates='news')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    news_id = Column(Integer, ForeignKey('news.id'))
    deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, onupdate=func.current_timestamp())
    deleted_at = Column(TIMESTAMP, nullable=True)

    user = relationship('User', back_populates='comments')
    news = relationship('News', back_populates='comments')


Base.metadata.create_all(bind=engine)
