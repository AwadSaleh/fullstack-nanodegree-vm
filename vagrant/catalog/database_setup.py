import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Store(Base):
    __tablename__ = 'Store'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Store_Item(Base):
    __tablename__ = 'store_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    store_id = Column(Integer, ForeignKey('store.id'))
    store = relationship(Store)


engine = create_engine('sqlite:///onlinstore.db')


Base.metadata.create_all(engine)
