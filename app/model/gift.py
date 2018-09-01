from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
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

    @staticmethod
    def get_recent():
        recent_gifts = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(30).all()
        return recent_gifts

    def get_book_dict(self):
        return self.book.book_model_to_dict()

from app.model.book import Book
from app.model.user import User
