from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.model.base import Base


class Gift(Base):
    __tablename__ = 'gift'
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')  # type: User
    uid = Column(Integer, ForeignKey('user.id'))
    book = relationship('Book')  # type: Book
    isbn = Column(String(length=15), ForeignKey('book.isbn'))


from app.model.book import Book
from app.model.user import User
