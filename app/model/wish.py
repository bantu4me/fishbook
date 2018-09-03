from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.model.base import Base
from app import db


class Wish(Base):
    __tablename__ = 'wish'
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    book = relationship('Book')  # type: Book
    isbn = Column(String(length=15), ForeignKey('book.isbn'))

    @staticmethod
    def get_wish_cout_by_isbnlist(isbn_list):
        sql_start = 'SELECT isbn,COUNT(isbn) from wish WHERE status=1 AND launched=FALSE and isbn in ('
        sql_end = ') GROUP BY isbn'
        isbn_list_str = ','.join(isbn_list)
        sql = sql_start + isbn_list_str + sql_end
        print(sql)
        isbn_count = db.session.execute(sql).fetchall()
        return isbn_count
