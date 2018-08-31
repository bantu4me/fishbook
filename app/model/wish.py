from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.model.base import Base


class Wish(Base):
    __tablename__ = 'wish'
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    book = relationship('Book')  # type: Book
    isbn = Column(String(length=15), ForeignKey('book.isbn'))