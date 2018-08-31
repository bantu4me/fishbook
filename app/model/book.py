from sqlalchemy import Column, Integer, String

from app.model.base import Base


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    author = Column(String(length=50), nullable=False)
    binding = Column(String(length=30), default='佚名')
    publisher = Column(String(length=50))
    price = Column(String(length=20))
    pages = Column(Integer)
    pubdate = Column(String(length=20))
    isbn = Column(String(length=15), nullable=False, unique=True)
    summary = Column(String(length=1000))
    image = Column(String(length=100))
    title = Column(String(length=30))

    # 模型转dict
    def book_model_to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
