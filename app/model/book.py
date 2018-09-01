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
        book_dict = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        # 作者如果是多个的话，会被转成字符串，应转为列表结构
        # 如：a,b,c > [a,b,c]
        if ',' in book_dict['author']:
            book_dict['author'] = book_dict['author'].split(',')
        else:
            book_dict['author'] = [book_dict['author']]
        return book_dict

