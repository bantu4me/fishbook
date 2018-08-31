from flask import current_app

from app.model.book import Book
from .httpclient import HttpClient


def get_start(page):
    return (page - 1) * current_app.config['PER_PAGE']


class YushuBook:
    # isbn_url = current_app.config['ISBN_URL']
    # keyword_url = current_app.config['KEYWORD_URL']
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def __fill_page(self, data):
        self.total = data['total']
        self.books = data['books']

    def __fill_single(self, book):
        self.total = 1
        self.books.append(book)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, get_start(page), current_app.config['PER_PAGE'])
        result = HttpClient.get(url)
        self.keyword = keyword
        self.__fill_page(result)

    def search_by_isbn(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            book = book.book_model_to_dict()
        else:
            url = self.isbn_url.format(isbn)
            book = HttpClient.get(url)
            # 入库
            self.save_singleBook_to_db(book)
        self.__fill_single(book)

    def save_singleBook_to_db(self, bookDataDic):
        from app import db
        with db.auto_commit():
            book = Book()
            book.set_attr(bookDataDic)
            db.session.add(book)


    @property
    def only(self):
        return self.books[0]
