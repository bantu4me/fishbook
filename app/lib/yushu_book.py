from flask import current_app
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

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, get_start(page), current_app.config['PER_PAGE'])
        result = HttpClient.get(url)
        self.keyword = keyword
        self.__fill_page(result)

