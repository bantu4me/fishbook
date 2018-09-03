from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from app import db
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
        recent_gifts = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            30).all()
        return recent_gifts

    def get_book_dict(self):
        return self.book.book_model_to_dict()

    @staticmethod
    def my_gift(uid):
        gifts = Gift.query.filter_by(launched=False, uid=uid).all()
        return gifts

    @staticmethod
    def get_gift_cout_by_isbnlist(isbn_list):
        sql_start = 'SELECT isbn,COUNT(isbn) from gift WHERE status=1 AND launched=FALSE and isbn in ('
        sql_end = ') GROUP BY isbn'
        isbn_list_str = ','.join(isbn_list)
        sql = sql_start + isbn_list_str + sql_end
        print(sql)
        isbn_count = db.session.execute(sql).fetchall()
        return isbn_count


from app.model.book import Book
from app.model.user import User
