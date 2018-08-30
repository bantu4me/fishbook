from .blueprint import web


@web.route('/book/search')
def search():
    return 'hello world'


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass
