from homework.module17.lecture.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable

class Category(Base):
    __tablename__="categories"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    products = relationship('Priduct', back_populates='category')

print(CreateTable(Category.__table__))






